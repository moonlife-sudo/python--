# main.py

import tkinter as tk
from tkinter import messagebox
from get_library_seats import get_library_seats

class SeatBookingApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("图书馆座位预约")

        # 设置字体
        font_label = ("Arial", 12)
        font_entry = ("Arial", 12)
        font_button = ("Arial", 14, "bold")

        # 用户名
        self.username_label = tk.Label(self.root, text="用户名:", font=font_label)
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root, font=font_entry)
        self.username_entry.pack()

        # 密码
        self.password_label = tk.Label(self.root, text="密码:", font=font_label)
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show="*", font=font_entry)
        self.password_entry.pack()

        # 日期
        self.date_label = tk.Label(self.root, text="日期(yyyy-mm-dd):", font=font_label)
        self.date_label.pack()
        self.date_entry = tk.Entry(self.root, font=font_entry)
        self.date_entry.pack()

        # 时间戳
        self.timestamp_label = tk.Label(self.root, text="时间戳(hh:mm-hh:mm):", font=font_label)
        self.timestamp_label.pack()
        self.timestamp_entry = tk.Entry(self.root, font=font_entry)
        self.timestamp_entry.pack()

        # 座位号选择列表
        self.floor_var = tk.StringVar(self.root)
        self.floor_var.set("请选择楼层")
        self.floor_options = list(floor_dict.keys())
        self.floor_menu = tk.OptionMenu(self.root, self.floor_var, *self.floor_options)
        self.floor_menu.config(font=font_entry)
        self.floor_menu.pack()

        # 座位号
        self.seats_label = tk.Label(self.root, text="座位号:", font=font_label)
        self.seats_label.pack()
        self.seats_entry = tk.Entry(self.root, font=font_entry)
        self.seats_entry.pack()

        # 提交按钮
        self.submit_button = tk.Button(self.root, text="提交", command=self.on_submit, font=font_button)
        self.submit_button.pack()

        # 设置窗口关闭事件
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # 设置窗口大小
        self.root.geometry("400x400")

        self.root.mainloop()

    def on_submit(self):
        # 获取用户输入
        username = self.username_entry.get()
        password = self.password_entry.get()
        date = self.date_entry.get()
        timestamp = self.timestamp_entry.get()
        seats_number = self.seats_entry.get()
        choose_floor = floor_dict.get(self.floor_var.get())

        # 进行输入格式检查
        if not (username and password and date and timestamp and seats_number and choose_floor):
            messagebox.showerror("错误", "请填写所有字段")
            return

        # 进行进一步的输入格式检查（这里可以根据需要进行具体的格式检查）

        # 创建座位预约实例并调用登录方法
        seat_booking = get_library_seats(username, password, choose_floor, date, timestamp, seats_number)
        seat_booking.login()

    def on_close(self):
        # 添加关闭窗口时的逻辑，例如询问用户是否确认关闭
        user_confirmation = messagebox.askokcancel("确认关闭", "您确定要关闭窗口吗？")
        if user_confirmation:
            self.root.destroy()

# 替换为实际的 floor_dict
floor_dict = {"图书馆二层A区": "100455344",
              "图书馆二层B区": "100455346",
              "图书馆三层A区": "100455350",
              "图书馆三层B区": "100455352",
              "图书馆三层C区": "100455354",
              "图书馆三层夹层": "111488386",
              "图书馆四层": "100455356",
              "图书馆四层夹层": "111488388",
              "图书馆五层": "100455358",
              "图书馆六层": "100455360"}

# 启动应用
app = SeatBookingApp()
