# Letterboxd Movie Watchlist Picker
[Letterboxd.com](https://letterboxd.com/) is a movie logging and review site where users can keep track of all the movies they have watched. Letterboxd.com also allows users to add movies to their watchlist which they can use to decide what to watch.

This project shows all watchlist movie overlap on multiple Letterboxd.com users' watchlists and can randomly pick one movie from that list. This allows users to easily look at what movies they have in common with other users' watchlists and easily decide what to watch together. An HTML page showing the common movies can be optionally created and opened in a browser.

## Running the Project
```
python3 console.py [flags]
```
The flags that can be set are:
| Flag        | Description           | Usage  |
| ------------- |:-------------:| -----:|
| -h, --help      | Show the optional arguements | `python3 console.py -h` |
| --users USERS, -u USERS | Letterboxd users | `python3 console.py -u davvoint north778`  |
| --common-watchlist, -w | Find common watchlist movies from specified users | `python3 console.py -w -u davvoint north778` |
| --random-movie, -r  | Pick a random movie from the common watchlist movies | `python3 console.py -wr -u davvoint north778` |
| --save-html, -s | Saves HTML file of common watchlist movies | `python3 console.py -wrs -u davvoint north778` |
| --browser-open, -b | Opens the saved HTML file in a browser | `python3 console.py -wrsb -u davvoint north778` |

## Example Run
```
python3 console.py -wsbr -u davvoint north778
```
