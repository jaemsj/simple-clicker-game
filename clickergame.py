import tkinter as tk
import random 
import time 
totalMoney = 0
addOnMainClick = 1
upgrade1Cost = 25
totalMoneyLabelX = 495
totalMoneyLabelSize = 50
#main window creation
root = tk.Tk()
root.title("clicker game")
root.geometry("1000x800")




#setup

def onClickMainObject():
    global totalMoney, addOnMainClick
    totalMoney = addOnMainClick + totalMoney
    print(totalMoney)
    moneyLabel.config(text= totalMoney, font=("arial", totalMoneyLabelSize, "bold"))
def onClickUpgrade1():
    global totalMoney, upgrade1Cost, addOnMainClick
    if totalMoney >= upgrade1Cost:
        totalMoney = totalMoney - upgrade1Cost
        upgrade1Cost = upgrade1Cost * 2
        addOnMainClick = addOnMainClick + 1
        moneyLabel.config(text= totalMoney, font=("arial", totalMoneyLabelSize, "bold"))
        upgrade1.config(text= "upgrade 1, " + str(upgrade1Cost))
    






#stats




#buttons
mainObject = tk.Button(root, text= "click here", command=onClickMainObject)
mainObject.place(x=10, y=50)
upgrade1 = tk.Button(root, text= "upgrade 1, $" + str(upgrade1Cost) , command=onClickUpgrade1)
upgrade1.place(x=700, y=50)



#text/labels
moneyLabel = tk.Label(root, text="0")
moneyLabel.place(x=totalMoneyLabelX, y=0)
moneyLabel.config(font=("arial", totalMoneyLabelSize, "bold"), fg="blue")







#runs loop, keep at bottom
root.mainloop()