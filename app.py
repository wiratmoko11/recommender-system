import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.widget = Widget(self)
        _widget = QWidget()
        _layout = QVBoxLayout(_widget)
        _layout.addWidget(self.widget)
        self.title = 'Collaborative Filtering'
        self.left = 10
        self.top = 30
        self.width = 640
        self.height = 480
        self.initUI()
        self.setCentralWidget(_widget)
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
        

class Widget(QWidget):
    def __init__(self, parent):
        super(Widget, self).__init__(parent)
        self.__widget()
        self.__layout()

    def __widget(self):
        self.datasetLabel = QLabel('Datasets')
        self.datasetFileLabel = QLabel('Dataset Belum Dipilih')
        self.pilihUserLabel = QLabel('Pilih User')
    
        self.datasetAddButton = QPushButton('Load Datasets', self)
        self.rekomendasiButton = QPushButton('Prediksi Rekomendasi')
        self.datasetAddButton.clicked.connect(self.loadDatasets)

        self.tableDataset = QTableWidget()
        self.tableDataset.setRowCount(4)
        self.tableDataset.setColumnCount(2)
        self.tableDataset.setHorizontalHeaderLabels(('Item 1', 'Item 2'))
        self.tableDataset.setVerticalHeaderLabels(('User 1', 'User 2', 'User 3', 'User 4'))

        self.tableDataset.setItem(0,0, QTableWidgetItem("2"))
        self.tableDataset.setItem(0,1, QTableWidgetItem("4"))
        self.tableDataset.setItem(1,0, QTableWidgetItem("1"))
        self.tableDataset.setItem(1,1, QTableWidgetItem("3"))
        self.tableDataset.setItem(2,0, QTableWidgetItem("3"))
        self.tableDataset.setItem(2,1, QTableWidgetItem("3"))
        self.tableDataset.setItem(3,0, QTableWidgetItem("0"))
        self.tableDataset.setItem(3,1, QTableWidgetItem("0"))
        self.tableDataset.move(0, 0)
        
        
    def __layout(self):
        vbox = QVBoxLayout()

        hbox = QHBoxLayout()
        hbox.addWidget(self.datasetLabel)
        hbox.addWidget(self.datasetAddButton)
        hbox.addWidget(self.datasetFileLabel)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.tableDataset)
        
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        
        self.setLayout(vbox)

    def loadDatasets(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Buka Datasets", "","*.csv", options=options)
        if fileName:
            print(fileName)
            self.datasetFileLabel.setText(fileName);
            #convert to array 2D
            #self.resultArray = ClassConvert(fileName)
            
        #QMainWindow.statusBar.showMessage("Opeing File", 4000)
        #filename = QFileDialog.getOpenFileName(self, 'Open File', '', '*.csv')
        #print(filename)
        #nama = os.path.basename(filename)
        #f = open(filename[0], 'r+')
        #filedata = f.read()
        #self.form_widget.sourceText.setText(filedata)
        #f.close()

    def predict(self):
        #hitung prediksi
        print('Hitung Prediksi')
         
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
