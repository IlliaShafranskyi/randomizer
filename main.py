from tkinter import *
from logic import *

root = Tk()
root.title("Random password")
root.geometry("600x300")
root.resizable(width=False, height=False)
root.configure(background="black")

main_label = Label(text="Randomizer", fg="yellow", bg="black")
main_label.pack()
main_label.place(x=190, y=20)
main_label.config(font=("Arial", 30))


length_pass_label = Label(text="Length of desired password:", fg="yellow", bg="black")
length_pass_label.pack()
length_pass_label.place(x=20, y=100)
length_pass_label.config(font=("Arial", 20))

length_entry_form = Entry(bg="yellow", fg="black")
length_entry_form.pack()
length_entry_form.place(x=380, y=107)

pass_label = Label(text="Password: ", fg="yellow", bg="black")
pass_label.pack()
pass_label.place(x=20, y=180)
pass_label.config(font=("Arial", 20))

result_form = Entry(bg="yellow", fg="black")
result_form.pack()
result_form.place(x=170, y=187)


get_the_pass = Button(text="Get the password", bg="yellow", fg="black")
get_the_pass.pack()
get_the_pass.place(x=230, y=240)



#logic
def get_the_password(event):
    result_form.delete(0, END)
    result = random_pass(int(length_entry_form.get()))
    result_form.insert(0, result)
    

get_the_pass.bind('<Button-1>', get_the_password)
root.mainloop()
