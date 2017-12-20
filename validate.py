import sys

class validate():

    def __init__(self, dataPredictions, dataTests):
        self.dataPrediction = dataPredictions
        self.dataTesting = dataTests

    def mse(self):
        for dataTest in self.dataTests[2]:

            if(dataTest == 0):
                for dataPrediction in self.dataPredictions[2]:
                    if(dataTest == dataPrediction):
                        self.error = self.error + 1
                    self.countData = self.countData + 1

                
        return self.error / self.countData
    
