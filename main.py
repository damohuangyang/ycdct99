import tkinter as tk
from tkinter import messagebox

def main():
    root = tk.Tk()
    root.title("YCDCT99 心理健康测试")
    root.geometry("420x260")
    root.resizable(False, False)

    label = tk.Label(
        root,
        text="欢迎使用 YCDCT99 心理健康测试\n\n这是一个示例 GUI 程序",
        font=("Microsoft YaHei", 12),
        justify="center"
    )
    label.pack(pady=40)

    def on_click():
        messagebox.showinfo(
            "测试完成",
            "测试结果：\n\n你的心理状态良好 😊"
        )

    btn = tk.Button(
        root,
        text="开始测试",
        font=("Microsoft YaHei", 11),
        width=15,
        command=on_click
    )
    btn.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import messagebox

def main():
    root = tk.Tk()
    root.title("YCDCT99 心理健康测试")
    root.geometry("400x250")
    root.resizable(False, False)

    label = tk.Label(
        root,
        text="欢迎使用 YCDCT99 心理健康测试\n\n这是一个示例 GUI 程序",
        font=("微软雅黑", 12),
        justify="center"
    )
    label.pack(pady=30)

    def on_click():
        messagebox.showinfo(
            "提示",
            "程序运行正常 ✅\n\n这是一个正式 GUI 测试版本"
        )

    btn = tk.Button(
        root,
        text="开始测试",
        font=("微软雅黑", 11),
        width=15,
        command=on_click
    )
    btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
