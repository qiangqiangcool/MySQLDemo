# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'database.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(object):
    def setupUi(self, database):
        database.setObjectName("database")
        database.resize(1500, 1000)
        self.gridLayout_2 = QtWidgets.QGridLayout(database)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.table = QtWidgets.QTableWidget(database)
        self.table.setMaximumSize(QtCore.QSize(300, 16777215))
        self.table.setRowCount(0)
        self.table.setColumnCount(1)
        self.table.setObjectName("table")
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setDefaultSectionSize(300)
        self.gridLayout_2.addWidget(self.table, 1, 0, 2, 1)
        self.data = QtWidgets.QTableWidget(database)
        self.data.setObjectName("data")
        self.data.setColumnCount(0)
        self.data.setRowCount(0)
        self.gridLayout_2.addWidget(self.data, 2, 1, 1, 3)
        self.executeBtn = QtWidgets.QPushButton(database)
        self.executeBtn.setObjectName("executeBtn")
        self.gridLayout_2.addWidget(self.executeBtn, 1, 2, 1, 1)
        self.sqlLine = QtWidgets.QLineEdit(database)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sqlLine.sizePolicy().hasHeightForWidth())
        self.sqlLine.setSizePolicy(sizePolicy)
        self.sqlLine.setObjectName("sqlLine")
        self.gridLayout_2.addWidget(self.sqlLine, 1, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(database)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.hostLine = QtWidgets.QLineEdit(self.groupBox)
        self.hostLine.setObjectName("hostLine")
        self.gridLayout.addWidget(self.hostLine, 0, 2, 1, 1)
        self.dbNameLine = QtWidgets.QLineEdit(self.groupBox)
        self.dbNameLine.setObjectName("dbNameLine")
        self.gridLayout.addWidget(self.dbNameLine, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 3, 1, 1)
        self.passwordLine = QtWidgets.QLineEdit(self.groupBox)
        self.passwordLine.setObjectName("passwordLine")
        self.gridLayout.addWidget(self.passwordLine, 2, 4, 1, 1)
        self.userLine = QtWidgets.QLineEdit(self.groupBox)
        self.userLine.setObjectName("userLine")
        self.gridLayout.addWidget(self.userLine, 2, 2, 1, 1)
        self.connectBtn = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectBtn.sizePolicy().hasHeightForWidth())
        self.connectBtn.setSizePolicy(sizePolicy)
        self.connectBtn.setObjectName("connectBtn")
        self.gridLayout.addWidget(self.connectBtn, 0, 5, 3, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 4)

        self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.hostLine.setPlaceholderText('Input Ip Address')
        self.dbNameLine.setPlaceholderText('Input DataBase Name')
        self.userLine.setPlaceholderText('Input Username')
        self.passwordLine.setPlaceholderText('Input Password')

        self.retranslateUi(database)
        QtCore.QMetaObject.connectSlotsByName(database)

    def retranslateUi(self, database):
        _translate = QtCore.QCoreApplication.translate
        database.setWindowTitle(_translate("database", "DataBase"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("database", "table in database"))
        self.executeBtn.setText(_translate("database", "execute"))
        self.groupBox.setTitle(_translate("database", "connect database"))
        self.hostLine.setText(_translate("database", "localhost"))
        self.label.setText(_translate("database", "database:"))
        self.label_2.setText(_translate("database", "ip:"))
        self.label_3.setText(_translate("database", "user:"))
        self.label_4.setText(_translate("database", "password:"))
        self.connectBtn.setText(_translate("database", "connect"))
