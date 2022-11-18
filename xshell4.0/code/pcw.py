#pcw1.0
window=["mainwindow","window1","window2","window3","window4"]
def setwindow(setstr,windown):
    window[windown-1]=setstr
def returnwindow(windown):
    return window[windown-1]
def runwindow(main,one,two,three,four):
    if main==True:
        print("")    
        print(window[0])
    if one==True:
        print("")
        print(window[1])
    if two==True:
        print("")
        print(window[2])
    if three==True:
        print("")
        print(window[3])
    if four==True:
        print("")
        print(window[4])