# from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QStatusBar, QPushButton
# from PySide6.QtGui import QAction, QIcon
# from PySide6.QtCore import QSize
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app #declare an app member
        self.setWindowTitle("Custom MainWindow")

        #Menubar and menus
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        #A bunch of other menu options just for the fun of it
        menu_bar.addMenu("Window")
        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")

        #Working with toolbars
        toolbar = QToolBar("my main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        #Add the quit action to the toolbar
        toolbar.addAction(quit_action)
        quit_action.triggered.connect(self.quit_app)

        action1 = QAction("Some Action", self)
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("start.png"), "Some other action", self)
        action2.setStatusTip("Status message for some other action")
        action2.triggered.connect("self.toolbar_button_click")
        toolbar.addAction(action2)

        toolbar.addSeparator()
        # toolbar.addWidget(QPushButton("Click here"))

        # Working with status bars
        self.setStatusBar(QStatusBar(self))
        button1 = QPushButton("BUTTON1")
        button1.clicked.connect(self.button1_clicked)
        button_about = QPushButton("About")
        button_about.clicked.connect(self.button_clicked_about)

        self.setCentralWidget(button_about)



    def button1_clicked(self):
        print("clicked on the button")

    #About
    def button_clicked_about(self):
        ret = QMessageBox.about(self,"Message Title",
                                        "Some about message")
        if ret == QMessageBox.Ok :
            print("User chose OK")
        else :
            print ("User chose Cancel")

    def quit_app(self):
        self.app.quit()

    def toolbar_button_click(self):
        self.statusBar().showMessage("Message from my app")
