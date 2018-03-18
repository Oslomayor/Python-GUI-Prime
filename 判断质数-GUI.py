# 9:45PM, Mar 10th, 2018 @ HDU_Wireless
# 我的第一个GUI程序
# 判断质数

import tkinter
import math
from tkinter import messagebox

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def response():
    global textbox
    # 排除非法输入
    if textbox.get() == '' or textbox.get().isdigit() == False:
        messagebox.askokcancel("提示框", "请输入一个正整数")
    elif isPrime(int(textbox.get())) == True:
        messagebox.askokcancel("提示框", "是质数")
    else:
        messagebox.askokcancel("提示框", "不是质数")

def main():
    global textbox
    # 主界面
    top = tkinter.Tk(className='判断质数小程序-镇长出品')
    top.minsize(350,200)
    tkinter.Label(top, text='输入整数').place(x=0,y=0)
    # 文本框
    var = tkinter.StringVar()
    textbox = tkinter.Entry(top, textvariable=var)
    textbox.focus_set()
    textbox.place(x=0,y=30)
    # 确定按钮
    tkinter.Button(top, text='确定',command=response).place(x=0,y=60)

    top.mainloop()

if __name__ == '__main__':
    main()