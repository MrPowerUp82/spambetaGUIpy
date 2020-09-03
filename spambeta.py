from pynput.keyboard import Key, Controller
from pynput.keyboard import Listener
from appJar import gui
from time import sleep
def press(button):
    if button == "Submit":
        msg=str(app.getEntry("Msg"))
        n=int(app.getEntry("Nvezes"))
        t=int(app.getEntry("tempo para iniciar(s)"))
        keyboard=Controller()
        i=0
        sleep(t)
        while i < n:
            for l in msg:
                keyboard.press(l)
                keyboard.release(l)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            i+=1
        #app.stop()
        #exit()
    else:
        app.stop()
        exit()

app=gui("Spam Bot", "320x320")
app.setBg("black")
app.setFg("red")
app.setFont(14)
app.addLabel("Spam bot")
app.addLabelEntry("Msg")
app.addLabelEntry("tempo para iniciar(s)")
app.addLabelEntry("Nvezes")
app.addLabel("Criador", text="by MrPowerUp",)
app.addButtons(["Submit", "Cancel"], press)
app.go()
