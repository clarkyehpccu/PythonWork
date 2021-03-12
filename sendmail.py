from tkinter import *
def showselect(evt): 
    print('selected',svar.get())
def showselectdatatype():
    print(type(svar.get()))      
win = Tk() 
win.geometry('400x300') 
win.title("watch StringVar()") 

listx = ['T1', 'T2', 'T3', 'T4', (100,200,300)]
print('listx', type(listx)) #class list

print('tuplex', type(tuplex))  #class tuple
svar = StringVar() 
svar.set((100)) #string 指定給StringVar物件
opm = OptionMenu(win, svar, *listx, command=showselect)
opm.grid(row=0,column=0) 

show=Button(win,text="show",command=showselectdatatype)
show.grid(row=0,column=1) 


win.mainloop() 
