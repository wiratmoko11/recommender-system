# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example_data.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bgDialog(object):
    def setupUi(self, bgDialog):
        bgDialog.setObjectName("bgDialog")
        bgDialog.resize(560, 390)
        self.table_data = QtWidgets.QTableWidget(bgDialog)
        self.table_data.setGeometry(QtCore.QRect(30, 30, 481, 291))
        self.table_data.setObjectName("table_data")
        self.table_data.setColumnCount(0)
        self.table_data.setRowCount(0)

        self.retranslateUi(bgDialog)
        QtCore.QMetaObject.connectSlotsByName(bgDialog)

    def retranslateUi(self, bgDialog):
        _translate = QtCore.QCoreApplication.translate
        bgDialog.setWindowTitle(_translate("bgDialog", "System Recommender"))

