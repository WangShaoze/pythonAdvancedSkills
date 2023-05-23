#! /usr/bin/python3
import os
from tkinter import *
import tkinter.ttk
import tkinter.messagebox
from db import Pool, Execute
from netSearchEngine import engine


class Face(object):
    def __init__(self):
        self.pool = self.setPoolAttributes()
        self.root = Tk()
        self.setAttributes()
        self.winMenu()
        self.currentFrame = self.winSearchFrame()  # 初始化一个当 前Frame 变量(currentFrame) 实现 窗口内的界面切换
        self.root.mainloop()

    @staticmethod
    def setPoolAttributes():
        pool = Pool()
        info = eval(open("db_config.txt", mode="r", encoding="utf-8").read())
        pool.setDbInfo(*info)
        pool.connPoolCreate(num=4)
        return pool

    def setAttributes(self):
        self.root.title("SearchWord")
        self.root.attributes("-alpha", 0.8)
        win_w = self.root.winfo_screenwidth()
        win_h = self.root.winfo_screenheight()
        w = 700
        h = 500
        self.root.geometry("%dx%d+%d+%d" % (w, h, (win_w - w) / 2, (win_h - h) / 2))
        self.root.config(bg="#da765b")

    def winMenu(self):
        def menuCommand1():
            if self.currentFrame != self.winSearchFrame():
                self.currentFrame.pack_forget()
                self.currentFrame = self.winSearchFrame()
                self.currentFrame.pack()

        def menuCommand2():
            if self.currentFrame != self.winAppendFrame():
                self.currentFrame.pack_forget()
                self.currentFrame = self.winAppendFrame()
                self.currentFrame.pack()

        def menuCommand3():
            if self.currentFrame != self.winSearchChineseFrame():
                self.currentFrame.pack_forget()
                self.currentFrame = self.winSearchChineseFrame()
                self.currentFrame.pack()

        def menuCommand4():
            if self.currentFrame != self.winCreateMDFrame():
                self.currentFrame.pack_forget()
                self.currentFrame = self.winCreateMDFrame()
                self.currentFrame.pack()

        def menuCommand():
            if self.currentFrame != self.winUpdateFrame():
                self.currentFrame.pack_forget()
                self.currentFrame = self.winUpdateFrame()
                self.currentFrame.pack()

        maniMenu = Menu(self.root)
        maniMenu.add_command(label="查词", command=menuCommand1)
        maniMenu.add_command(label="中文查词", command=menuCommand3)
        maniMenu.add_command(label="添加词语", command=menuCommand2)
        maniMenu.add_command(label="修改词汇信息", command=menuCommand)
        maniMenu.add_command(label="CreateMdFile", command=menuCommand4)
        self.root.config(menu=maniMenu)

    def winSearchFrame(self):
        searchFrame = Frame(self.root, bg="#da765b")
        varS = StringVar()

        l1 = Label(searchFrame, text="输入英语单词:", font=("黑体", 16, "bold"), bg="#da765b", width=10, height=2)
        l1.grid(row=0, column=0)
        e1 = Entry(searchFrame, font=("黑体", 16, "bold"), width=20)
        e1.grid(row=0, column=1)
        l2 = Label(searchFrame, text="单词意思:", font=("黑体", 16, "bold"), bg="#da765b", width=10, height=2)
        l2.grid(row=1, column=0)
        l3 = Label(searchFrame, textvariable=varS, font=("黑体", 12, "bold"), bg="#da765b", width=25, height=2)
        l3.grid(row=1, column=1)
        t1 = Text(searchFrame, width=40, height=9, font=("黑体", 15, "bold"))
        t1.grid(row=2, columnspan=3)

        def search():
            t1.delete("1.0", "end")
            word = e1.get()
            if word == "":
                tkinter.messagebox.showinfo("提示", "单词信息不能为空！")
                return
            conn = self.pool.getConnection()
            Execute.conn = conn
            mean = Execute.uniSQL_getData(f"select mean from word_for_cet6 where word='{word}';")
            if mean == list():
                varS.set("数据库中没有查到该词！")
                l3.config(bg="#abc88b")
                Execute.manySQL(engine(word))
                tkinter.messagebox.showinfo("提示", "已通过网络查找，写入数据库，请重试！")
            else:
                t1.insert("1.0", mean[0][0])
                varS.set("查询成功！！")
                l3.config(bg="#abc88b")
            self.pool.returnConnection(conn)

        def search_bind(evt):
            search()

        e1.bind('<Return>', search_bind)  # 将 Entry-e1 控件和 Enter 绑定

        b1 = Button(searchFrame, text="GO", font=("黑体", 16, "bold"), bg="#9b95c9", width=10, height=2, command=search)
        b1.grid(row=3, column=3)
        return searchFrame

    def winSearchChineseFrame(self):
        searchChineseFrame = Frame(self.root, bg="#da765b")
        l1 = Label(searchChineseFrame, text="输入中文词:", bg="#da765b", font=("黑体", 16, "bold"), width=10, height=2)
        l1.grid(row=0, column=0)
        e1 = Entry(searchChineseFrame, font=("黑体", 16, "bold"), width=20)
        e1.grid(row=0, column=1)
        l2 = Label(searchChineseFrame, text="单词及寓意:", bg="#da765b", font=("黑体", 16, "bold"), width=10, height=2)
        l2.grid(row=1, column=0)
        t1 = Text(searchChineseFrame, width=40, height=9, font=("黑体", 15, "bold"))
        t1.grid(row=2, columnspan=3)

        def search():
            t1.delete("1.0", "end")
            chinese = e1.get()
            if chinese == '':
                tkinter.messagebox.showinfo("提示", "中文词不能为空！！")
                return
            conn = self.pool.getConnection()
            Execute.conn = conn
            mean = Execute.uniSQL_getData(
                f"select word,mean from word_for_cet6 where mean like '%{chinese}%' or word like '%{chinese}%';")
            if mean == list():
                tkinter.messagebox.showinfo("提示", "数据库没有对应信息！！")
                Execute.manySQL(engine(chinese))
                tkinter.messagebox.showinfo("提示", "已通过网络查找，写入数据库，请重试！")
            else:
                for uni in mean:
                    sd = uni[0] + ":\n\t" + uni[1] + "\n" + "---" * 20 + "\n"
                    t1.insert("1.0", sd)
            self.pool.returnConnection(conn)

        def search_bind(evt):
            search()

        e1.bind('<Return>', search_bind)  # 将 Entry-e1 控件和 Enter 绑定

        b1 = Button(searchChineseFrame, text="GO", font=("黑体", 16, "bold"), bg="#9b95c9", width=10, height=2,
                    command=search)
        b1.grid(row=3, column=3)

        return searchChineseFrame

    def winAppendFrame(self):
        appendFrame = Frame(self.root, bg="#da765b")
        l1 = Label(appendFrame, text="单词:", bg="#da765b", font=("黑体", 16, "bold"), width=10, height=2)
        l1.grid(row=0, column=0)
        e1 = Entry(appendFrame, font=("黑体", 16, "bold"), width=20)
        e1.grid(row=0, column=1)

        l2 = Label(appendFrame, text="意思及词性:", bg="#da765b", font=("黑体", 16, "bold"), width=10, height=2)
        l2.grid(row=1, column=0)
        e2 = Entry(appendFrame, font=("黑体", 16, "bold"), width=20)
        e2.grid(row=1, column=1)

        def appendWord():
            word = e1.get()
            mean = e2.get()
            if word == "" or mean == "":
                tkinter.messagebox.showinfo("提示", "单词信息不能为空！")
                flag = False
            else:
                conn = self.pool.getConnection()
                Execute.conn = conn
                flag = Execute.uniSQL(f"insert into word_for_cet6 values('{word}', '{mean}');")
                self.pool.returnConnection(conn)
            if flag:
                tkinter.messagebox.showinfo("提示", "单词添加成功*--*  ")
                e1.delete(0, "end")
                e2.delete(0, "end")
            else:
                tkinter.messagebox.showinfo("提示", "单词添加失败，清重试！")

        b1 = Button(appendFrame, text="Commit", font=("黑体", 16, "bold"), bg='#9b95c9', width=10, height=2,
                    command=appendWord)
        b1.grid(row=2, column=3)

        return appendFrame

    def winUpdateFrame(self):
        updateFrame = Frame(self.root, bg="#da765b")
        l1 = Label(updateFrame, text="需要修改的单词:", bg="#da765b", font=("黑体", 16, "bold"), width=15, height=2)
        l1.grid(row=0, column=0)
        e1 = Entry(updateFrame, font=("黑体", 16, "bold"), width=20)
        e1.grid(row=0, column=1)

        t1 = Text(updateFrame, font=("黑体", 15, "bold"), height=9, width=40)
        t1.grid(row=1, columnspan=3)

        def search(eve):
            word = e1.get()
            if word == "":
                tkinter.messagebox.showinfo("提示", "单词信息不能为空！")
                return
            t1.delete("1.0", "end")
            conn = self.pool.getConnection()
            Execute.conn = conn
            mean = Execute.uniSQL_getData(f"select mean from word_for_cet6 where word='{word}';")
            if mean == list():
                tkinter.messagebox.showinfo("提示", "数据库中没有查到该词！")
                Execute.manySQL(engine(word))
                tkinter.messagebox.showinfo("提示", "已通过网络查找，写入数据库，请重试！")
            else:
                t1.insert("1.0", mean[0][0])
            self.pool.returnConnection(conn)

        e1.bind('<Return>', search)  # 将 Entry-e1 控件和 Enter 绑定

        def updateWordInfo():
            word = e1.get()
            if word == "":
                tkinter.messagebox.showinfo("提示", "单词信息不能为空！")
                return
            mean_new = t1.get("1.0", "end")
            conn = self.pool.getConnection()
            Execute.conn = conn
            flag = Execute.uniSQL(f"UPDATE word_for_cet6 SET mean = '{mean_new}' WHERE word = '{word}';")
            self.pool.returnConnection(conn)
            if flag:
                tkinter.messagebox.showinfo("提示", "单词信息修改成功！")
            else:
                tkinter.messagebox.showinfo("提示", "单词有误！")

        b1 = Button(updateFrame, text="Commit", font=("黑体", 16, "bold"), bg='#9b95c9', width=10, height=2,
                    command=updateWordInfo)
        b1.grid(row=2, column=3)

        return updateFrame

    def winCreateMDFrame(self):
        createMdFileFrame = Frame(self.root, bg="#da765b")

        def convertTOmd():
            head = """### 单词学习\n|单词|词性和意思|\n|:------:|-----------:|\n"""
            content = t1.get("1.0", "end")
            conn = self.pool.getConnection()
            Execute.conn = conn
            if content:
                word_li = content.strip().split("\n")
                for uni in word_li:
                    if uni == "" or uni == "\n":
                        continue
                    mean = Execute.uniSQL_getData("select mean from word_for_cet6 where word='{}';".format(uni))
                    mean = str(mean[0][0]).replace("\n", "  ")
                    head += "|{}|{}|\n".format(uni, mean)
                if e1.get() != "":
                    fileName = e1.get()
                    if str(e1.get()).find(".md"):
                        fileName = e1.get().strip().strip(".md")
                    try:
                        with open(f"MdFiles/{fileName}.md", mode="w", encoding="utf-8") as f:
                            f.write(head)
                    except Exception as e:
                        print("e:", e)  # e: [Errno 2] No such file or directory: 'MdFiles/C.md'
                        if "No such file or directory" in str(e):
                            os.mkdir("./MdFiles")
                            with open(f"MdFiles/{fileName}.md", mode="w", encoding="utf-8") as f:
                                f.write(head)
                else:
                    try:
                        with open(f"MdFiles/YourFile.md", mode="w", encoding="utf-8") as f:
                            f.write(head)
                    except Exception as e:
                        print("e:", e)  # e: [Errno 2] No such file or directory: 'MdFiles/YourFile.md'
                        if "No such file or directory" in str(e):
                            os.mkdir("./MdFiles")
                            with open(f"MdFiles/YourFile.md", mode="w", encoding="utf-8") as f:
                                f.write(head)
                tkinter.messagebox.showinfo("提示", "文件生成成功。")
            else:
                # 提示
                tkinter.messagebox.showinfo("提示", "单词为空！！")
            self.pool.returnConnection(conn)

        l1 = Label(createMdFileFrame, text="需要转换的词汇:", bg="#da765b", font=("黑体", 16, "bold"), width=20,
                   height=2)
        l1.grid(row=0, columnspan=2)
        t1 = Text(createMdFileFrame, width=40, height=9, font=("黑体", 15, "bold"))
        t1.grid(row=1, rowspan=4, columnspan=3)

        l2 = Label(createMdFileFrame, text="文件名:", bg="#da765b", font=("黑体", 16, "bold"), width=5,
                   height=2)
        l2.grid(row=5, column=1)
        e1 = Entry(createMdFileFrame, font=("黑体", 16, "bold"), width=15)
        e1.grid(row=5, column=2)
        b1 = Button(createMdFileFrame, text="转MD", font=("黑体", 16, "bold"), bg='#9b95c9', width=10, height=2,
                    command=convertTOmd)
        b1.grid(row=5, column=3)
        return createMdFileFrame


face = Face()
