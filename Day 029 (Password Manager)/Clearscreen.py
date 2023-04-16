import os
import time


# print('Flask URL Paths and the Flask Debugger.py')
# os.system('clear')

def clear():
    os.system("cls" if os.name == "nt" else "clear")


for i in range(10):
    print(i)
    time.sleep(1)
    clear()
