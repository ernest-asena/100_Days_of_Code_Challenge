import tkinter as tk

window = tk.Tk()
window.title('Miles to KM Converter')
window.minsize(height=200, width=200)
window.config(padx=100, pady=100)

# Entry Button
miles = tk.Entry(width=30, bd=3, bg='yellow', fg='red', highlightcolor='pink')
miles.grid(column=6, row=1)

# Miles Label
miles_label = tk.Label(text='Miles', font=("Arial", 12, "bold"), bg='pink', relief='raised')
miles_label.grid(column=7, row=1)

# is_equal_to label
is_equal_to = tk.Label(text='Is equal to ...', font=("Arial", 12, "bold"), relief='raised')
is_equal_to.grid(column=5, row=5)

# result label
result = tk.Label(text='1.609344', font=("Arial", 24, "bold"), relief='raised', fg='yellow', bg='grey')
result.grid(column=6, row=5)

# KM label
km_label = tk.Label(text='KM', font=("Arial", 12, "bold"), relief='raised')
km_label.grid(column=7, row=5)


def miles_to_km():
    mile = int(miles.get())
    km = round(mile * 1.609344, 2)
    result['text'] = km

    # print(km)


# Calculate Button
calculate = tk.Button(text='Convert', command=miles_to_km, font=("Arial", 24, "bold"))
calculate.grid(column=6, row=6)

window.mainloop()
