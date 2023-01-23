# WhatToWatch

A Streamlit app that allows users to explore a watchlist of TV Shows and Films by expanding one of the sections below. The app provides details about the selected TV Show, similar TV Shows, and providers available for the show. Users can also add and remove TV Shows from their watchlist.
How to use

    Run the command streamlit run app.py to start the app
    Expand the "TV Show Watchlist" section
    Select a TV Show from the dropdown menu
    Click on the button "Remove TV Show from Our List" to remove the selected TV Show from the watchlist
    To add a TV Show to the watchlist, you need to run the code that add the show first
    You can also see the "Film Watchlist" section, where you can remove or add a film to your watchlist

Dependencies

    streamlit==0.67.0
    pandas==1.2.3
    requests==2.25.0

API key

You need an API key from The Movie Database API to use this app.
Note

The app will save the watchlist in two pickle files user_tv_df.pkl and user_film_df.pkl, so you can keep the watchlist even after closing the app. If you want to start a new watchlist, you need to delete the pickle files.
