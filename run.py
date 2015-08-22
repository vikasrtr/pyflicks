"""
pyFlicks

A basic movie recommender based on User-based Collaborative Filtering

__author__: vikas_rtr

"""

from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import scipy.sparse as spr

import sys

app = Flask(__name__)


class ModelData(object):

    def __init__(self, model_matrix, movies, links):
        loader = np.load(model_matrix)
        mat = spr.csr_matrix(
            (loader['data'], loader['indices'], loader['indptr']), shape=loader['shape']).toarray()
        mat = np.nan_to_num(mat)

        self.mat = mat
        self.movies = pd.read_csv(movies).values
        link = pd.read_csv(links)
        link.drop(['tmdbId', 'movieId'], axis=1, inplace=True)
        self.links = link.values


@app.route('/', methods=['GET', 'POST'])
def homepage():

    if request.method == 'GET':

        try:
            return render_template('index.html', movie_results=mymodel.movies)
        except:
            return sys.exc_info()


@app.route('/recommend', methods=['POST'])
def recommend():

    # get rating data
    mat = mymodel.mat
    ratings = np.zeros(shape=(1, mat.shape[1]))

    for i in range(ratings.shape[0]):
        ratings[0, i] = request.form.get('mid-' + str(i + 1))

    # mean of current users
    a_mean = ratings.mean()
    a_std = ratings.std()

    # mean-center ratings
    ratings = ratings - a_mean

    # mean of all users
    u_mean = np.nanmean(mat, axis=1)
    u_std = np.nanstd(mat, axis=1)

    # create array to store similarity weight
    weights = np.zeros(shape=(mat.shape[0], 1))

    # compute similarity weight for each user
    for i in range(mat.shape[0]):
        common_wts = (mat[i, :] - u_mean[i]) * ratings
        newval = (a_std * u_std[i]) + 0.0001
        a, b = newval.shape, common_wts.shape

        weights[i] = np.sum(common_wts) / newval

    # compute predictions over all movies
    mat = mat - u_mean[:, np.newaxis]
    preds = a_mean + (np.dot(mat.T, weights) / np.sum(weights))

    # combine predictions with movies
    movies = np.hstack((mymodel.movies, mymodel.links))
    preds = np.hstack((preds, movies))

    # sort by predictions and return top 10
    preds = preds[preds[:, 0].argsort(axis=0)]
    preds = preds[-10::]

    try:
        return render_template('recommend.html', preds=preds[::-1])
    except:
        return sys.exc_info()


if __name__ == "__main__":

    mymodel = ModelData(
        'data/pyflicks.npz', 'data/movies.csv', 'data/links.csv')

    app.debug = True
    app.run()
