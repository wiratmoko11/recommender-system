import numpy as np
import math
from datasets import datasets 

class similiarity():
    mean = np.zeros(10)
    def __init__(self):
        
        """
        
        """
    
    def pearson(self, u, v, mean):
        rating_user_u = self.datasets[u]
        rating_user_v = self.datasets[v]
        item_of_intersect = self.intersection(rating_user_u, rating_user_v)
        #print("Item of Intersect ", item_of_intersect)
        top = 0; bottom_u = 0; bottom_v = 0
        for i in range(0, len(item_of_intersect)):
            top = top + (self.datasets[u][i]-mean[u]) * (self.datasets[v][i] - mean[v])
            bottom_u = bottom_u + pow(self.datasets[u][i] - mean[u], 2)
            bottom_v = bottom_v + pow(self.datasets[v][i] - mean[v], 2)
        
        if(bottom_v == 0):
            pearson_value = 0
        else:    
            pearson_value = top / (math.sqrt(bottom_u) * math.sqrt(bottom_v))

        return pearson_value

    def intersection(self, data1, data2):
        index_intersect = []
        for i in range(data1.shape[0]):
            if((data1[i] != 0 and data1[i] != -1) and (data2[i] != 0 and data2[i] != -1)):
                index_intersect.append(i)
            
        return index_intersect
    def mean(self, user):
        #print(self.datasets[0])
        rating_user = self.datasets[user]
        #print(rating_user.shape[0])
        temp_mean = 0
        count = 0
        for i in range(0, rating_user.shape[0]):
            if(self.datasets[user][i] != 0 and self.datasets[user][i] != -1):
                #print(self.datasets[user][i])
                temp_mean = temp_mean + self.datasets[user][i]
                count = count + 1
        if(count == 0):
            return 0
        else:
            return temp_mean / count
    
    def find_similiar_user(self, user, item, k, pearson):
        #print(user)
        sorted_pearson = self.sort_pearson(pearson[user])
        similiar = []
        for i in range(k+1):
            if(i != user):
                similiar.append(i)

        return similiar, sorted_pearson
    def sort_pearson(self, pearson):
        """
        Sorting Pearson
        """
        return np.sort(pearson)

    def prediction(self, user, item, pearson):
        #Top K
        k = 5
        theta = 0.5
        P, sorted_pearson = self.find_similiar_user(user, item, k, pearson)
        prediction_rating = 0
        top = 0; bottom = 0;
        for i in P:
            if(sorted_pearson[i] > theta):
                top = top + self.datasets[i][item] * sorted_pearson[i]
                bottom = bottom + sorted_pearson[i]
        
        if(bottom == 0):
            prediction_rating = 0
        else:    
            prediction_rating = top / bottom

        return prediction_rating

if __name__ == "__main__":
    datasets = datasets("movie-lens.csv")
    sim = similiarity()
    sim.datasets = datasets.sample()
    print(sim.mean(2))
    #print(sample_data)
        

    

    
    
    
