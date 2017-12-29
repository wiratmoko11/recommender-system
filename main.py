from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import view
import os
import numpy as np
import pandas as pd

class mainApp(QtWidgets.QMainWindow, view.Ui_bgDialog):
	def __init__(self, parent=None):
		super(mainApp, self).__init__(parent)
		self.setupUi(self)

		self.openFile()
		self.generateKolom()
		self.data = ""
		# Data Untuk Generate Kolom
		self.dataID = []
		self.dataMovieID = ""
		# Data Untuk Generate Baris
		self.dataUserID=""

	def generateKolom(self):
		self.table_data.setColumnCount(len(self.dataID))
		for i in range(len(self.dataID)):
			self.table_data.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(str(self.dataID[i])))

	def generateRating(self,dataUserID):
		self.table_data.setRowCount(len(dataUserID))
		for i in range(0,len(dataUserID)):
			for j in range(0,i):
				self.table_data.setItem(i,j,QtWidgets.QTableWidgetItem(j))

	def openFile(self):
		# Open File
		self.data = pd.read_csv("movie-lens.csv")
		# getData MovieID
		self.dataMovieID = self.data.loc[:,('movieId')].values
		self.dataMovieID.sort()
		rmDuplicate = set(self.dataMovieID)
		self.dataID = list(rmDuplicate)
		self.dataID.sort()
		# getData UserID
		self.dataUserID = self.data.loc[:,('userId')].values
		self.dataUserID.sort()
		barisDup = set(self.dataUserID)
		userListID = list(barisDup)
		userListID.sort()
		print(userListID)
		# Func Generate Kolom
		self.generateKolom()
		self.generateRating(userListID)
		
def main():
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    form = mainApp()                 # We set the form to be our ExampleApp (design)
    form.show()                      # Show the form
    app.exec_()

if __name__ == '__main__':
    main()
