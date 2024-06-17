from tracking_numbers import get_tracking_number
import tkinter as tk
import webbrowser
import time

def getInput():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT) 

    track_num = get_tracking_number(str(INPUT))  

    print(track_num)

    if track_num is None:
        l2 = tk.Label(window, text='Sorry, Tracking Number is Invalid. Input a new tracking number.')
        l2.config(font=("Courier", 14))
        l2.pack()
        window.after(5000, l2.destroy)  # Waits 5 secs then destroys l2
    else:
        print(track_num.tracking_url)
        webbrowser.open(track_num.tracking_url)



   

#TKINTER SETUP
window = tk.Tk()

window.geometry("300x300")
window.title("Package Tracker")

#Top Label and Box
l = tk.Label(window, text = 'Enter Tracking Number:')
l.config(font =("Courier", 14))
inputtxt = tk.Text(window, height = 10,
                width = 25)

#Enter Button
enter = tk.Button(window,
                 text ="Get Tracking",
                 command = lambda:getInput())

#Exit button.
b2 =tk.Button(window, text = "Exit",
            command = window.destroy)

l.pack()
inputtxt.pack()
enter.pack()
b2.pack()


window.mainloop()

#1ZA6D4270406843035