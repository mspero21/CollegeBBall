import requests
import urllib.request
from requests import Session
import datetime
import json
import re
from bs4 import BeautifulSoup
from varaibles import drafted_teams, team_mappings, create_team_to_conference_dict, conferences_dict

teamsConference = create_team_to_conference_dict()
session = Session()
import re

# Send an HTTP GET request to the URL

SCORES = {}
TODAY = datetime.date.today()
TEAM_NAMES = ["Dunne", "Jack", "Mike", "Silv", "Sully"]
DRAFTED_TEAMS = drafted_teams
TEAM_MAPPINGS = team_mappings
START_DATE = datetime.date(2023, 11, 6)

# found_teams = []
# missing_teams = []


def generateTop25Dates():
    top25Dates = []
    start_date = datetime.datetime.strptime("06/11", "%d/%m")
    top25Dates.append(start_date.strftime("%d/%m"))
    for i in range(25):
        start_date += datetime.timedelta(days=7)
        top25Dates.append(start_date.strftime("%d/%m"))
    print(top25Dates)
    return top25Dates


def initialze_score(output_file):
    for name in TEAM_NAMES:
        SCORES[name] = 0
    print(SCORES, file=output_file)


def generateTeams():
    # Attempt to open rosters file
    with open("rosters.json", "r") as json_file:
        # load data into json_data object
        rosters = json.load(json_file)

    #Random test to see if rosters looking alright
    if "TCU" in rosters["Dunne"]:
        print("Rosters successfully created")
        return rosters
    else:
        print("Rosters unsucusfully created")
        exit()


def generateTop25(id, top_25, rosters, week_no, output_file, points):
    top_25 = []
    #Creates the URL to look at for top 25
    top25URL = (
        f"https://www.collegepollarchive.com/mbasketball/ap/seasons.cfm?appollid={id}"
    )
    response = requests.get(top25URL)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, "html.parser")
        first_rows = soup.find_all("table")
        rows = first_rows[4].find_all("tr")
        val = 1
        #Loops through the 25 rows we need to find 
        for num in range(8, 33):
            #Some ugly work of getting the team from the website into the format we want
            team_rows = rows[num].find_all("td")
            team = team_rows[2].text
            team_final_unstripped = re.sub(r"\s*\([^)]*\)", "", team)
            team_final = team_final_unstripped.strip()
            if team_final not in DRAFTED_TEAMS:
                print(team_final)
                team_final = team_mappings[team_final]

            #Adds the team to the top 25 list
            top_25.append(team_final)
            
            #Checks to see if we are calculating points for standings
            if points:
                if val < 26:
                    #On the first loop
                    if val == 1:
                        #Checks to makes sure the No. 1 team has been drafted
                        if team_final in DRAFTED_TEAMS:
                            #Adds the points to the team for having No. 1 rank
                            for name in TEAM_NAMES:
                                if team_final in rosters[name]:
                                    SCORES[name] = SCORES[name] + 1 
                                    print(
                                        f"{name} has {team_final} who is ranked No. 1 for week {week_no}...1 point awarded",
                                        file=output_file,
                                    )
                    #Same process as above but now for 2-15
                    if val < 16:
                        if team_final in DRAFTED_TEAMS:
                            for name in TEAM_NAMES:
                                if team_final in rosters[name]:
                                    SCORES[name] = SCORES[name] + 3
                                    print(
                                        f"{name} has {team_final} who is ranked No. {val} for week {week_no}.....3 points awarded",
                                        file=output_file,
                                    )
                    #Same process as above but now for 15-25
                    if val >= 16 and val <= 25:
                        if team_final in DRAFTED_TEAMS:
                            for name in TEAM_NAMES:
                                if team_final in rosters[name]:
                                    SCORES[name] = SCORES[name] + 1
                                    print(
                                        f"{name} has {team_final} who is ranked No. {val} for week {week_no}.....1 point awarded",
                                        file=output_file,
                                    )
                val += 1
    print(top_25)
    return top_25


def generateScore(rosters, output_file):

    #Finds dates to update top 25 standings
    top25Dates = generateTop25Dates()
    # Define a list to store the formatted date strings
    date_strings = []

    #Some variables we will use for scraping
    base_url = "https://www.ncaa.com/scoreboard/basketball-men/d1/"
    top_25_counter = 0
    top_25_id = 1260
    top_25 = []
    week_no = 1

    # # Set the start date as November 1st
    # start_date = datetime.date(2023, 11, 6)

    # # Get the current date
    # current_date = datetime.date.today()

    # # Loop through the dates
    # while start_date <= current_date:
    #     print(start_date.strftime('%d/%m'))
    #     start_date += datetime.timedelta(days=1)

    #points will be set to true when we are ready to calculate points for top 25 standings 
    points = False
    formatted_date_counter = 0
    #This loops through every day of the season
    looping_date = START_DATE
    while looping_date < TODAY:
        #Gets the date into the format we need it in
        formatted_date = looping_date.strftime("%d/%m")
        year = looping_date.year
        

        #We set points to true once week 4 hits
        if week_no == 4:
            points = True
        #Checks to see if we need to update the top 25 stnadings
        if formatted_date in top25Dates:
            formatted_date_counter+=1
            #Creates a new top 25
            top_25 = []
            top25 = generateTop25(
                top_25_id, top_25, rosters, week_no, output_file, points
            )

            #Updates the varaibles we need for url work
            top_25_id += 1
            top_25_counter += 1
            week_no += 1
        
        #Gets the date into a url format
        url_date = f"{base_url}{formatted_date}/all-conf"
        response = requests.get(f"https://sports.yahoo.com/college-basketball/scoreboard/?confId=all&schedState=2&dateRange={year}-{looping_date.strftime('%m')}-{looping_date.strftime('%d')}")
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, "html.parser")
            scoreboard = soup.find('div', id="scoreboard-group-2")
            games = scoreboard.find_next('ul').find_all('li')
            for game in games[::3]:
                teams = game.find_all('li',class_='team')
                count = 0
                for team in teams:
                    if count ==0:
                        divs = team.find_all('div')
                        away_team = text_without_numbers = re.sub(r'\(\d+\)', '', divs[2].text).strip()
                        away_score = int(divs[4].text.strip())
                        count +=1
                    else:
                        divs = team.find_all('div')
                        home_team = text_without_numbers = re.sub(r'\(\d+\)', '', divs[2].text).strip()
                        home_score = int(divs[4].text.strip())
                winner = away_team if away_score > home_score else home_team
                loser = home_team if away_team == winner else away_team
                if winner in team_mappings:
                    winner = team_mappings[winner]
                if loser in team_mappings:
                    loser = team_mappings[loser]
                #Makes sure winner is drafted by one of us 
                # print(f"winner: {winner}")
                # print(f"loser: {loser}")
                # print(f"home team: {home_team}")
                # print(f"away team: {away_team}")
                # print("")
                if winner in DRAFTED_TEAMS:
                    #Calculates points for normal win
                    conference = False
                    game_winner(winner, loser, rosters,conference, output_file)
                    #Awards points if the team that lost is in the top 25
                    if loser in top25:
                        top_25_win(winner, loser, rosters, output_file)
                    #Awards points for a road conference win 
                    if winner == away_team:
                        if loser in conferences_dict[teamsConference[winner]]:
                            conference = True
                            game_winner(winner, loser, rosters, conference, output_file)
                # else:
                    # print("CANT FIND TEAM")
                    # print(winner)
        else:
            print(
                "Failed to retrieve the web page. Status code:",
                response.status_code,
                file=output_file,
            )
        looping_date += datetime.timedelta(days=1)
    print(formatted_date_counter)


def game_winner(winner, loser, rosters,  conference, output_file):
    #Loops through our roster to add points to correct team
    for roster in TEAM_NAMES:
        if winner in rosters[roster]:
            #Adds bonus points for a conference win
            if conference:
                print(
                    f"{roster} had {winner} who won on the road against {loser}... One and a half Point awarded",
                    file=output_file,
                )
                SCORES[roster] = SCORES[roster] + 1.5
            #Adds points for win
            else:
                print(
                    f"{roster} had {winner} who beat {loser}... One Point awarded",
                    file=output_file,
                )
                SCORES[roster] = SCORES[roster] + 1


def top_25_win(winner, loser, rosters, output_file):
    #Loops through our teams to add points to right team for a top 25 win
    for roster in TEAM_NAMES:
        if winner in rosters[roster]:
            print(
                f"{roster} had {winner} who beat {loser} who was ranked in top 25... Five Points awarded",
                file=output_file,
            )
            value = SCORES[roster]
            newValue = value + 5
            SCORES[roster] = newValue


# Define the main function that calls my_function
def main():
    #Opens scores.txt file to write to
    with open("scores.txt", "w") as output_file:
        #Sets score to zero
        print("Set scores to 0", file=output_file)
        initialze_score(output_file)
        print("Generating Scores", file=output_file)

        #Creates our teams
        teams = generateTeams()

        #Generates the score 
        generateScore(teams, output_file)
        print(SCORES, file=output_file)


# Check if this script is the main program (not imported as a module)
if __name__ == "__main__":
    main()
