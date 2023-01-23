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

You need an API key from The Movie Database API to use this app. To get started with The Movie Database API, follow the [guide](https://developers.themoviedb.org/3/getting-started/introduction)

## Getting Started

Download the files in this repo.

The app needs to meet the above dependancies, so I would recommend creating a virtual python environment and loading the required modules and libraries into that.  Tools like [Anaconda Navigator](https://docs.anaconda.com/navigator/index.html) make that very simple.

Launch a terminal session in your virtual pythin environment and navigate to the location containing the files. 

The app can be launched by running the following command from the directory containing the files.

    streamlit run watchlist.py 
    
The app will be hosted at

    http://localhost:8501



![First Launch](https://github.com/sconyard/WhatToWatch/blob/c5c03baec6763824666c641b7a04fc5069457ed1/media/Watchlist%20Homepage.png)


## Note

The app will save the watchlist in two pickle files user_tv_df.pkl and user_film_df.pkl, so you can keep the watchlist even after closing the app. If you want to start a new watchlist, you need to delete the pickle files.
