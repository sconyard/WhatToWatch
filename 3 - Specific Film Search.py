import streamlit as st
import requests
import pandas as pd
from pandas import json_normalize
import pickle

st.set_page_config(layout="wide", page_title="What to Watch...?", page_icon=":tv:")

st.info('Know exactly what you want to watch, but not sure where it is available to stream? Search for it below.')

api_key = '**enter your api key here**'

search = st.text_input('Search for a film')
if search:
    search_api = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=en-US&query={search}&page=1'
    search_films = requests.get(search_api).json()['results']
    search_json_df = json_normalize(search_films)
    search_df = pd.DataFrame(search_json_df, columns=['title', 'overview', 'popularity', 'vote_average', 'vote_count', 'id'])
    st.dataframe(search_df)

    film_selection = st.selectbox('Select a Film', (search_df["title"].unique()))
    selected_film_code = search_df.loc[search_df.title == film_selection]["id"].iloc[0]

    film_details = f'https://api.themoviedb.org/3/movie/{selected_film_code}?api_key={api_key}&language=en-US'
    details = requests.get(film_details).json()
    details_json_df = json_normalize(details)
    details_df = pd.DataFrame(details_json_df, columns=['tagline', 'overview', 'runtime', 'release_date', 'revenue', 'vote_average', 'vote_count'])

    similar_films = f'https://api.themoviedb.org/3/movie/{selected_film_code}/similar?api_key={api_key}&language=en-US&page=1'
    similar = requests.get(similar_films).json()['results']
    similar_json_df = json_normalize(similar)
    similar_df = pd.DataFrame(similar_json_df, columns=['title', 'popularity'])

    provider_api = f'https://api.themoviedb.org/3/movie/{selected_film_code}/watch/providers?api_key={api_key}'
    providers = requests.get(provider_api).json()['results']

    providers_json_df_ALL = json_normalize(providers)

    with open('user_film_df.pkl', 'rb') as f:
        user_film_df = pickle.load(f)

    film_filter = search_df[search_df.id == selected_film_code]


    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Details")
        st.markdown(f'**Tagline:** *{details["tagline"]}*')
        st.markdown(f'**Overview:** {details["overview"]}')
        st.markdown(f'**Runtime:** {details["runtime"]}')
        st.markdown(f'**Release Date:** {details["release_date"]}')
        st.markdown(f'**Revenue:** {details["revenue"]}')
        st.markdown(f'**Vote Average:** {details["vote_average"]}')
        st.markdown(f'**Vote Count:** {details["vote_count"]}')
        st.write('The following providers are available for this film')
        try:
            num_indexes = len(providers['GB']['flatrate'])
            for i in range(num_indexes):
                st.markdown(f'**Provider:** {providers["GB"]["flatrate"][i]["provider_name"]}')
                st.image(f'https://image.tmdb.org/t/p/w500/{providers["GB"]["flatrate"][i]["logo_path"]}', width=45)
        except KeyError:
            st.error("One of the values does not exist in the JSON file, Most likely this means the film is not available to stream in the UK")
        except IndexError:
            st.error("One of the index does not exist in the JSON file, Most likely this means the film is not available to stream in the UK")

    with col2:
        st.image(f'https://image.tmdb.org/t/p/w500/{details["poster_path"]}', width=300)
        st.info('Click the button to add this film to our list')
        if st.button('Add to Our List'):
            user_film_df = pd.concat([user_film_df, film_filter], ignore_index=True)
        with open('user_film_df.pkl', 'wb') as f:
            pickle.dump(user_film_df, f)

    with col3:
        st.header("Similar Films")
        st.dataframe(similar_df)

    st.header("Our List")
    st.dataframe(user_film_df, use_container_width=True)
else:
    st.info('Please enter a film to search for')

st.write('Data in this site is provided by www.themoviedb.org, with watch provider data provided by www.justwatch.com')