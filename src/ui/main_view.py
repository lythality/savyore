# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 666)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.vioWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.vioWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.vioWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.vioWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.vioWidget.setRowCount(0)
        self.vioWidget.setColumnCount(4)
        self.vioWidget.setObjectName("vioWidget")
        item = QtWidgets.QTableWidgetItem()
        self.vioWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.vioWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.vioWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.vioWidget.setHorizontalHeaderItem(3, item)
        self.vioWidget.horizontalHeader().setStretchLastSection(True)
        self.vioWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.vioWidget)
        self.codeWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.codeWidget.setFont(font)
        self.codeWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.codeWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.codeWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.codeWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.codeWidget.setShowGrid(False)
        self.codeWidget.setColumnCount(3)
        self.codeWidget.setObjectName("codeWidget")
        self.codeWidget.setRowCount(0)
        self.codeWidget.horizontalHeader().setVisible(False)
        self.codeWidget.horizontalHeader().setDefaultSectionSize(0)
        self.codeWidget.horizontalHeader().setMinimumSectionSize(0)
        self.codeWidget.horizontalHeader().setStretchLastSection(True)
        self.codeWidget.verticalHeader().setVisible(False)
        self.codeWidget.verticalHeader().setDefaultSectionSize(0)
        self.codeWidget.verticalHeader().setHighlightSections(False)
        self.codeWidget.verticalHeader().setMinimumSectionSize(0)
        self.verticalLayout.addWidget(self.codeWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.button_clicked) # type: ignore
        self.vioWidget.cellDoubleClicked['int','int'].connect(MainWindow.show_code) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        item = self.vioWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Rule"))
        item = self.vioWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "File"))
        item = self.vioWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Loc."))
        item = self.vioWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Comment"))
