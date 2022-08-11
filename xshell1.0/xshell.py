import webbrowser
import wget
print("xshell 1.0")
print("python for vscode\n可以输入help来查询输入指令")
list=["xshell","web","ofile","exit","help","xsget"]
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
        print("\n[xshell][web][ofile][xsget][exit][help]\n")
    if text==list[5]:
        webget=input("\nget>")
        path=input("path>")
        wget.download(webget,path)
        print("")