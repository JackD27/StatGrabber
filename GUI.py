from tkinter import *
from tkinter import ttk
import webbrowser
from PrizePickTransfer import *
import os
from variables import Compute
import itertools
import math

computeWords = Compute()
    
def myClick():
    try:
        sport = entry3.get()
        if len(sport) < 1:
            sport = None
        file = fileGrabber(sport)
        myLabel4['fg'] = "green"
        myLabel4['text'] = "Success! Saved to:",os.getcwd()
        file.to_csv('PrizePicksDataFrame.csv', index = False)
        entry3.delete(0, END)
    except:
        myLabel4['text'] = "Error Occurred! No internet/Code error."
        myLabel4['fg'] = "red"
        entry3.delete(0, END)
        
def myClick2():
    try:
        sport = entry3.get()
        if len(sport) < 1:
            sport = None
        file2 = fileGrabber2(sport)
        myLabel4['fg'] = "green"
        myLabel4['text'] = "Success! Saved to:",os.getcwd()
        file2.to_csv('UnderDogDataFrame.csv', index = False)
        entry3.delete(0, END)
    except:
        myLabel4['text'] = "Error Occurred! No internet/Code error."
        myLabel4['fg'] = "red"
        entry3.delete(0, END)

def clickUrl(url):
         webbrowser.open_new_tab(url)  
         

def addName():
        word = entry.get()
        if len(word) > 0:
            entry.delete(0, END)
            myListbox.insert(END, word)

def delName():
          myListbox.delete(ANCHOR)

def delAll():
          myListbox.delete(0, END)
          
def clearAll():
    for item in treeBox.get_children():
        treeBox.delete(item)
          
names = []

def compute():
        word2 = entry2.get()
        try:
            number = int(word2)
            if number > 0:
                if myListbox.size() > 0:
                    names.clear()
                    entry2.delete(0, END)
                    computeWords.setNumber(number)
                    for i, name in enumerate(myListbox.get(0, END)):
                        names.append(name)
                    myLabel5['fg'] = "#86c5da"
                    myLabel5['text'] = 'There are',math.comb(len(names), computeWords.getNumber()),'combinations.'
                    dataframe = pd.DataFrame(list(itertools.combinations(names,computeWords.getNumber())))
                    clearAll()
                    cols = list(dataframe.columns)
                    treeBox["columns"] = cols
                    for i in cols:
                        treeBox.column(i, anchor="w")
                        treeBox.heading(i, text=i, anchor='w')
                    for index, row in dataframe.iterrows():
                        treeBox.insert("",0,text=index,values=list(row))
                else:
                    myLabel5['text'] = "List of names is empty."
                    myLabel5['fg'] = "red"
        except:
            myLabel5['text'] = "Enter a valid number"
            myLabel5['fg'] = "red"
        

root = Tk()
root.title("Stat Grabber!!!")


root.geometry('690x600')
root.configure(bg='#293145')

myFrame = Frame(root, background='#313D56')
myFrame2 = Frame(root, background='#313D56')
myFrame3 = Frame(root, background='#313D56')

entry = Entry(master=myFrame2, bg='#343434', fg='silver')
entry2 = Entry(master=myFrame3, width=10, bg='#343434', fg='silver')
myLabel5 = Label(myFrame3, text='', fg='red', background='#313D56')

myButton2 = Button(myFrame2, text="ADD", command=addName, state='normal', cursor='hand2', width=10, bg='#677BAD', fg='white')
myButton3 = Button(myFrame2, text="DELETE", command=delName, state='normal', cursor='hand2', width=10, bg='#677BAD', fg='white')
myButton4 = Button(myFrame2, text="DELETE ALL", command=delAll, state='normal', cursor='hand2', width=10, bg='#677BAD', fg='white')
myButton5 = Button(myFrame3, text="Compute", command=compute, state='normal', cursor='hand2', width=10, bg='#677BAD', fg='white')
#677BAD

myLabel2 = Label(myFrame, text="PrizePicks and UnderDogFantasy", fg='#86c5da', background='#313D56')
myLabel = Label(myFrame, text="Click Link and paste into: PrizePicksdata.json", cursor='hand2', background='#313D56', fg='white')
myLabel.bind("<Button-1>", lambda e:clickUrl('https://api.prizepicks.com/projections'))
entry3 = Entry(master=myFrame, width=10, bg='#343434', fg='silver')
myLabel4 = Label(myFrame, text='', fg='green', background='#313D56')
myButton = Button(myFrame, text="Click for PrizePick CSV", command=myClick, state='normal', cursor='hand2', bg='#677BAD', fg='white')
myButton6 = Button(myFrame, text="Click for UnderDog CSV", command=myClick2, state='normal', cursor='hand2', bg='#677BAD', fg='white')





myFrame.grid(row=0, column=0, padx= 10, pady=10, sticky='W')
myFrame2.grid(row=0, column=0, padx= 300, pady=10, sticky='E')
myFrame3.grid(row=1, column=0, columnspan=1, padx=10, pady=10, sticky='W')

entry.grid(row=0, column=0, padx= 10, pady=10)

myButton2.grid(row=0, column=1, padx= 10, pady=10)
myButton3.grid(row=1, column=2, padx= 10, pady=10)
myButton4.grid(row=1, column=2, padx= 10, pady=10, sticky='S')
entry3.grid(row=4, column=0, padx= 10, pady=10)

myListbox = Listbox(myFrame2, width=40, bg='#343434', fg='silver', selectbackground='#00008b', height=8)
myListbox.grid(row=1, column=0, columnspan=2 ,padx= 10, pady=10, sticky = 'W')

treeBox = ttk.Treeview(myFrame3)
treeBox.grid(row=1, column=0, columnspan=2 ,padx= 10, pady=10, sticky = 'W')
ttk.Style().theme_use('clam')
ttk.Style().configure("Treeview", background="#343434", foreground="silver", fieldbackground="#343434")


entry2.grid(row=0, column=0, padx= 5, pady=5, sticky = 'W')
myButton5.grid(row=0, column=0, padx=80, pady=5, sticky='E')
myLabel5.grid(row=0, column=1, padx= 0, pady=0, sticky = 'W')

myLabel.grid(row=0, column=0, padx= 10, pady=10)
myLabel2.grid(row=2, column=0, padx= 10, pady=10)
myLabel4.grid(row=3, column=0, padx= 10, pady=10)
myButton.grid(row=5, column=0, padx= 10, pady=10)
myButton6.grid(row=6, column=0, padx= 10, pady=10)

root.mainloop()

   
    
  
         