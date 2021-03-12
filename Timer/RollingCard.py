from tkinter import *

win=Tk()
win.geometry("1000x500")

def rollingCard():
    global count, card1,card2, card3,card4
    count +=  1
    print('count', count)
    lea = count % 4
    if lea == 0:
        card.config(image=card1)
    elif lea == 1:
        card.config(image=card2)
    elif lea == 2:
        card.config(image=card3)
    elif lea == 3:
        card.config(image=card4)
        
    win.after(10,rollingCard)

rolling = Button(win, text="滾動", command=rollingCard)
rolling.place(x=0,y=0)

cardImg= PhotoImage(file="D:\\2020Python\\我的範例\\poker圖檔\\C11.PNG")
card1= PhotoImage(file="D:\\2020Python\\我的範例\\poker圖檔\\C1.PNG")
card2= PhotoImage(file="D:\\2020Python\\我的範例\\poker圖檔\\C2.PNG")
card3= PhotoImage(file="D:\\2020Python\\我的範例\\poker圖檔\\C3.PNG")
card4= PhotoImage(file="D:\\2020Python\\我的範例\\poker圖檔\\C4.PNG")
count = 0


card=Button(win, text='rollingCard', image=cardImg)
card.place(x=100, y=100)

win.mainloop()