import requests
import datetime
import json
from bs4 import BeautifulSoup
from varaibles import drafted_teams
# Send an HTTP GET request to the URL

SCORES= {}
found_teams = []
missing_teams = []
TODAY = datetime.date.today()
TEAM_NAMES = ["Dunne","Jack","Mike","Silv","Sully"]
DRAFTED_TEAMS = drafted_teams
# Define the start date (November 1st)
START_DATE = datetime.date(2023, 11, 6)


def initialze_score(output_file):
    for name in TEAM_NAMES:
        SCORES[name]=0
    print(SCORES, file=output_file)
 
def generateTeams(output_file):
    try:
        #Attempt to open rosters file
        with open('rosters.json', 'r') as json_file:
            #load data into json_data object
            rosters = json.load(json_file)
    except:
        print("roster file loaded unsuccsfully", file=output_file)
        exit()

    if 'TCU' in rosters['Dunne']:
        print("Rosters successfully created", file=output_file)
        return rosters
    else:
        print("Rosters unsucusfully created", file=output_file)
        exit()

def generateTop25(output_file):
    top25URL = "https://apnews.com/hub/ap-top-25-college-basketball-poll"
    response = requests.get(top25URL)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        team_ranking_list = soup.find_all('dd', class_='PollModuleRow')
        rankings = {}
        for team_ranking in team_ranking_list:  
            # Extract and print the team name and ranking
            rank = team_ranking.find('div', class_='PollModuleRow-rank').text.strip()
            team = team_ranking.find('div', class_='PollModuleRow-team').find('a').text.strip()
            # print(f"Team: {team}, Ranking: {rank}")
            rankings[team] = rank
        return rankings
    else:
        print("Failed to retrieve the web page. Status code:", response.status_code, file=output_file)


def generateGames(rosters, top25, output_file):
    # Define a list to store the formatted date strings
    date_strings = []
    # Loop through dates
    looping_date = START_DATE
    while looping_date <= TODAY:
        formatted_date = looping_date.strftime("%Y/%m/%d")
        date_strings.append(formatted_date)
        # Increment the current_date by one day
        looping_date += datetime.timedelta(days=1)

    # Create the URL strings
    base_url = "https://www.ncaa.com/scoreboard/basketball-men/d1/"
    url_dates = [f"{base_url}{date}/all-conf" for date in date_strings]

    # Print the generated URL strings
    for url in url_dates:
        print(f"Scoring games from this link: {url}", file=output_file)
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')
            games = soup.find('div', class_="gamePod_content-pod_container").find_all('div', class_="gamePod")
            for game in games:
                    if game.find('li', class_="winner") is not None:
                        winner = game.find('li', class_="winner").find('span',class_="gamePod-game-team-name").text
                        teams = game.find_all('li')
                        home_team = teams[0].find('span',class_="gamePod-game-team-name").text
                        away_team = teams[1].find('span',class_="gamePod-game-team-name").text
                        loser = home_team if away_team == winner else away_team
                        if winner in DRAFTED_TEAMS:
                            game_winner(winner,loser,rosters, output_file)
                            if loser in top25:
                                top_25_win(winner,loser,rosters, output_file)
                            #TO ADD
                                #ROAD CONFERENCE WINS



                            #Uncomment this code to track teams that are being found for debugging purposes
                            # if winner not in found_teams:
                            #     found_teams.append(winner)
                            # if loser not in found_teams:
                            #     found_teams.append(loser)
        else:
            print("Failed to retrieve the web page. Status code:", response.status_code, file=output_file)
            exit()


def game_winner(winner,loser,rosters, output_file):
     for roster in TEAM_NAMES:
        if winner in rosters[roster]:
            print(f"{roster} had {winner} who beat {loser}... One Point awarded", file=output_file)
            SCORES[roster] = SCORES[roster]+1

def top_25_win(winner,loser,rosters, output_file):
     for roster in TEAM_NAMES:
        if winner in rosters[roster]:
            print(f"{roster} had {winner} who beat {loser} who was ranked in top 25... Five Points awarded", file=output_file)
            value = SCORES[roster]
            newValue = value + 5
            SCORES[roster] = newValue

    
# def find_missing_teams(teams):
#     for roster in TEAM_NAMES:
#         for team in teams[roster]:
#             if team not in found_teams:
#                 missing_teams.append(team)

        
# Define the main function that calls my_function
def main():
    with open('scores.txt', 'w') as output_file:
        print("Set scores to 0", file=output_file)
        initialze_score(output_file)
        print("Generating Scores", file=output_file)
        teams = generateTeams(output_file)
        top25 = generateTop25(output_file)
        
        games = generateGames(teams, top25, output_file)
        #TO ADD
            #RANKINGS AFTER WEEK 3
            #CONFERENCE CHAMPS
            #REGULAR SEASON CONFERENCE CHAMPS
            #LAST PLACE FINISH
            #POY 
        #Uncomment to find missing teams
        #find_missing_teams(teams)
        print(SCORES, file=output_file)

# Check if this script is the main program (not imported as a module)
if __name__ == "__main__":
    main()