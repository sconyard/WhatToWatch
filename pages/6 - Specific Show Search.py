import streamlit as st
import requests
import pandas as pd
from pandas import json_normalize
import pickle

st.set_page_config(layout="wide", page_title="What to Watch...?", page_icon=":tv:")

st.info('Know exactly what you want to watch, but not sure where it is available to stream? Search for it below. ')

api_key = '**enter your api key here**'

search = st.text_input('Search for a TV Show')
if search:
    search_api = f'https://api.themoviedb.org/3/search/tv?api_key={api_key}&language=en-US&query={search}&page=1'
    search_tvshows = requests.get(search_api).json()['results']
    search_json_df = json_normalize(search_tvshows)
    search_df = pd.DataFrame(search_json_df, columns=['name', 'overview', 'popularity', 'vote_average', 'vote_count', 'id'])
    st.dataframe(search_df)

    tvshow_selection = st.selectbox('Select a TV Show from Results', (search_df["name"].unique()))
    selected_tvshow_code = search_df.loc[search_df.name == tvshow_selection]["id"].iloc[0]

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

    with open('user_tv_df.pkl', 'rb') as f:
        user_tv_df = pickle.load(f)

    tvshows_filter = search_df[search_df.id == selected_tvshow_code]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Details")
        st.markdown(f'**Tagline:** *{details["tagline"]}*')
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
        st.info('Click the button to add this show to our list')
        if st.button('Add to Our List'):
            user_tv_df = pd.concat([user_tv_df, tvshows_filter], ignore_index=True)
        with open('user_tv_df.pkl', 'wb') as f:
            pickle.dump(user_tv_df, f)

    with col3:
        st.header("Similar TV Shows")
        st.dataframe(similar_df)

    st.header("Our TV Show List")
    st.dataframe(user_tv_df, use_container_width=True)
else:
    st.info('Please enter a TV show to search for')

st.write('Data in this site is provided by www.themoviedb.org, with watch provider data provided by www.justwatch.com')