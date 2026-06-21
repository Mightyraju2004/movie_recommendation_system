import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=abf46a492ce27525fe3f525e1add549b&language=en-US".format(
        movie_id)

    try:
        # Timeout ko 4 se badhakar 7 seconds kar diya taaki slow network par bhi load ho jaye
        data = requests.get(url, timeout=7)
        data = data.json()
        poster_path = data['poster_path']

        # Agar poster_path successfully mil jata hai
        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path

    except Exception:
        pass

    # Agar internet aatke ya image na mile, toh ek clean aur valid default picture URL return karega
    return "https://images.unsplash.com/photo-1594909122845-11baa439b7bf?q=80&w=500&auto=format&fit=crop"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster from API
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

movies=pickle.load(open('movie_list.pkl','rb'))
movies_list=movies['title'].values
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')

selected_movie_name=st.selectbox('How would you like to contacted?',movies_list)

if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    # 5 Sundar columns banaye taaki horizontal layout mile
    col1, col2, col3, col4, col5 = st.columns(5)

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