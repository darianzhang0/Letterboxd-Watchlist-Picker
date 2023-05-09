from bs4 import BeautifulSoup
import requests

letterboxdUrl = 'https://letterboxd.com'

# Get the common movies on each users watchlist along with the letterboxd movie link
def WatchListPicker(users):
    watchlists = []
    for user in users:
        watchlists.append(GetWatchList(user))
        
    commonWatchlist = GetCommonMovies(watchlists)
    return commonWatchlist

# Get the watchlist of the given user
def GetWatchList(user):
    watchlist = {}
    userWatchlistUrl = f'{letterboxdUrl}/{user}/watchlist/'
    html_text = requests.get(userWatchlistUrl).text
    soup = BeautifulSoup(html_text, 'html.parser')
    movies = soup.find_all('li', class_ = "poster-container")

    for movie in movies:
        movieLink = movie.find('div')
        movieName = movie.find('img')
        watchlist[movieName['alt']] = letterboxdUrl + movieLink['data-film-slug']

    pagesNum = soup.find_all('li', class_ = "paginate-page")
    if pagesNum:
        maxPage = pagesNum[len(pagesNum) - 1].get_text()
        for page in range (2, int(maxPage) + 1):
            userWatchlistUrl = f'{letterboxdUrl}/{user}/watchlist/page/{page}'
            html_text = requests.get(userWatchlistUrl).text
            soup = BeautifulSoup(html_text, 'html.parser')
            movies = soup.find_all('li', class_ = "poster-container")
            for movie in movies:
                movieLink = movie.find('div')
                movieName = movie.find('img')
                watchlist[movieName['alt']] = letterboxdUrl + movieLink['data-film-slug']
    
    return watchlist

# Get the common movies from each users watchlist
def GetCommonMovies(watchlists):
    commonMovies = set(watchlists[0])
    for watchlist in watchlists[1:]:
        commonMovies.intersection_update(set(watchlist))

    commonWatchlist = {key: watchlists[0][key] for key in commonMovies}
    return commonWatchlist
