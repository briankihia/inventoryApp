from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# the above are just starting things you type before anything

# we create a class which will mean that all those click methods and all that will have access to everything
# so we create a class MyWindow which will inherit from QMainWindow meaning that that class will be able to take all properties from qMainWindow and use them in myWindow and we can change and use them there

class MyWindow(QMainWindow):
    # first method we need to write is the init method
    # this is OOP
    # this init method will run whenever we create an instance of myWindow adn then we call what is known as the parent constructor of this myWindow and that is what the super line does

    def __init__(self):
        super(MyWindow, self).__init__()
        
        # here we bring the setGeometry and setWindow title that we had down there
        # we are referencing the window of this class so we use self.
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Tech with Brian")
        # we also call our below initUI here 
        self.initUI()

    # this some choose to omit
    # though this is here we put all the stuff that we want in our window
    def initUI(self):
        # so what goes in here is stuff like  label we got down there
        # label = QtWidgets.QLabel(win) but we will have to change the win
        # this is because , when we create an instance of my window, what we are really doing is creating an instance of QMainWindow
        # so just like we said down there win= QMainWindow(), thus rather than win we just have to add self inside the brackets and at the beginning ie. self.label =QyWidgets.QLabel(self)
        # the reason for adding self at the beginning is because we want to be able to access label and b1 anywhere throughout my object or class so that when we click a button I can actually change this label text from inside of that function or method since it's part of the class
        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label") 
        self.label.move(50,50)
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me")
        # we change the clicked in the bracket to self.clicked because we need to reference the clicked in the class not the one outside
        self.b1.clicked.connect(self.clicked)

    # the next thing is to define a method called clicked in our class
    def clicked(self):
        # this time in here we change the text that the label shows
        self.label.setText("you pressed the button ")





# this function will define what to happen when our button defined below is clicked
def clicked():
    print("clicked")

# now we define an application
# the sys.argv is to give a config setup for our q application to know what os it's running on and how to display the window since os running on has differences
def window():
    app = QApplication(sys.argv)
    # we create some kind of window that will show in our application
    # some people use QWidget but we use QMainWindow
    # win = QMainWindow()
    # here we will have to change win to be an instance of myWindow class
    win = MyWindow()
    # now we set the size of our window and the position of it on the screen
    # thus we call a method called Geometry and we give it 4 arguments
    # win.setGeometry(xposition, yposition, width, height)
    # win.setGeometry(200, 200, 300, 300)
    # # we set window title, what shows at top bar
    # win.setWindowTitle("Tech with Brian")
    # now you put content in our window

    # now we can add a label to our app and we add a parameter to show where we want our label, win means inside our window
    # label = QtWidgets.QLabel(win)
    # # now we add text
    # label.setText("my first label")
    # #now we move our label
    # label.move(50,50)

    # # adding a button is same as a label above
    # b1 = QtWidgets.QPushButton(win)
    # b1.setText("click me")
    # # upto here the button is available but does nothing on clicking
    # # thus what we need to do next is kind of match this button  click to an event
    # # to do that we first of all create a function that will trigger when that button is clicked
    # # we do it above the screen
    # # NB. Now to map this button to the function clicked.In the brackets we type the name of the function without the brackets
    # # the first clicked is an event
    # b1.clicked.connect(clicked)


    # to show/display our window we need to call win.show()
    win.show()
    # now we type a code that allows us to exit our window when we click x button
    sys.exit(app.exec_())

# if you want program to show up you need to run this code below
window()



