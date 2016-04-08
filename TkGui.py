import tkinter as tk
from PIL import Image,ImageTk

root = tk.Tk()
root.wm_title("Seminar")
root.config(background = "#FFFFFF")

display = tk.Frame(root,width=600,height=600)
display.grid(row=0, column=1, padx=0, pady=0,sticky=tk.N+tk.S)

goalFrame=tk.Frame(display,width=200,height=200)
goalFrame.grid(row=0,column=1,padx=0,pady=0)

bestFrame=tk.Frame(display,width=200,height=200)
bestFrame.grid(row=1,column=0,padx=0,pady=0)

secondBestFrame=tk.Frame(display,width=200,height=200)
secondBestFrame.grid(row=1,column=1,padx=0,pady=0)

thirdBestFrame=tk.Frame(display,width=200,height=200)
thirdBestFrame.grid(row=1,column=2,padx=0,pady=0)

goalText = tk.Label(goalFrame,text="Goal Image",font=("Serif",10))
BestText = tk.Label(bestFrame,text="Current Best: .0157",font=("Serif",10))
secondBestText = tk.Label(secondBestFrame,text="Current Second: .0255",font=("Serif",10))
thirdBestText = tk.Label(thirdBestFrame,text="Current Third: .0357",font=("Serif",10))
generationText = tk.Label(display,text="Generations: 300",font=("Serif",10))

generationText.grid(row=2,column=1)

goalIm = Image.open('test500.png')
resizedGoal = goalIm.resize((200,200),Image.ANTIALIAS)
goal = ImageTk.PhotoImage(resizedGoal)
goalImage = tk.Label(goalFrame,image=goal,text="Goal Image")
goalImage.grid(row=1,column=1,padx=0,pady=0)
goalText.grid(row=0,column=1,padx=0,pady=0)

bestIm = Image.open('test655.png')
resizedBest = bestIm.resize((200,200),Image.ANTIALIAS)
best = ImageTk.PhotoImage(resizedBest)
bestImage = tk.Label(bestFrame,image=best, text="Best so far")
bestImage.grid(row=1,column=1,padx=0,pady=0)
BestText.grid(row=0,column=1,padx=0,pady=0)

secondBestIm = Image.open('test535.png')
resizedBest = secondBestIm.resize((200,200),Image.ANTIALIAS)
secondBest = ImageTk.PhotoImage(resizedBest)
bestImage = tk.Label(secondBestFrame,image=secondBest, text="Best so far")
bestImage.grid(row=1,column=1,padx=0,pady=0)
secondBestText.grid(row=0,column=1,padx=0,pady=0)

thirdBestIm = Image.open('test518.png')
resizedBest = thirdBestIm.resize((200,200),Image.ANTIALIAS)
thirdBest = ImageTk.PhotoImage(resizedBest)
bestImage = tk.Label(thirdBestFrame,image=thirdBest, text="Best so far")
bestImage.grid(row=1,column=1,padx=0,pady=0)
thirdBestText.grid(row=0,column=1,padx=0,pady=0)

root.mainloop()