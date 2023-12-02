from tkinter import * 
from tkinter import messagebox
  
root = Tk()
root.geometry("400x200")
  
w = Label(root, text ='Testujemy na zajęciach', font = "40") 
w.pack()
  
messagebox.showinfo("showinfo", "Information")
  
messagebox.showwarning("showwarning", "Warning")
  
messagebox.showerror("showerror", "Error")
  
messagebox.askquestion("askquestion", "Are you sure?")
  
messagebox.askokcancel("askokcancel", "Want to continue?")
  
messagebox.askyesno("askyesno", "Find the value?")
  
  
messagebox.askretrycancel("askretrycancel", "Try again?")  
  
root.mainloop()
