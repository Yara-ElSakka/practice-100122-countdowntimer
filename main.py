# practice exercise done by yara
# countdown timer homework !
# let's do this ..
# 09.01.22
# HW: 16.01.22

import time
from tkinter import *
from requests import *

# todo : import messagebox to display a message at the end of the countdown
# yara: done as below. we have already imported everything from tkinter anyway :)
from tkinter import messagebox

programWindow = Tk()

# create 3 variables for time
# hour
# minute
# second

hour = StringVar()
minute = StringVar()
second = StringVar()

# set the three variables to 0
# hour.set("00")
# minute
# second

hour.set("00")
minute.set("00")
second.set("00")

# Configure the window to take the following attributes
# title
programWindow.title("yaras countdown timer made for the whole globe")
# size
programWindow.geometry("500x600")
# background color
programWindow.config(bg="#D77FA1")
# font
titleLabel = Label(text="yaras countdown timer made for the whole globe", font="times 12 bold", bg="#BAFFB4")
titleLabel.pack(pady=20)

hoursInput = Entry(textvariable=hour)
# pack the input box
hoursInput.pack()

minuteInput = Entry(textvariable=minute)
# pack the input box
minuteInput.pack()

secondInput = Entry(textvariable=second)
# pack the input box
secondInput.pack()


# this function is linked in the begin button (command).
def submitTime():
    # store time given by user in a var

    try:
        # TODO : multipy the hours by 3600 and minutes by 60
        # Yara: we convert user input time (h,m,s) to total number of seconds:
        user_input = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())

    except:

        print("Please use Numbers only")

    # TODO 1 : create a while loop to count down only if user_input is greater than 0
    # 2: code while loop here

    while user_input > 0:
        print(f"user_input={user_input}")
        # todo 3 # create a variable for minutes that will store divmod(user_input, 60)
        # yara: divmod(a,b) = a divided by b , gives(answer , reminder)
        # user input divided by 60 will give mints and reminder is seconds.
        # the answer is the min_s and reminder is second_s

        minute_s, second_s = divmod(user_input, 60)

        print(f"minute_s={minute_s}", f"second_s={second_s}")

        # todo 4 # create a variable for seconds that will store divmod(user_input, 60)

        # Yara: already done above.

        # todo 5 # create a if statement to check if user_input is greater than 0 and if it is then create a variable for hours that will store divmod(minutes, 60)
        # # if:
        # Yara: to start with, we set the value of hour_s to zero.
        hour_s = 0
        if minute_s > 60:
            hour_s, minute_s = divmod(minute_s, 60)
            print(f"hour_s={hour_s}", f"minute_s={minute_s}")
        # # # variable
        #
        # exit if statement
        #
        # todo 6 # using set() and format() to store the user given values with two decimal places
        # hour variable from beginning of the program.set("{0:2d}".format(new hour variable from inside the while loop))
        hour.set("{0:2d}".format(hour_s))
        # minute variable from beginning of the program.set("{0:2d}".format(new minute variable from inside the while loop))
        minute.set("{0:2d}".format(minute_s))
        # second variable from beginning of the program.set("{0:2d}".format(new second variable from inside the while loop))
        second.set("{0:2d}".format(second_s))

        # todo 7 update the program window with method update()
        programWindow.update()
        # Yara: to control the speed of the counter, we need to use 1 sec counter inside the while loop:
        time.sleep(1)

        # todo 8 when the user_input is 0 then display a messagebox with a creative message
        if user_input == 0:
            print("The countdown timer is up ! Thanks for using Yara's App")

        # todo 9 after every one sec the value of user_input will be decremented by one
        user_input -= 1


# my buttons (widgets): reset and close buttons:
beginCountDown = Button(text="begin", command=submitTime)
# pack the button and set the text to "Begin Countdown"
beginCountDown.pack(padx=20, side=RIGHT)

# create a button that will reset the timer by deleting whats inside the input fields
# and set the text to "Reset"

def resetButtonFunc():
    hour.set("00")
    minute.set("00")
    second.set("00")

# my buttons (widgets): reset and close buttons:
resetButton = Button(text="reset", command=resetButtonFunc)
resetButton.pack(padx=20, side=LEFT)

closeButton = Button(text="close", command=programWindow.destroy)
closeButton.pack(pady=20, side=BOTTOM)

mainloop()
# end of code