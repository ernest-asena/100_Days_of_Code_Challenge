import tkinter as tk

window = tk.Tk()
window.title('My first GUI Program')
window.minsize(width=500, height=300)

# Labels
label = tk.Label(text='Welcome', font=('Arial', 24))
# You can edit the text as follows;
# label['text'] = 'New text'
# OR
# label.config(text='New Text')
label.pack()


def button_clicked():
    # label['text'] = 'Button Got Clicked'
    label['text'] = input.get()


# Button
button_start = tk.Button(text='Start', command=button_clicked)
button_start.pack()

# Entry
input = tk.Entry(width=5)
print(input.get())
input.pack()

window.mainloop()
