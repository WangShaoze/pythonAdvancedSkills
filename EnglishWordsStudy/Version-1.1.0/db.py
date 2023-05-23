import re

import pymysql

import netSearchEngine


class Pool(object):
    """
    创建数据库的连接池
    """

    def __init__(self):
        self.__user = ""
        self.__password = ""
        self.__port = 3306
        self.__database = ""
        self.__host = "localhost"
        self.__charset = "utf-8"
        self.__pool = []

    def setDbInfo(self, user: str, password: str, port: int, host: str, database: str, charset: str):
        """
        这个函数用于设置数据库信息
        :param user:
        :param password:
        :param port:
        :param host:
        :param database:
        :param charset: 指定字符集
        :return:
        """
        self.__user = user
        self.__password = password
        self.__port = port
        self.__host = host
        self.__database = database
        self.__charset = charset

    def getDbInfo(self):
        """
        获取用户信息
        :return:
        """
        return self.__user, self.__password, self.__port, self.__host, self.__database, self.__charset

    def getConnection(self):
        """
        获取一个链接
        :return:
        """
        return self.__pool.pop()

    def returnConnection(self, connection: pymysql.Connection):
        """
        将连接放回连接池
        :param connection:
        :return:
        """
        if connection is not None:
            self.__pool.append(connection)

    def connPoolCreate(self, num: int = 5):
        """
        创建连接 当连接数小于3的时候就会创建
        :param num:
        :return:
        """
        if len(self.__pool) <= 4:
            for i in range(num):
                conn = pymysql.Connection(user=self.__user, password=self.__password, port=self.__port,
                                          host=self.__host,
                                          database=self.__database, charset=self.__charset)
                self.__pool.append(conn)

    def getPoolSize(self):
        """
        获取连接池中存在连接的数目
        :return:
        """
        return len(self.__pool)

    def __del__(self):
        """
        在退出时销毁连接
        :return:
        """
        for conn in self.__pool:
            conn.close()


class Execute:
    """
    执行SQL语句的执行类，需要在类中指定与MySQL的连接
    """
    conn: pymysql.Connection = None  # 需要一个与数据库的连接

    @classmethod
    def uniSQL(cls, sql: str):
        """
        执行当条没有返回数据的SQL语句
        :param sql: 需要执行的SQL
        :return:
        """
        flag = False
        cursor = cls.conn.cursor()
        try:
            cursor.execute(sql)
            flag = True
        except Exception as e:
            print(e)
        cursor.close()
        cls.conn.commit()  # 还回连接时一定要提交数据
        return flag

    @classmethod
    def uniSQL_getData(cls, sql: str):
        """
        执单挑有返回值的SQL语句
        :param sql: 需要执行的SQL
        :return: 执行的结果
        """
        cursor = cls.conn.cursor()
        cursor.execute(sql)
        data = [uni for uni in cursor.fetchall()]
        if data == list():
            prog = re.compile("select mean from word_for_cet6 where word='(?P<word>.*?)';", re.S)
            word = prog.findall(sql)[0]
            cls.manySQL(netSearchEngine.engine(word))
            data = cls.uniSQL_getData(sql)
        cursor.close()
        return data

    @classmethod
    def manySQL(cls, sql_li: list):
        """
        执行当条没有返回数据的SQL语句
        :param sql_li: 需要执行的多条SQL的列表
        :return:
        """
        cursor = cls.conn.cursor()
        for sql in sql_li:
            try:
                cursor.execute(sql)
            except Exception as e:
                print(e)
        cursor.close()
        cls.conn.commit()  # 还回连接时一定要提交数据

    @classmethod
    def manySQL_getData(cls, sql_li: list):
        """
        执行多条有返回值的SQL语句
        :param sql_li: 需要执行的多条SQL的列表
        :return: 执行的结果
        """
        cursor = cls.conn.cursor()
        data = []
        for sql in sql_li:
            cursor.execute(sql)
            data += [uni for uni in data]
        cursor.close()
        return data


if __name__ == '__main__':
    pool = Pool()
    info = eval(open("db_config.txt", mode="r", encoding="utf-8").read())
    pool.setDbInfo(*info)
    # print(pool.getDbInfo())
    pool.connPoolCreate(2)
    connection_ = pool.getConnection()
    # print(pool.getPoolSize())
    # pool.returnConnection(connection_)
    # print(pool.getPoolSize())
    Execute.conn = connection_
    dat = Execute.uniSQL_getData("select mean from word_for_cet6 where word='{}';".format("pity"))
    print(dat)
