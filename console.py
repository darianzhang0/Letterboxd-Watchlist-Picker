from rich.console import Console
from rich import print as rprint
import argparse
from watchlistpicker import WatchListPicker
from htmlcreator import HTMLCreator
import pprint

console = Console()

# Add command line arguments. The -h flag gives all the options
parser = argparse.ArgumentParser(description='Letterboxd Watchlist Picker')
parser.add_argument('--users', '-u', dest='users', action="extend", nargs="+", help = 'Letterboxd users')
parser.add_argument('--common-watchlist', '-w', dest='watchlist', action="store_true", default=False, help='Find common watchlist movies')
parser.add_argument('--random-movie', '-r', dest='random', action="store_true", default=False, help='Pick a random movie from the common watchlist movies')
parser.add_argument('--save-html', '-s', dest='html', action="store_true", default=False, help='Saves HTML file of common watchlist movies')
parser.add_argument('--browser-open', '-b', dest='browserOpen', action="store_true", default=False, help='Opens saved HTML file in browser')
args = parser.parse_args()

print(args.users)

if __name__ == '__main__':
    console.print('[dark_orange] Provided Command Line Arguments')
    # Show the current flag settings
    for flag,value in vars(args).items():
        rprint(f'\t{flag}={value}')
    print()
    
    if args.watchlist:
        commonWatchlist = WatchListPicker(args.users)
        pprint.pprint(commonWatchlist)

        if args.html:
            HTMLCreator(commonWatchlist, args)
