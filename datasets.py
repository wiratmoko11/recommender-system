import sys
import numpy as np
import pandas

class datasets(object):
    def __init__(self, datasets):
        self.datasets = datasets

    def sample(self):
        sample_data = np.zeros((5, 6))
        sample_data[0][0] = 7
        sample_data[0][1] = 6
        sample_data[0][2] = 7
        sample_data[0][3] = 4
        sample_data[0][4] = 5
        sample_data[0][5] = 4

        sample_data[1][0] = 6
        sample_data[1][1] = 7
        sample_data[1][2] = -1
        sample_data[1][3] = 4
        sample_data[1][4] = 3
        sample_data[1][5] = 4

        sample_data[2][0] = -1
        sample_data[2][1] = 3
        sample_data[2][2] = 3
        sample_data[2][3] = 1
        sample_data[2][4] = 1
        sample_data[2][5] = -1

        sample_data[3][0] = 1
        sample_data[3][1] = 2
        sample_data[3][2] = 2
        sample_data[3][3] = 3
        sample_data[3][4] = 3
        sample_data[3][5] = 4

        sample_data[4][0] = 1
        sample_data[4][1] = -1
        sample_data[4][2] = 1
        sample_data[4][3] = 2
        sample_data[4][4] = 3
        sample_data[4][5] = 3

        user = np.array([1, 2, 3, 4, 5])
        item = np.array([1, 2, 3, 4, 5 ,6])

        return sample_data, [], user, item
    
    def to_matrix2d(self):
        data =  np.loadtxt(open(self.datasets, "rb"), delimiter=",", skiprows=1, usecols=range(0,3)).astype("float")
        #data = np.array(data)

        return data[:100000]
    def split(self, num_split=5):
        matrix_datasets = self.to_matrix2d()
        #print(matrix_datasets)
        #matrix_datasets = np.asarray(matrix_datasets)
        np.random.shuffle(matrix_datasets)
        #print(matrix_datasets)
        return np.split(matrix_datasets, num_split)
    

    def join(self, array_part):
        join_rating = array_part[0]
        for i in range(1, len(array_part)):
            join_rating = np.append(join_rating, array_part[i], axis=0)
        return join_rating

    def to_table(self, data):
        full_data = self.to_matrix2d()
        user_id = np.unique(full_data[:, 0]).astype(int)
        movie_id = np.unique(full_data[:, 1]).astype(int)
        rating = data
        matrix_rating = np.zeros(shape=(user_id.shape[0], movie_id.shape[0]))
        #print(matrix_rating.shape)
        
        for row in rating:
            #print(row)
            index_movie = np.where(movie_id==row[1])
            matrix_rating[row[0].astype(int)-1, index_movie[0][0]] = row[2]

        return matrix_rating

    def get_user(self, full_data):
        user_id = np.unique(full_data[:, 0]).astype(int)
        return user_id

    def get_item(self, full_data):
        movie_id = np.unique(full_data[:, 1]).astype(int)
        return movie_id
    def get_user_item(self, full_data):
        user_id = np.unique(full_data[:, 0]).astype(int)
        movie_id = np.unique(full_data[:, 1]).astype(int)
        return user_id, movie_id
        
    def to_data_testing(self, array_data):
        array_data[:, 2] = -1
        return array_data
    
if __name__ == "__main__":
    datasets = datasets("movie-lens.csv")
    part_data = datasets.split(4)
    join_data = datasets.join([part_data[0], part_data[1], part_data[3]])
    table_data = datasets.to_table(join_data)
    df = pandas.DataFrame(table_data)
    
    #df.to_csv('test')
    #print(datasets.movie_id)
    #print(datasets.split_datasets[3].shape[0])
