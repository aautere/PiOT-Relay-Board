MIT License

Copyright (c) 2016 ModMyPi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

#Library imports

from tkinter import *
from tkinter import StringVar
import time
from functools import partial

class App:
# Class to manage control of the PIOT1005
# ---------------------------------------


    def __init__(self, master):
    # Init function for class
    # -----------------------
    
        frame = Frame(master)
        frame.pack()
        

        #arrays of IO states and GPIO pins (we always use J pin number convention in this program)
        self.IOState=[0,0,0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.jPin   =[3,5,7,8,10,11,12,13,15,16,18,19,21,22,23,24,26,29,31,32,33,35,36,37,38,40]
        self.AllState = 0

        
        # Create and position each of the buttons 
        self.ChannelButton3 = Button(frame, text="3",bg = "red", activebackground="red", height=1, width=1)
        self.ChannelButton3.grid(row=1,column=2); 
        self.ChannelButton5 = Button(frame, text="5",bg = "red", activebackground="red",height=1, width=1)
        self.ChannelButton5.grid(row=2,column=2); 
        self.ChannelButton7 = Button(frame, text="7",bg = "red", activebackground="red",height=1, width=1)
        self.ChannelButton7.grid(row=3,column=2); 
        self.ChannelButton8 = Button(frame, text="8",bg = "red", activebackground="red",height=1, width=1)
        self.ChannelButton8.grid(row=3,column=3);
        self.ChannelButton10 = Button(frame, text="10",bg = "red",activebackground="red",height=1, width=1)
        self.ChannelButton10.grid(row=4,column=3); 
        self.ChannelButton11 = Button(frame, text="11",bg = "red",activebackground="red",height=1, width=1)
        self.ChannelButton11.grid(row=5,column=2); 
        self.ChannelButton12 = Button(frame, text="12",bg = "red",activebackground="red",height=1, width=1)
        self.ChannelButton12.grid(row=5,column=3); 
        self.ChannelButton13 = Button(frame, text="13",bg = "red",activebackground="red",height=1, width=1)
        self.ChannelButton13.grid(row=6,column=2); 
        self.ChannelButton15 = Button(frame, text="15",bg = "red",activebackground="red",height=1, width=1)
        self.ChannelButton15.grid(row=7,column=2); 
        self.ChannelButton16 = Button(frame, text="16",bg = "red",activebackground="red",height=1, width=1)
        self.ChannelButton16.grid(row=7,column=3); 
        self.ChannelButton18 = Button(frame, text="18",bg = "red",activebackground="red",height=1, width=1)
        self.ChannelButton18.grid(row=8,column=3); 
        self.ChannelButton19 = Button(frame, text="19",bg = "red",activebackground="red",height=1, width=1)
        self.ChannelButton19.grid(row=9,column=2); 
        self.ChannelButton21 = Button(frame, text="21",bg = "red",activebackground="red",height=1, width=1)
        self.ChannelButton21.grid(row=10,column=2); 
        self.ChannelButton22 = Button(frame, text="22",bg = "red",activebackground="red",height=1, width=1)
        self.ChannelButton22.grid(row=10,column=3); 
        self.ChannelButton23 = Button(frame, text="23",bg = "red",activebackground="red",height=1, width=1)
        self.ChannelButton23.grid(row=11,column=2); 
        self.ChannelButton24 = Button(frame, text="24",bg = "red",activebackground="red",height=1, width=1)
        self.ChannelButton24.grid(row=11,column=3); 
        self.ChannelButton26 = Button(frame, text="26",bg = "red",activebackground="red",height=1, width=1)
        self.ChannelButton26.grid(row=12,column=3); 
        self.ChannelButton29 = Button(frame, text="29",bg = "red",activebackground="red",height=1, width=1)
        self.ChannelButton29.grid(row=14,column=2); 
        self.ChannelButton31 = Button(frame, text="31",bg = "red",activebackground="red",height=1, width=1)
        self.ChannelButton31.grid(row=15,column=2); 
        self.ChannelButton32 = Button(frame, text="32",bg = "red",activebackground="red",height=1, width=1)
        self.ChannelButton32.grid(row=15,column=3); 
        self.ChannelButton33 = Button(frame, text="33",bg = "red",activebackground="red",height=1, width=1)
        self.ChannelButton33.grid(row=16,column=2); 
        self.ChannelButton35 = Button(frame, text="35",bg = "red",activebackground="red",height=1, width=1)
        self.ChannelButton35.grid(row=17,column=2); 
        self.ChannelButton36 = Button(frame, text="36",bg = "red",activebackground="red",height=1, width=1)
        self.ChannelButton36.grid(row=17,column=3); 
        self.ChannelButton37 = Button(frame, text="37",bg = "red",activebackground="red",height=1, width=1)
        self.ChannelButton37.grid(row=18,column=2); 
        self.ChannelButton38 = Button(frame, text="38",bg = "red",activebackground="red",height=1, width=1)
        self.ChannelButton38.grid(row=18,column=3); 
        self.ChannelButton40 = Button(frame, text="40",bg = "red",activebackground="red",height=1, width=1)
        self.ChannelButton40.grid(row=19,column=3);

        # create on and off actions for each button
        action_toggle3 = partial(self.ToggleOnOff, 0, self.ChannelButton3)
        action_toggle5 = partial(self.ToggleOnOff, 1, self.ChannelButton5)
        action_toggle7 = partial(self.ToggleOnOff, 2, self.ChannelButton7)
        action_toggle8 = partial(self.ToggleOnOff, 3, self.ChannelButton8)
        action_toggle10= partial(self.ToggleOnOff, 4, self.ChannelButton10)
        action_toggle11= partial(self.ToggleOnOff, 5, self.ChannelButton11)
        action_toggle12= partial(self.ToggleOnOff, 6, self.ChannelButton12)
        action_toggle13= partial(self.ToggleOnOff, 7, self.ChannelButton13)
        action_toggle15= partial(self.ToggleOnOff, 8, self.ChannelButton15)
        action_toggle16= partial(self.ToggleOnOff, 9, self.ChannelButton16)
        action_toggle18= partial(self.ToggleOnOff, 10, self.ChannelButton18)
        action_toggle19= partial(self.ToggleOnOff, 11, self.ChannelButton19)
        action_toggle21= partial(self.ToggleOnOff, 12, self.ChannelButton21)
        action_toggle22= partial(self.ToggleOnOff, 13, self.ChannelButton22)
        action_toggle23= partial(self.ToggleOnOff, 14, self.ChannelButton23)
        action_toggle24= partial(self.ToggleOnOff, 15, self.ChannelButton24)
        action_toggle26= partial(self.ToggleOnOff, 16, self.ChannelButton26)
        action_toggle29= partial(self.ToggleOnOff, 17, self.ChannelButton29)
        action_toggle31= partial(self.ToggleOnOff, 18, self.ChannelButton31)
        action_toggle32= partial(self.ToggleOnOff, 19, self.ChannelButton32)
        action_toggle33= partial(self.ToggleOnOff, 20, self.ChannelButton33)
        action_toggle35= partial(self.ToggleOnOff, 21, self.ChannelButton35)
        action_toggle36= partial(self.ToggleOnOff, 22, self.ChannelButton36)
        action_toggle37= partial(self.ToggleOnOff, 23, self.ChannelButton37)
        action_toggle38= partial(self.ToggleOnOff, 24, self.ChannelButton38)
        action_toggle40= partial(self.ToggleOnOff, 25, self.ChannelButton40)

        #associate the actions with the button
        self.ChannelButton3.config(command=action_toggle3)
        self.ChannelButton5.config(command=action_toggle5)
        self.ChannelButton7.config(command=action_toggle7)
        self.ChannelButton8.config(command=action_toggle8)
        self.ChannelButton10.config(command=action_toggle10)
        self.ChannelButton11.config(command=action_toggle11)
        self.ChannelButton12.config(command=action_toggle12)
        self.ChannelButton13.config(command=action_toggle13)
        self.ChannelButton15.config(command=action_toggle15)
        self.ChannelButton16.config(command=action_toggle16)
        self.ChannelButton18.config(command=action_toggle18)
        self.ChannelButton19.config(command=action_toggle19)
        self.ChannelButton21.config(command=action_toggle21)
        self.ChannelButton22.config(command=action_toggle22)
        self.ChannelButton23.config(command=action_toggle23)
        self.ChannelButton24.config(command=action_toggle24)
        self.ChannelButton26.config(command=action_toggle26)
        self.ChannelButton29.config(command=action_toggle29)
        self.ChannelButton31.config(command=action_toggle31)
        self.ChannelButton32.config(command=action_toggle32)
        self.ChannelButton33.config(command=action_toggle33)
        self.ChannelButton35.config(command=action_toggle35)
        self.ChannelButton36.config(command=action_toggle36)
        self.ChannelButton37.config(command=action_toggle37)
        self.ChannelButton38.config(command=action_toggle38)
        self.ChannelButton40.config(command=action_toggle40)

        # Create the GPIO labels alongside the buttons
        l3 = Label(frame, text = "GPIO02", height=1, width=6);
        l3.grid (row=1, column=0)
        l5 = Label(frame, text = "GPIO03", height=1, width=6);
        l5.grid (row=2, column=0)
        l7 = Label(frame, text = "GPIO04", height=1, width=6);
        l7.grid (row=3, column=0)
        l8 = Label(frame, text = "GPIO14", height=1, width=6);
        l8.grid (row=3, column=4)
        l10 = Label(frame, text = "GPIO15", height=1, width=6);
        l10.grid (row=4, column=4)
        l11 = Label(frame, text = "GPIO17", height=1, width=6);
        l11.grid (row=5, column=0)
        l12 = Label(frame, text = "GPIO18", height=1, width=6);
        l12.grid (row=5, column=4)
        l13 = Label(frame, text = "GPIO27", height=1, width=6);
        l13.grid (row=6, column=0)
        l15 = Label(frame, text = "GPIO22", height=1, width=6);
        l15.grid (row=7, column=0)
        l16 = Label(frame, text = "GPIO23", height=1, width=6);
        l16.grid (row=7, column=4)
        l18 = Label(frame, text = "GPIO24", height=1, width=6);
        l18.grid (row=8, column=4)
        l19 = Label(frame, text = "GPIO10", height=1, width=6);
        l19.grid (row=9, column=0)
        l21 = Label(frame, text = "GPIO09", height=1, width=6);
        l21.grid (row=10, column=0)
        l22 = Label(frame, text = "GPIO25", height=1, width=6);
        l22.grid (row=10, column=4)
        l23 = Label(frame, text = "GPIO11", height=1, width=6);
        l23.grid (row=11, column=0)
        l24 = Label(frame, text = "GPIO08", height=1, width=6);
        l24.grid (row=11, column=4)
        l26 = Label(frame, text = "GPIO07", height=1, width=6);
        l26.grid (row=12, column=4)
        l29 = Label(frame, text = "GPIO05", height=1, width=6);
        l29.grid (row=14, column=0)
        l31 = Label(frame, text = "GPIO06", height=1, width=6);
        l31.grid (row=15, column=0)
        l32 = Label(frame, text = "GPIO12", height=1, width=6);
        l32.grid (row=15, column=4)
        l33 = Label(frame, text = "GPIO13", height=1, width=6);
        l33.grid (row=16, column=0)
        l35 = Label(frame, text = "GPIO19", height=1, width=6);
        l35.grid (row=17, column=0)
        l36 = Label(frame, text = "GPIO16", height=1, width=6);
        l36.grid (row=17, column=4)
        l37 = Label(frame, text = "GPIO26", height=1, width=6);
        l37.grid (row=18, column=0)
        l38 = Label(frame, text = "GPIO20", height=1, width=6);
        l38.grid (row=18, column=4)
        l40 = Label(frame, text = "GPIO21", height=1, width=6);
        l40.grid (row=19, column=4)

        # Create the Toggle All button
        ToggleAllButton = Button(frame, text="Toggle All",  height=1, width=25, command =self.ToggleAll)
        ToggleAllButton.grid(row=20, column=0,columnspan=5)

        # Create the connect button
        ConnectButton = Button(frame, text="Connect/Disconnect",  height=1, width=25, command =self.Connect)
        ConnectButton.grid(row=21, column=0, columnspan=5)

    
    def ToggleAll(self):
    # toggle all i/os on or off
    # -------------------------
    
        if self.AllState==1:
            self.AllState = 0
            bgclr="red"
            fgclr="black"
        else:
            self.AllState = 1
            bgclr="green"
            fgclr="white"

        # update the button colours according to the IO state
        self.ChannelButton3.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton5.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton7.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton8.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton10.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton11.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton12.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton13.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton15.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton16.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton18.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton19.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton21.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton22.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton23.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton24.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton26.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton29.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton31.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton32.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton33.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton35.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton36.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton37.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton38.config(fg = fgclr , bg = bgclr, activebackground=bgclr)
        self.ChannelButton40.config(fg = fgclr , bg = bgclr, activebackground=bgclr)


        # put the new i/o states in the array of i/o states
        for idx in range(26):    
            GPIO.output(self.jPin[idx] ,self.AllState)
            self.IOState[idx] = self.AllState

    
    def ToggleOnOff(self, idx, button):
        # Toggle an i/o on or off
        # -----------------------
        if (self.IOState[idx] == 0):
            self.IOState[idx] = 1
            button.config(bg="green", fg="white",activebackground="green")
        else:
            self.IOState[idx] = 0
            button.config(bg="red", fg="black",activebackground="red")
        GPIO.output(self.jPin[idx] ,self.IOState[idx])
        
    
    def Connect(self):
        # Send connect/disconnect pulse train to J3
        # -----------------------------------------
        
        for idx in range(4):
            GPIO.output(3,1)
            time.sleep(0.05)
            GPIO.output(3,0)
            time.sleep(0.05)

    
    def SetAllOff(self):
        # Drive all outputs to the 'off' state
        # ------------------------------------
        
        for idx in range(26):    
            GPIO.output(self.jPin[idx] ,0)
            self.IOState[idx] = 0

# Main program
# ------------

import RPi.GPIO as GPIO

#Turn off GPIO warnings
GPIO.setwarnings(False)

#Set the GPIO numbering convention to be header pin numbers
GPIO.setmode(GPIO.BOARD)

#Configure each GPIO pin as an output
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)



#Create our window using Tkinter
root = Tk()
root.title('PiOT 5')
root.resizable(width=FALSE, height=FALSE)

app = App(root)

#Turn all the GPIO off to start with
app.SetAllOff()

#Main loop - responds to dialog events
root.mainloop()

#we exit the main loop if user has closed the window
#reset the GPIO and end the program
GPIO.cleanup()
