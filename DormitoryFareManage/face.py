#! /usr/bin/python3
import json
from tkinter import *
import tkinter.messagebox   # 用于软件的弹窗
import tkinter.ttk


class Face(object):
    def __init__(self):
        self.root = tkinter.Tk()   # 创建一个根窗口
        self.setAttributes()    # 设置属性
        self.winMenu()  # 设置窗口的菜单
        self.currentFrame = self.winAppendFrame()  # 初始化一个当 前Frame 变量(currentFrame) 实现 窗口内的界面切换
        self.root.mainloop()  # 根窗口循环

    def setAttributes(self):
        """
        窗口基本属性设置
        :return:
        """
        self.root.title("宿舍舍费管理")
        self.root.config(bg='#87CEEB')         # 设置窗口的背景颜色
        self.root.attributes('-alpha', 0.8)    # 设置窗口的透明度
        # 获取屏幕的宽高
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        w = 1010   # 根窗口宽
        h = 700    # 根窗口高
        self.root.geometry("%dx%d+%d+%d" % (w, h, (width - w) / 2, (height - h) / 2))   # 700x700 居中显示

    def winMenu(self):
        """
        设置窗口的菜单的函数
        :return:
        """
        # 新增命令菜单项，使用 add_command() 实现
        def menuCommand1():
            """
            添加 菜单对应的命令
            :return:
            """
            if self.currentFrame != self.winAppendFrame():   # 判断初始化中的currentFrame是否是 winAppendFrame() 返回的frame
                self.currentFrame.pack_forget()  # 取消显示当前界面，并不是销毁
                self.currentFrame = self.winAppendFrame()  # 重新赋值
                self.currentFrame.pack()  # 显示赋值后的当前界面

        def menuCommand():
            """
            查看 菜单对应的命令
            :return:
            """
            if self.currentFrame != self.winLookFrame():
                self.currentFrame.pack_forget()  # 取消显示当前界面，并不是销毁
                self.currentFrame = self.winLookFrame()
                self.currentFrame.pack()

        # 创建一个主目录菜单，也被称为顶级菜单
        mainMenu = Menu(self.root)   # 主目录菜单
        mainMenu.add_command(label="添加", command=menuCommand1)  # 添加 操作的子菜单菜单
        mainMenu.add_command(label="查看", command=menuCommand)   # 查看 操作的子菜单菜单
        # 显示菜单
        self.root.config(menu=mainMenu)   # 将主目录菜单放到根窗口上

    def winAppendFrame(self):
        """
        实现 添加 操作
        :return: appendFrame 添加操作的 frame ,方便实现初始化中 根窗口的界面切换
        """

        # 界面中的一些基本元素的布局
        appendFrame = Frame(self.root, bg="#87CEEB")
        l1 = Label(appendFrame, text="日期:", bg='#87CEEB', font=("黑体", 12, "bold"), width=10, height=2)
        l1.grid(row=0, column=0)
        e1 = Entry(appendFrame, bg="white", font=("黑体", 12, "bold"), width=30)
        e1.grid(row=0, column=1)
        l2 = Label(appendFrame, text="事务:", bg='#87CEEB', font=("黑体", 12, "bold"), width=10, height=2)
        l2.grid(row=1, column=0)
        e2 = Entry(appendFrame, bg="white", font=("黑体", 12, "bold"), width=30)
        e2.grid(row=1, column=1)

        l3 = Label(appendFrame, text="事务金额:", bg='#87CEEB', font=("黑体", 12, "bold"), width=10, height=2)
        l3.grid(row=2, column=0)
        e3 = Entry(appendFrame, bg="white", font=("黑体", 12, "bold"), width=30)
        e3.grid(row=2, column=1)
        l4 = Label(appendFrame, text="备注:", bg='#87CEEB', font=("黑体", 12, "bold"), width=10, height=2)
        l4.grid(row=3, column=0)
        e4 = Entry(appendFrame, bg="white", font=("黑体", 12, "bold"), width=30)
        e4.grid(row=3, column=1)

        def commitFunc():
            """
            将数据保存到 data.json文件中，对应界面中的 Commit 按钮
            :return:
            """
            if (e1.get() != "") and (e2.get() != "") and (e3.get() != ""):  # 通过这个判断实现前3项必填
                with open("data.json", mode="r", encoding="utf-8") as fi:
                    data = json.load(fi)   # 读取json文件中的数据
                    yv_e = float(data[-1]["余额"]) + float(e3.get())  # 计算余额

                dataDict = {"日期": e1.get(), "事务": e2.get(), "事务金额": e3.get(), "余额": "{}".format(yv_e),
                            "备注": e4.get()}    # 获取窗体中的数据和yv_e数据组成字典数据
                data.append(dataDict)  # 向json文件中的数据中，添加新的 数据--> dataDict

                with open("data.json", mode="w", encoding="utf-8") as fo:
                    json.dump(obj=data, fp=fo, indent=4, ensure_ascii=False)   # 重新写入json数据

                # 下面是两个弹窗提示
                tkinter.messagebox.showinfo("提交数据", "数据提交成功！！")
                tkinter.messagebox.showinfo("提交数据", "请查看！！")

                # 数据提交成功时，需要将原来的数据清空
                e1.delete(0, "end")
                e2.delete(0, "end")
                e3.delete(0, "end")
                e4.delete(0, "end")

            else:  # 数据不全时，会通过弹窗提示
                tkinter.messagebox.showinfo("提交数据", "数据不全！！")
                tkinter.messagebox.showinfo("提示", "前3项必填。")

        # 右下方的 数据提交 按钮
        b1 = Button(appendFrame, text="Commit", font=("黑体", 15, "bold"), width=10, height=2, command=commitFunc)
        b1.grid(row=4, column=2)
        return appendFrame

    def winLookFrame(self):
        """
        实现 查看 操作
        :return: lookFrame 添加操作的 frame ,方便实现初始化中 根窗口的界面切换
        """
        lookFrame = Frame(self.root, bg="white", width=80, height=100)

        # 表格的标题
        l1 = Label(lookFrame, text="宿舍费用表", bg='#87CEEB', font=("黑体", 12, "bold"), width=111, height=2)
        l1.pack()

        # 表格的 字段 的数据----------列
        table = tkinter.ttk.Treeview(lookFrame, columns=("c1", "c2", "c3", "c4", "c5"), height=28, show="headings")
        table.heading("c1", text="日期")
        table.heading("c2", text="事务")
        table.heading("c3", text="事务金额")
        table.heading("c4", text="余额")
        table.heading("c5", text="备注")

        def dataInsert():
            """
            读取json文件中的数据，实现数据展示
            :return:
            """
            table.delete(*table.get_children())  # 在每一次刷新数据的时候，需要先将表中的数据清空
            with open("data.json", mode="r", encoding="utf-8") as fi:
                for uni in json.load(fi):
                    # 将每一条数据插入到表格中
                    table.insert("", "end", values=(
                        f'{uni["日期"]}', f'{uni["事务"]}', f'{uni["事务金额"]}', f'{uni["余额"]}', f'{uni["备注"]}'))

        table.pack()  # 显示表

        # 数据刷新按钮
        b2 = Button(lookFrame, text="刷新", bg='#87CEEB', font=("黑体", 12, "bold"), width=10, height=2,
                    command=dataInsert)
        b2.pack()
        return lookFrame


face = Face()  # 创建对象
