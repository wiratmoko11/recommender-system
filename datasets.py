import sys
import numpy as np

class datasets(object):
    def __init__(self, datasets):
        self.datasets = datasets
        self.to_matrix2d()
        
    def to_matrix2d(self):
        self.matrix_datasets = np.loadtxt(open(self.datasets, "rb"), delimiter=",", skiprows=1, usecols=range(0,3)).astype("float")

    def split(self, num_split=5):
        self.split_datasets = np.split(self.matrix_datasets, num_split)

    def join(self, array_part):
        
        for i in array_part:
            join_rating = np.concatenate(join_rating, i)
            
        return join_rating

    def to_table(self):
        user_id = np.unique(self.matrix_datasets[:, 0])
        movie_id = np.unique(self.matrix_datasets[:, 1])
        join_rating = self.join([1,2,3,4])
        rating = join_rating[2] * 2
        
        matrix_rating = np.zeros(shape=(user_id.shape[0], movie_id.shape[0]))

        for row in rating:
            index_movie = np.where(movie_id==row[1])
            matrix_rating[row[0], index_movie] = row[2]

        return matrix_rating
        
if __name__ == "__main__":
    datasets = datasets("movie-lens.csv")
    datasets.split(4)
    datasets.to_table()
    #print(datasets.movie_id)
    #print(datasets.split_datasets[3].shape[0])
