import streamlit as st
import requests
import pandas as pd
from pandas import json_normalize
import pickle

st.set_page_config(layout="wide", page_title="What to Watch...?", page_icon=":tv:")

api_key = '**enter your api key here**'

st.info('Expand one of the sections below to explore the current watchlist of TV Shows and Films!')

with open('user_tv_df.pkl', 'rb') as f:
    user_tv_df = pickle.load(f)

with open('user_film_df.pkl', 'rb') as f:
    user_film_df = pickle.load(f)

with st.expander("TV Show Watchlist"):
    st.header("Our TV List")
    st.dataframe(user_tv_df, use_container_width=True)

    tv_show_selection = st.selectbox('Select a TV Show', (user_tv_df["name"].unique()))
    selected_tvshow_code = user_tv_df.loc[user_tv_df.name == tv_show_selection]["id"].iloc[0]

    tvshow_details = f'https://api.themoviedb.org/3/tv/{selected_tvshow_code}?api_key={api_key}&language=en-US'
    details = requests.get(tvshow_details).json()
    details_json_df = json_normalize(details)
    details_df = pd.DataFrame(details_json_df, columns=['tagline', 'overview', 'status', 'type','number_of_seasons', 'number_of_episodes', 'vote_average', 'vote_count'])

    similar_tvshows = f'https://api.themoviedb.org/3/tv/{selected_tvshow_code}/similar?api_key={api_key}&language=en-US&page=1'
    similar = requests.get(similar_tvshows).json()['results']
    similar_json_df = json_normalize(similar)
    similar_df = pd.DataFrame(similar_json_df, columns=['name', 'popularity'])

    provider_api = f'https://api.themoviedb.org/3/tv/{selected_tvshow_code}/watch/providers?api_key={api_key}'
    providers = requests.get(provider_api).json()['results']
    providers_json_df_ALL = json_normalize(providers)

    st.info("Click on the button below to remove the show from your list, the update won't come into effect until you select another show from the drop down menu")

    tvshows_filter = user_tv_df[user_tv_df.id == selected_tvshow_code]
    if st.button('Remove TV Show from Our List', key='tv'):
        user_tv_df = user_tv_df[~user_tv_df.id.isin(tvshows_filter.id)]
        with open('user_tv_df.pkl', 'wb') as f:
            pickle.dump(user_tv_df, f)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Details")
        st.markdown(f'**Tagline:** {details["tagline"]}')
        st.markdown(f'**Overview:** {details["overview"]}')
        st.markdown(f'**Status:** {details["status"]}')
        st.markdown(f'**Type:** {details["type"]}')
        st.markdown(f'**Number of Seasons:** {details["number_of_seasons"]}')
        st.markdown(f'**Number of Episodes:** {details["number_of_episodes"]}')
        st.markdown(f'**Vote Average:** {details["vote_average"]}')
        st.markdown(f'**Vote Count:** {details["vote_count"]}')
        st.write('The following providers are available for this show')
        try:
            num_indexes = len(providers['GB']['flatrate'])
            for i in range(num_indexes):
                st.markdown(f'**Provider:** {providers["GB"]["flatrate"][i]["provider_name"]}')
                st.image(f'https://image.tmdb.org/t/p/w500/{providers["GB"]["flatrate"][i]["logo_path"]}', width=45)
        except KeyError:
            st.error("One of the values does not exist in the JSON file, Most likely this means the show is not available to stream in the UK")
        except IndexError:
            st.error("One of the index does not exist in the JSON file, Most likely this means the show is not available to stream in the UK")

    with col2:

        st.image(f'https://image.tmdb.org/t/p/w500/{details["poster_path"]}', width=300)

    with col3:
        st.header("Similar TV Shows")
        st.dataframe(similar_df)

with st.expander("Film Watchlist"):
    st.header("Our Film WatchList")
    st.dataframe(user_film_df, use_container_width=True)

    film_selection = st.selectbox('Select a film', (user_film_df["title"].unique()))
    selected_film_code = user_film_df.loc[user_film_df.title == film_selection]["id"].iloc[0]

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

    st.info("Click on the button below to remove the show from your list, the update won't come into effect until you select another show from the drop down menu")

    film_filter = user_film_df[user_film_df.id == selected_film_code]
    if st.button('Remove from Our List', key='film'):
        user_film_df = user_film_df[~user_film_df.id.isin(film_filter.id)]
        with open('user_film_df.pkl', 'wb') as f:
            pickle.dump(user_film_df, f)

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

    with col3:
        st.header("Similar Films")
        st.dataframe(similar_df)

st.write('Data in this site is provided by www.themoviedb.org, with watch provider data provided by www.justwatch.com')