## If you are getting error in running the code please use the follwing command in terminal:- python -m streamlit run app.py
import pickle
import pandas as pd
import requests
import streamlit as st

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
def recommend(movies):
    movie_index = movie[movie['title'] == movies].index[0]
    distances = similarity[movie_index]
    # We need to store the original index number of each movie otherwise it is difficult to get those after sorting , for this we will use enumerate function
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters=[]
    for i in movies_list:
        # To fetch movies poster from api
        movie_id=movie.iloc[i[0]].movie_id
        recommended_movies.append(movie.iloc[i[0]].title)
        # To print posters of the movies
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


st.title('Movies Recommender System')
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movie = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

selected_movie_name = st.selectbox(
    'Select the movie name', movie['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    col1,col2,col3,col4,col5=st.beta_columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

# To find out which function to use to build a website we can use streamlit documentation itself
