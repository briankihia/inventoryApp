# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'code.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QComboBox, QItemDelegate
import psycopg2


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 454)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(150, 10, 421, 221))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.form = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.form.setContentsMargins(0, 0, 0, 0)
        self.form.setObjectName("form")
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.form.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.table = QtWidgets.QTableWidget(self.formLayoutWidget)
        self.table.setAlternatingRowColors(False)
        self.table.setRowCount(1)
        self.table.setColumnCount(4)
        self.table.setObjectName("table")
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        self.form.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.table)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

         # Create a QComboBox for the stock column
        self.stock_combo_box = QComboBox()
        self.stock_combo_box.addItems(["Books", "LightBulb", "Flowers", "Phones","laptop"])  # Add your desired items here

        # Set the QComboBox as the item delegate for the stock column
        self.table.setItemDelegateForColumn(0, MyComboBoxDelegate(self.stock_combo_box))


        self.pushButton.clicked.connect(self.submit_data)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "stock"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "quantity"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "buying_price"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "selling_price"))



    def submit_data(self):
        rows = self.table.rowCount()
        cols = self.table.columnCount()

        # Connect to PostgreSQL database
        conn = psycopg2.connect(
            dbname="inventory",
            user="postgres",
            password="briankihiakiama",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # Check if the table exists
        cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'invent')")
        table_exists = cur.fetchone()[0]

        # If the table doesn't exist, create it
        if not table_exists:
            cur.execute("""
                CREATE TABLE invent (
                    stock VARCHAR(255),
                    quantity INTEGER,
                    balance NUMERIC,
                    buying_price NUMERIC,
                    selling_price NUMERIC,
                    profit NUMERIC,
                    total_profit NUMERIC
                    )
            """)



        # Insert data into PostgreSQL database
        for row in range(rows):
            stock = self.table.item(row, 0).text()
            quantity = int(self.table.item(row, 1).text())
            buying_price = float(self.table.item(row, 2).text())
            selling_price = float(self.table.item(row, 3).text())

             # Calculate profit
            profit = selling_price - buying_price

            # calculating total profit
            total_profit = profit * quantity



            # Insert data into the database
        cur.execute("INSERT INTO invent (stock, quantity, buying_price, selling_price, profit, total_profit) VALUES (%s, %s, %s, %s, %s, %s)",
                    (stock, quantity, buying_price, selling_price, profit, total_profit))

        # Commit changes and close connection
        conn.commit()
        conn.close()

class MyComboBoxDelegate(QItemDelegate):
    def __init__(self, combo_box):
        super().__init__()
        self.combo_box = combo_box

    def createEditor(self, parent, option, index):
        return self.combo_box


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
