from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# the above are just starting things you type before anything

# now we define an application
# the sys.argv is to give a config setup for our q application to know what os it's running on and how to display the window since os running on has differences
def window():
    app = QApplication(sys.argv)
    # we create some kind of window that will show in our application
    # some people use QWidget but we use QMainWindow
    win = QMainWindow()
    # now we set the size of our window and the position of it on the screen
    # thus we call a method called Geometry and we give it 4 arguments
    # win.setGeometry(xposition, yposition, width, height)
    win.setGeometry(200, 200, 300, 300)
    # we set window title, what shows at top bar
    win.setWindowTitle("Tech with Brian")
    # now you put content in our window

    # to show/display our window we need to call win.show()
    win.show()
    # now we type a code that allows us to exit our window when we click x button
    sys.exit(app.exec_())

# if you want program to show up you need to run this code below
window()



