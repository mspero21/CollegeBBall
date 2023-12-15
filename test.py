from datetime import datetime, timedelta
from sportsipy.ncaab.boxscore import Boxscores

games_today = Boxscores(datetime.today()-timedelta(days=1))
print(games_today.games)  # Prints a dictionary of all matchups for today