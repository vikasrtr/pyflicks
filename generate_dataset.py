"""
pyFlicks

Script to generate required dataset

"""

import numpy as np
import pandas as pd
import scipy.sparse as spr

# load users, movies and ratings
movies = pd.read_csv('data/movies.csv')
ratings = pd.read_csv('data/ratings.csv')
ratings.drop('timestamp', axis=1, inplace=True)

# create a matrix of form [Users, Movies] with each element having a movie
# rated by a given user

mat = np.zeros(
    shape=(ratings.userId.unique().shape[0], movies.shape[0]))

# fill mat with ratings corresponding to each movie
# for each rating find corresponding index in mat
mov_ids = movies.movieId.tolist()

# loop through each rating
rat = ratings.values.astype(np.int)

for r in rat:
    mat[r[0] - 1, mov_ids.index(r[1])] = r[2]

# save model as sparse matrix
spr_matrix = spr.csr_matrix(mat)

np.savez('data/pyflicks.npz', data=spr_matrix.data, indices=spr_matrix.indices,
         indptr=spr_matrix.indptr, shape=spr_matrix.shape)

# Code to load back matrix
# loader = np.load('data/movie_tags.npz')
# new_csr = spr.csr_matrix(
#     (loader['data'], loader['indices'], loader['indptr']), shape=loader['shape'])

print('Done!')
