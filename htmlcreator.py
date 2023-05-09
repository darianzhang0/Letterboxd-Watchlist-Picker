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
                   <body>  ''')
        usersFormatted = ' '.join(map(str, args.users))
        file.write(f'<h1>{usersFormatted} Letterboxd Common Watchlisted Movies </h1>')

        if args.random:
            key = random.choice(list(movieList))
            file.write(f'<h4>Random Movie Choice from Watchlist: <a href={movieList[key]}>{key} </h4>')

        file.write('<table border="1" width="100%"><tr><th>Movie</th><th>Director</th><th>Runtime</th><th>Genre(s)</th></tr>')
        for key in movieList:
            strRW = "<tr><td>" + f"<a href={movieList[key]}>{key}</a>"

            userWatchlistUrl = f'{movieList[key]}'
            html_text = requests.get(userWatchlistUrl).text
            soup = BeautifulSoup(html_text, 'html.parser')
            director = soup.find('span', class_ = "prettify")
            length = soup.find('p', class_ = "text-link text-footer")
            genre = soup.find('div', class_ = "text-sluglist capitalize")

            strRW += "</td><td>" + director.get_text() + "</td><td>" + length.get_text().lstrip()[0:8].rstrip() + "</td><td>" + genre.get_text().strip().replace(' ', ', ') + "</td></tr>"
            file.write(strRW)

        file.write('</table>')
        file.write('''</body>
                    </html> ''')

    if args.browserOpen:
        webbrowser.open('file://' + os.path.realpath(filename))
