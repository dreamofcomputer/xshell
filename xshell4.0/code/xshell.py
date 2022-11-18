print("start>>ok")
import pcw
pcw.setwindow("---------------\n-mode GUI beta-\n-1.计算器     -\n-2.about      -\n-3.exit       -\n---------------",1)
pcw.setwindow("--------------\n-计算器打开中-\n--------------",2)
pcw.setwindow("-------\n-beta -\n-------",3)
print("GUI>>ok")
import webbrowser
print("web>>ok")
import wget
print("get>>ok")
import matplotlib.pyplot as plt
import numpy as np
print("math>>ok")
import os
print("os>>ok")
print("\n\n")
#start xshell
print("xshell 4.0")
print("python for vscode\n可以输入help来查询输入指令\n")
list=["xshell","web","ofile","exit","help","xsget","xfile","xyplotprint","mode GUI"]
while True:
    text=input("xshell>")
    if text==list[0]:
        print("\nxshell:4.0")
        print("developer:dreamofcomputer")
        print("edition:python for windows\n")
    if text==list[1]:
        webs=input("web>")
        webbrowser.open(webs)
    if text==list[2]:
        filepath=input("file path>")
        ofiles=open(filepath,"r")
        print("")
        print(ofiles.read())
        ofiles.close
        print("")
    if text==list[3]:
        break
    if text==list[4]:
        print("")
        print("xshell-查看此模拟终端版本\nweb-打开网页\nofile-打开txt文件\nxsget-从链接下载文件\nxfile-写入已有txt文件\nxyplotprint-确定两点画线\nmode GUI-打开GUI模式(测试状态)\nhelp-查看指令\nexit-退出")
        print("")
    if text==list[5]:
        webget=input("\nget>")
        path=input("path>")
        wget.download(webget,path)
        print("")
    if text==list[6]:
        thetxtp=input("txt path>")
        writeword=input("write>")
        with open(thetxtp,"a") as addwordfile:
                addwordfile.write(writeword)
        thesonxfiles="1"
        while thesonxfiles=="1":
            thesonxfiles=input("1.继续写下一行\n2.退出\n")
            if thesonxfiles=="1":
                writeword=input("write>")
                with open(thetxtp,"a") as addwordfile:
                    addwordfile.write("\n")
                    addwordfile.write(writeword)
            if thesonxfiles=="2":
                thesonxfiles="2"
    if text==list[7]:
        xprint=input("1点x>")
        yprint=input("1点y>")
        txprint=input("2点x>")
        typrint=input("2点y>")
        xpoints = np.array([xprint , txprint])
        ypoints = np.array([yprint , typrint])
        plt.plot(xpoints, ypoints)
        plt.show()
    if text==list[8]:
        a=1
        while a==1:
            print("")
            pcw.runwindow(True,False,False,False,False)
            wintext=input(">")
            pcw.runwindow(False,wintext=="1",wintext=="2",False,False)
            if wintext=="1":
                from tkinter import *
                def asdf():
                    global c
                    b=Label(a,text="运算符：")
                    b.grid(column=0,row=1)
                    c=Entry()
                    c.grid(column=1,row=1)
                    d=Button(a,text="确定",command=jkl)
                    d.grid(column=2,row=1)
                def jkl():
                    global f
                    e=Label(a,text="第二个数：")
                    e.grid(column=0,row=2)
                    f=Entry()
                    f.grid(column=1,row=2)
                    g=Button(a,text="确定",command=ys)
                    g.grid(column=2,row=2)
                def ys():
                    global a
                    if c.get()=="+" or c.get()=="＋":
                        abc=Label(a,text=int(cc.get())+int(f.get()))
                        abc.grid(column=0,row=4)
                    if c.get()=="-":
                        abc=Label(a,text=int(cc.get())-int(f.get()))
                        abc.grid(column=0,row=4)
                    if c.get()=="*" or c.get()=="x" or c.get()=="X":
                        abc=Label(a,text=int(cc.get())*int(f.get()))
                        abc.grid(column=0,row=4)
                    if c.get()=="/" or c.get()=="÷":
                        abc=Label(a,text=int(cc.get())/int(f.get()))
                        abc.grid(column=0,row=4)
                a=Tk()
                a.geometry("360x180")
                a.title("计算器")
                bb=Label(a,text="第一个数：")
                bb.grid(column=0,row=0)
                cc=Entry()
                cc.grid(column=1,row=0)
                dd=Button(a,text="确定",command=asdf)
                dd.grid(column=2,row=0)
                a.mainloop()
            if wintext=="3":
                a=2