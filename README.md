# WhatToWatch

"What are we watching tonight...." followed by mindless scrolling through streaming provider interfaces looking for something interesting...  Sound familiar?  You need to use WhattoWatch!

WhatToWatch is a python app developed using Streamlit, using information provided by [The Movie Database API](https://www.themoviedb.org/) that allows users to discover and explore TV shows and Films and save those you want to watch to a watchlist.

A user can browse titles by genre across all available streaming providers, search across genres within a single streaming provider or it they are looking for a specific title they can search for it directly.  When searching by genre the most popular rank titles are provided first, all returned results include popularity, vote average and vote counts. 

Each search mode shows key information about the titles, like running time, number of episodes and seasons etc.

When a user has found a title they'd like to watch it is saved to a watchlist, that can be referenced next time someone asks "What are we wathcing tonight...?"

## Dependencies

    streamlit
    pandas
    requests
    pickle

## API key

You need an API key from The Movie Database API to use this app.  Follow the guide from [TMDB](https://developers.themoviedb.org/3/getting-started/introduction)


Note

The app will save the watchlist in two pickle files user_tv_df.pkl and user_film_df.pkl, so you can keep the watchlist even after closing the app. If you want to start a new watchlist, you need to delete the pickle files.
