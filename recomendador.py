
import pandas as pd
import matplotlib.pyplot as plt

ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')

MoviesData = movies.merge(ratings, left_on='movieId', right_on='movieId', how='outer')
MeanDataDesc = MoviesData.groupby(by='title')['rating'].mean().sort_values(ascending=False)
# plt.plot(MeanDataDesc)

PopuDataDesc = MoviesData.groupby('title')['rating'].size().sort_values(ascending=False)
ClassMovie = pd.concat([MeanDataDesc,PopuDataDesc], axis = 1)
ClassMovie.columns = ['promedio_rating','numero_califs']

EstadisMovie = ClassMovie.groupby('numero_califs')['promedio_rating'].mean().sort_values(ascending=False)
# plt.bar(EstadisMovie.values[:50],EstadisMovie.index[:50], width = 1)

k = EstadisMovie[EstadisMovie.index[:10]]

NewData = MoviesData.pivot_table(index ='userId', columns='title', values='rating')






#Obtenga una lista con las calificaciones que los usuarios dieron a la pelicula mas popular (la que se tiene en mente luego de la comprobacion estadistica)

#Haga una nueva lista con la correlacion entre la lista anterior y el ultimo dataframe que se implemento, en esta instancia se va calcular la correlacion entre 
#todas las peliculas del dataframe y la pelicula mas popular y mejor calificada del dataframe (pista: corrwith)

#Implemente un nuevo dataframe con la ultima lista (la de las correlaciones) y a la columna llamela 'Correlaciones'
#Elimine de esta lista todos los valores NaN

#A este ultimo dataframe agreguele la columna del dataframe donde se registraron la cantidad de calificaciones por pelicula ('numero_califs') (pista: join)

#Visualice las recomendaciones como las peliculas con un numero de calificaciones mayores al percentil 60 del numero de calificaciones por pelicula ('numero_califs')
#y ordene el dataframe en orden descendente de la columna 'Correlaciones'




