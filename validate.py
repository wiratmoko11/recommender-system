import sys
from datasets import datasets
from similiarity import similiarity
import pandas
import numpy as np

class validate():

    def __init__(self):
        #self.dataPrediction = dataPredictions
        #self.dataTesting = dataTests
        """"""

    def mae(self, data_training, data_testing, data_predict):
        count_data = 0
        count_e = 0
        for i in range(data_predict.shape[0]):
            for j in range(data_predict.shape[1]):
                if(data_training[i][j] == -1):
                    count_e = abs(data_testing[i][j] - data_predict[i][j])
                    count_data = count_data + 1
                
        return count_e / count_data

    def training(self):
        k = 5
        dataset = datasets("movie-lens.csv")
        sim = similiarity()
        real_part_data = dataset.split(k)
        testing_data = dataset.to_matrix2d()
        pandas.DataFrame(testing_data).to_csv("report/testing data.csv")
        pandas.DataFrame(dataset.to_table(dataset.join(real_part_data[:]))).to_csv("report/rating testing data.csv")
        user, movie = dataset.get_user_item(testing_data)
        
        for i in range(k):
            part_data = np.copy(real_part_data)
            mean = np.zeros(user.shape[0])
            pearson = np.zeros((user.shape[0], user.shape[0]))
            part_data[i] = dataset.to_data_testing(part_data[i])
            
            training_data = dataset.join(part_data[:])
            pandas.DataFrame(training_data).to_csv("report/training data-"+str(i)+".csv")
            table_data = dataset.to_table(training_data)
            predict_data = np.copy(table_data)
            
            pandas.DataFrame(table_data).to_csv("report/rating training data-"+str(i)+".csv")
            sim.datasets = table_data
            #Cari Mean
            print("Hitung Mean")
            for i_mean in range(user.shape[0]):
                mean[i_mean] = sim.mean(i_mean)
                
            pandas.DataFrame(mean).to_csv("report/mean-"+str(i)+".csv")
            
            
            print("Hitung Pearson")
            for u in range(user.shape[0]):
                for v in range(u, user.shape[0]):
                    pearson[u][v] = sim.pearson(u, v, mean)
                    pearson[v][u] = pearson[u][v]
                    
                    
                    print("Pearson User ", u, "Dan ", v, " = ", pearson[u][v])

            df = pandas.DataFrame(pearson)
            df.to_csv("report/result pearson-"+str(i)+".csv")
            
            
            print("Hitung Prediksi")
            #print(table_data.shape)
            for row_user in range(table_data.shape[0]):
                for col_item in range(table_data.shape[1]):
                    if(table_data[row_user][col_item] == -1):
                        #Predicting
                        rating_prediction = sim.prediction(row_user, col_item, pearson)
                        predict_data[row_user][col_item] = rating_prediction
            
            pandas.DataFrame(predict_data).to_csv("report/predict-"+str(i)+".csv")
            
            print("Hitung MAE")
            mae_result = np.zeros(k)
            mae_result[i] = self.mae(table_data, dataset.to_table(dataset.join(real_part_data[:])), predict_data)
            pandas.DataFrame(mae_result).to_csv("report/mae.csv")
        
        result = np.sum(mae_result) / k
        print("Result = ", result)
            
if __name__ == "__main__":
    validate = validate()
    validate.training()
