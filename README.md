# WhatToWatch

"What are we watching tonight...." followed by mindless scrolling through streaming provider interfaces looking for something interesting...  Sound familiar?  You need to use WhattoWatch!

WhatToWatch is a python app developed using [Streamlit](https://streamlit.io/), using information provided by [The Movie Database API](https://www.themoviedb.org/) and [JustWatch](https://www.justwatch.com/) that allows users to discover and explore TV shows and Films and save those you want to watch to a watchlist.

A user can browse titles by genre across all available streaming providers, search across genres within a single streaming provider or if they are looking for a specific title they can search for it directly.  When searching by genre the most popular rank titles are provided first, all returned results include popularity, vote average and vote counts. 

Each search mode shows key information about the titles, like running time, number of episodes and seasons etc.

When a user has found a title they'd like to watch, it is saved to a watchlist that can be referenced next time someone asks "What are we watching tonight...?"

## Dependencies

    - streamlit
    - pandas
    - requests
    - pickle

## API key

You need an API key from The Movie Database API to use this app. To get started with The Movie Database API, follow the [guide](https://developers.themoviedb.org/3/getting-started/introduction)

## How does it work?

The app is built using streamlit to provide the layout, text inputs, buttons and wraps around the core functions of the various api lookups, the dataframes that are built and the pickle files.

Requests queries multiple APIs, to build up the information that is presented back to the users.  The APIs that are queried can be catagorised as;

    - Discover
    - Genre
    - Search
    - Details
    - Similar
    - Watch Provider

There are different API endpoints for TV and Movies.

All APIs are hosted by [The Movie Database](https://www.themoviedb.org/), with Watch provider information provided by [JustWatch](https://www.justwatch.com/)

Pandas is used to hold the information and where required pass it on to the other queries. The watchlists are loaded from pickle files, each time a row is added to the dataframe via the ***add to our list*** button the whole pickle file is updated.  Entries are removed using a similar method.

## Getting Started

Download the files in this repo.

The app needs to meet the above dependencies, so I would recommend creating a virtual python environment and loading the required modules and libraries into that.  Tools like [Anaconda Navigator](https://docs.anaconda.com/navigator/index.html) make that very simple.

Launch a terminal session in your virtual python environment and navigate to the location containing the files. 

The app can be launched by running the following command from the directory containing the files.

    streamlit run watchlist.py 
    
The app will be hosted at

    http://localhost:8501

## How to use

### Homepage

When accessing the app the homepage is a view of the TV and Film watchlists, in expandable sections to make it easier to browse initially for what you want to access.

![Watchlist](https://github.com/sconyard/WhatToWatch/blob/c5c03baec6763824666c641b7a04fc5069457ed1/media/Watchlist%20Homepage.png)

Each watchlist can be expanded to browse, the first part is the information for all titles on the watchlist

![watchlist detail](https://github.com/sconyard/WhatToWatch/blob/615fdf437d4cc0e6e5a569540ea8966d9327aa0a/media/Watchlist%202.png)

Titles of interest can be selected from the dropdown list, and information regarding the title and from the similar titles api is presented.  This is where there is an option to remove titles being browsed from the watchlist.

![watchlist detail](https://github.com/sconyard/WhatToWatch/blob/615fdf437d4cc0e6e5a569540ea8966d9327aa0a/media/Watchlist%201.png)

### Searching by Genre

This is a multipage Streamlit app, which generates a collapsible menu on the left of the page.  The genre search options are available via ***Film Search*** or ***TV Show Search***.  Selecting the desired genre on this page generates a list of titles across all streaming providers, filtered by popularity from The Movie Database site.

![genre](https://github.com/sconyard/WhatToWatch/blob/1d89781d3449914d7b59975944b02013e1e1c309/media/Genre%20Search.png)

Each of the discovered titles is selectable from the next dropdown box, on selection the details for the title are displayed and there is an option to add the selected title to the watchlist.

![genre](https://github.com/sconyard/WhatToWatch/blob/1d89781d3449914d7b59975944b02013e1e1c309/media/Details%20and%20Add.png)

### Searching by Provider

The tool also provides a method to search by selecting a streaming provider.  Streaming providers returned from an API query are presented for selection in a dropdown box. 

![provider](https://github.com/sconyard/WhatToWatch/blob/1d89781d3449914d7b59975944b02013e1e1c309/media/Provider%20Search.png)

After selecting a provider the desired genre can be selected and a list of titles is generated that can be added to the watchlist via the details section.

![provider](https://github.com/sconyard/WhatToWatch/blob/1d89781d3449914d7b59975944b02013e1e1c309/media/Provider%20Search%202.png)

### Searching by text lookup

The app also provides a method to search for titles from a text lookup, useful if you know the title you want to watch, but are not sure where or if it is streaming currently.

![text lookup](https://github.com/sconyard/WhatToWatch/blob/1d89781d3449914d7b59975944b02013e1e1c309/media/Text%20Search.png)

Where there are multiple matches for a title, multiple results will be returned.

![text lookup](https://github.com/sconyard/WhatToWatch/blob/1d89781d3449914d7b59975944b02013e1e1c309/media/Text%20Search%202.png)

## Notes of usage

***Code provided without any support whatsoever***

###  Got into a pickle?

The app will save the watchlist in two pickle files user_tv_df.pkl and user_film_df.pkl.  This allows the watchlist to be kept even after closing the app. 

An empty pickle file will generate an error in the watchlist page, if you get an error on the watchlist page try adding something to the tv and film watchlists.  

If the pickle files corrupt they will need to be recreated, the simplest way to do that is to create the required dataframes and save new pickle files.  The structure of each watchlist dataframe is the same, the command to recreate them are below, for the film watchlist just substitute 'tv' for 'film'

    user_tv_df = pd.DataFrame(columns=['name', 'overview', 'popularity', 'vote_average', 'vote_count', 'id'])
    with open('user_tv_df.pkl', 'wb') as f:
        pickle.dump(user_tv_df, f)
        
###  Region

I'm in the UK, some of the API calls are hardcoded to the UK as I had no need to see what's available in other regions. Following the methods in this code adding a region lookup should be straightforward. 

The searches via with watch providers selected require a region element, the part of the api query that sets that is ***'&watch_region=XXX'***
