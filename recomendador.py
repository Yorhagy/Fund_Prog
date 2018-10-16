
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')

MoviesData = movies.merge(ratings, left_on='movieId', right_on='movieId', how='inner')

MeanDataDesc = MoviesData.groupby('movieId')['rating'].mean().sort_values(ascending=False)

PopuDataDesc = MoviesData.groupby('movieId')['rating'].size().sort_values(ascending=False)

ClassMovie = pd.concat([MeanDataDesc, PopuDataDesc], axis=1)
ClassMovie.columns = ['promedio_rating', 'numero_califs']

EstadisMovie = ClassMovie.groupby('numero_califs')['promedio_rating'].mean()

ClassMovie['Populares'] = ClassMovie['promedio_rating'] * np.log(ClassMovie['numero_califs'])
PopuMovies = ClassMovie.merge(movies, left_on='movieId', right_on='movieId', how='outer').sort_values(by='Populares', ascending=False)
print('Populares', PopuMovies.iloc[PopuMovies.iloc[0]['movieId']]['title'])

NewData = MoviesData.pivot(index='userId', columns='movieId', values='rating')

ClassMoviesPopu = NewData[PopuMovies.iloc[0]['movieId']]

CorrMovies = NewData.corrwith(ClassMoviesPopu, axis=0)

DataCorrMovies = pd.DataFrame({'Correlaciones': CorrMovies, 'movieId': CorrMovies.index})

DataCorrMovies.dropna(inplace = True)

NewDataCorrMovies = DataCorrMovies.merge(ClassMovie, left_on='movieId', right_on='movieId', how='inner')

RecMovies = NewDataCorrMovies[NewDataCorrMovies['numero_califs'] > NewDataCorrMovies['numero_califs'].quantile(0.99) ].sort_values(by='Correlaciones', ascending=False)
print(RecMovies)