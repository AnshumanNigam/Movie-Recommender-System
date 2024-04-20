import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
        url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
     

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    movie_list=sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies=[]
    recommended_poster=[]

    for i in movie_list[1:6]:
        movie_id=movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommended_poster.append(fetch_poster(movie_id))
    return recommend_movies, recommended_poster

movies_list=pickle.load(open('movie_list.pkl','rb'))
movies=pd.DataFrame(movies_list)
similarity=pickle.load(open('similarity.pkl','rb'))

st.title('WatchNext')
st.markdown("A movie recommender System")  
st.markdown("Just enter a movie name and I will recommend you similar movies")  

option_selected = st.selectbox(
    'Enter a Movie Name?',
    movies['title'].values)

if st.button('Show Recommendation'):
    recommend_movies, recommended_poster = recommend(option_selected)
    cols = st.columns(5)  # Create columns for recommendations

    for i, (movie_title, poster_url) in enumerate(zip(recommend_movies, recommended_poster)):
        with cols[i]:
            if poster_url:  # Only display image if poster available
                st.image(poster_url)
            st.text(movie_title)

st.write('<hr style="border: 1px solid lightgray;">', unsafe_allow_html=True)  # Add a horizontal line
st.write("Made with Love ❤️ by [Anshuman Nigam](linkedin.com/in/anshuman-nigam-343406255)")


# if st.button('Show Recommendation'):
#     recommend_movies, recommended_poster=recommend(option_selected)
#     col1, col2, col3, col4, col5= st.beta_columns(5)[0]

# with col1:
#      st.text(recommend_movies[0])
#      st.image(recommended_poster[0])
# with col2:
#     st.text(recommend_movies[1])
#     st.image(recommended_poster[1])

# with col3:
#     st.text(recommend_movies[2])
#     st.image(recommended_poster[2])
# with col4:
#     st.text(recommend_movies[3])
#     st.image(recommended_poster[3])
# with col5:
#     st.text(recommend_movies[4])
#     st.image(recommended_poster[4])

   

