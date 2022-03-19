# Python has a lot of GUI frameworks, but Tkinter is the only framework that’s built into the Python standard
# library. Tkinter has several strengths. It’s cross-platform, so the same code works on Windows, macOS, and Linux.
# Visual elements are rendered using native operating system elements, so applications built with Tkinter look like
# they belong on the platform where they’re run.

import tkinter as tk

window = tk.Tk()
window.title('My first GUI Program')
window.minsize(width=500, height=300)

# Labels
label = tk.Label(text='Open', font=('Arial', 24))

label.pack()












window.mainloop()