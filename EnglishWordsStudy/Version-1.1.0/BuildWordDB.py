import json

from db import Pool, Execute

sql_create_db = "CREATE DATABASE all_words CHARACTER SET 'utf8';"
sql_create_tb = "CREATE TABLE IF NOT EXISTS word_for_cet6(word VARCHAR(30),mean VARCHAR(300));"

with open("db_config.txt", mode="r", encoding="utf-8") as fi:
    info = eval(fi.read())
    # 配置文件中的 数据库信息
    # ('root', 'linux09180974', 3306, 'localhost', 'all_words', 'utf8')
    # 用户名        密码       数据库端口号   主机地址    现有的数据库    数据库的编码格式
    pool = Pool()
    pool.setDbInfo(*info)
    pool.connPoolCreate(1)
    conn = pool.getConnection()
    Execute.conn = conn
    execute_dat_ = [sql_create_db, "use all_words;", sql_create_tb]

    # 读取 wordsSQL.json 中的sql数据 执行sql数据，将数据写入数据库
    with open("wordsSQL.json", mode="r", encoding="utf-8") as f:
        execute_dat_ += json.load(f)

    # 使用现有的数据库，执行 新建数据库和数据表，并在数据表中写入 单词数据
    Execute.manySQL(execute_dat_)
    pool.returnConnection(connection=conn)

    # 将原有的 dbdb_config.txt 修改为 新的数据库信息
    info = list(info)
    info[4] = "all_words"
    info = tuple(info)
    with open("db_config.txt", mode="w", encoding="utf-8") as fo:
        fo.write(str(info))
