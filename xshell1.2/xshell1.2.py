import webbrowser
import wget
print("xshell 1.2")
print("python for vscode\n可以输入help来查询输入指令")
list=["xshell","web","ofile","exit","help","xsget","xfile"]
while True:
    text=input("xshell>")
    if text==list[0]:
        print("\nxshell:1.0")
        print("developer:dreamofcomputer")
        print("edition:exe for windows\n")
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
        print(list)
        print("xshell-查看此模拟终端版本\nweb-打开网页\nofile-打开txt文件\nexit-退出\nhelp-查看指令\nxsget-从链接下载文件\nxfile-写入已有txt文件")
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