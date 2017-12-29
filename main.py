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
		self.datatempMovieID = []
		self.dataMovieID = ""
		# Data Untuk Generate Baris
		self.dataUserID=""
		self.datatempUserID = []
		# data

	def generateKolom(self):
		self.table_data.setColumnCount(len(self.datatempMovieID))
		for i in range(len(self.datatempMovieID)):
			self.table_data.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(str(self.datatempMovieID[i])))

	def generateBaris(self,dataUserID):
		self.table_data.setRowCount(len(dataUserID))
		for i in range(0,len(dataUserID)):
			for j in range(0,i):
				self.table_data.setItem(i,j,QtWidgets.QTableWidgetItem(j))

	def generateRating(self,dataUserID):
		userID =  self.data.loc[:,('userId')].values
		movieID = self.data.loc[:,('movieId')].values
		ratingID = self.data.loc[:,('rating')].values
		
		for x in range(0,len(userID)):
			indexMovieID = self.datatempMovieID.index(movieID[x])
			indexUserID = self.datatempUserID.index(userID[x])
			self.table_data.setItem(indexUserID,indexMovieID,QtWidgets.QTableWidgetItem(str(ratingID[x])))

		# for i in range(0,len(dataUserID)):
		# 	for j in range(0,len(self.datatempMovieID)):
		# 		self.table_data.setItem(i,j,QtWidgets.QTableWidgetItem(str(6)))

	def openFile(self):
		# Open File
		self.data = pd.read_csv("movie-lens.csv")
		# getData MovieID
		self.dataMovieID = self.data.loc[:,('movieId')].values
		self.dataMovieID.sort()
		rmDuplicate = set(self.dataMovieID)
		self.datatempMovieID = list(rmDuplicate)
		self.datatempMovieID.sort()
		# getData UserID
		self.dataUserID = self.data.loc[:,('userId')].values
		self.dataUserID.sort()
		barisDup = set(self.dataUserID)
		self.datatempUserID = list(barisDup)
		self.datatempUserID.sort()
		# Func Generate Kolom
		self.generateKolom()
		self.generateBaris(self.datatempUserID)
		self.generateRating(self.datatempUserID)
		
def main():
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    form = mainApp()                 # We set the form to be our ExampleApp (design)
    form.show()                      # Show the form
    app.exec_()

if __name__ == '__main__':
    main()
