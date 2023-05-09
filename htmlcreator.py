import webbrowser
from bs4 import BeautifulSoup
import requests
import random
import os

# Create the HTML file based on the specified flags
def HTMLCreator(movieList, args):
    usersFormatted = '_'.join(map(str, args.users))
    filename = f'{usersFormatted}_common_watchlist_movies.html'
    
    with open(filename, 'w') as file:
        file.write('''<html>
        <head>
        <title>Letterboxd Watchlist Picker</title>
        </head> 
        <body>''')
        usersFormatted = ' '.join(map(str, args.users))
        file.write(f'<h1>{usersFormatted} Letterboxd Common Watchlisted Movies </h1>\n')

        if args.random:
            key = random.choice(list(movieList))
            file.write(f'<h4>Random Movie Choice from Watchlist: <a href={movieList[key]}>{key} </h4>')

        file.write('<table border="1" width="100%"><tr><th>Movie</th><th>Director(s)</th><th>Runtime</th><th>Genre(s)</th></tr>\n')
        for key in movieList:
            tableRow = "<tr><td>" + f"<a href={movieList[key]}>{key}</a>"

            userWatchlistUrl = f'{movieList[key]}'
            html_text = requests.get(userWatchlistUrl).text
            soup = BeautifulSoup(html_text, 'html.parser')

            director = soup.find_all('span', class_ = "prettify")
            if director is not None and len(director) != 0:
                director = [name.get_text() for name in director]
                director = ", ".join(director).strip()
            else:
                director = "N/A"
            
            length = soup.find('p', class_ = "text-link text-footer").get_text().lstrip()[0:8].rstrip()
            if not length[0].isnumeric():
                length = "N/A"

            genre = soup.find('div', class_ = "text-sluglist capitalize")
            if genre is not None:
                genre = genre.get_text().strip().replace(' ', ', ')
            else:
                genre = "N/A"

            tableRow += "</td><td>" + director + "</td><td>" + length + "</td><td>" + genre + "</td></tr>\n"
            file.write(tableRow)

        file.write('''</table>
        </body>
        </html>''')

    if args.browserOpen:
        webbrowser.open('file://' + os.path.realpath(filename))
