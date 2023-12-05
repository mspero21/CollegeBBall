import requests
import datetime
import json
from bs4 import BeautifulSoup
from varaibles import drafted_teams, team_mappings, teamsConference, conferences_dict
import re

# Send an HTTP GET request to the URL

SCORES = {}
TODAY = datetime.date.today()
TEAM_NAMES = ["Dunne", "Jack", "Mike", "Silv", "Sully"]
DRAFTED_TEAMS = drafted_teams
TEAM_MAPPINGS = team_mappings
START_DATE = datetime.date(2023, 11, 6)

TOP_25_DATES = []
# found_teams = []
# missing_teams = []


def generateTop25Dates():
    start_date = datetime.datetime.strptime("2023/11/06", "%Y/%m/%d")
    TOP_25_DATES.append(start_date.strftime("%Y/%m/%d"))
    for i in range(25):
        start_date += datetime.timedelta(days=7)
        TOP_25_DATES.append(start_date.strftime("%Y/%m/%d"))
    print(TOP_25_DATES)


def initialze_score(output_file):
    for name in TEAM_NAMES:
        SCORES[name] = 0
    print(SCORES, file=output_file)


def generateTeams():
    # Attempt to open rosters file
    with open("rosters.json", "r") as json_file:
        # load data into json_data object
        rosters = json.load(json_file)
        print(rosters)

    if "TCU" in rosters["Dunne"]:
        print("Rosters successfully created")
        return rosters
    else:
        print("Rosters unsucusfully created")
        exit()


def generateTop25(id, top_25, rosters, week_no, output_file, points):
    top_25 = []
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
        for num in range(8, 33):
            team_rows = rows[num].find_all("td")
            team = team_rows[2].text
            team_final_unstripped = re.sub(r"\s*\([^)]*\)", "", team)
            team_final = team_final_unstripped.strip()
            if team_final not in DRAFTED_TEAMS:
                team_final = team_mappings[team_final]
            top_25.append(team_final)
            if points:
                if val < 26:
                    if val == 1:
                        if team_final in DRAFTED_TEAMS:
                            for name in TEAM_NAMES:
                                if team_final in rosters[name]:
                                    SCORES[name] = SCORES[name] + 1 d
                                    print(
                                        f"{name} has {team_final} who is ranked No. 1 for week {week_no}...1 point awarded",
                                        file=output_file,
                                    )
                    if val < 16:
                        if team_final in DRAFTED_TEAMS:
                            for name in TEAM_NAMES:
                                if team_final in rosters[name]:
                                    SCORES[name] = SCORES[name] + 3
                                    print(
                                        f"{name} has {team_final} who is ranked No. {val} for week {week_no}.....3 points awarded",
                                        file=output_file,
                                    )
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

    return top_25


def generateGames(rosters, output_file):
    # Define a list to store the formatted date strings
    date_strings = []
    # Create the URL strings
    base_url = "https://www.ncaa.com/scoreboard/basketball-men/d1/"
    top_25_counter = 0
    top_25_id = 1260
    top_25 = []
    # Loop through dates
    week_no = 1
    points = False
    looping_date = START_DATE
    while looping_date <= TODAY:
        formatted_date = looping_date.strftime("%Y/%m/%d")
        if week_no == 4:
            points = True
        if formatted_date in TOP_25_DATES:
            top_25 = []
            top25 = generateTop25(
                top_25_id, top_25, rosters, week_no, output_file, points
            )
            top_25_id += 1
            top_25_counter += 1
            week_no += 1

        # date_strings.append(formatted_date)
        # Increment the current_date by one day
        url_date = f"{base_url}{formatted_date}/all-conf"
        print(f"Scoring games from this link: {url_date}", file=output_file)
        response = requests.get(url_date)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, "html.parser")
            games = soup.find("div", class_="gamePod_content-pod_container").find_all(
                "div", class_="gamePod"
            )
            for game in games:
                if game.find("li", class_="winner") is not None:
                    winner = (
                        game.find("li", class_="winner")
                        .find("span", class_="gamePod-game-team-name")
                        .text
                    )
                    teams = game.find_all("li")
                    home_team = (
                        teams[0].find("span", class_="gamePod-game-team-name").text
                    )
                    away_team = (
                        teams[1].find("span", class_="gamePod-game-team-name").text
                    )
                    loser = home_team if away_team == winner else away_team
                    if winner in DRAFTED_TEAMS:
                        conference = False
                        game_winner(winner, loser, rosters,conference, output_file)
                        if loser in top25:
                            top_25_win(winner, loser, rosters, output_file)
                        if winner == away_team:
                            if teamsConference[winner] == teamsConference[loser]:
                                conference = True
                                game_winner(winner, loser, rosters, conference, output_file)

                        # TO ADD
                        # ROAD CONFERENCE WINS

                        # Uncomment this code to track teams that are being found for debugging purposes
                        # if winner not in found_teams:
                        #     found_teams.append(winner)
                        # if loser not in found_teams:
                        #     found_teams.append(loser)
        else:
            print(
                "Failed to retrieve the web page. Status code:",
                response.status_code,
                file=output_file,
            )
            exit()
        looping_date += datetime.timedelta(days=1)


def game_winner(winner, loser, rosters,  conference, output_file):
    for roster in TEAM_NAMES:
        if winner in rosters[roster]:
            if conference:
                print(
                    f"{roster} had {winner} who won on the road against {loser}... One and a half Point awarded",
                    file=output_file,
                )
                SCORES[roster] = SCORES[roster] + 1.5
            else:
                print(
                    f"{roster} had {winner} who beat {loser}... One Point awarded",
                    file=output_file,
                )
                SCORES[roster] = SCORES[roster] + 1


def top_25_win(winner, loser, rosters, output_file):
    for roster in TEAM_NAMES:
        if winner in rosters[roster]:
            print(
                f"{roster} had {winner} who beat {loser} who was ranked in top 25... Five Points awarded",
                file=output_file,
            )
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
    generateTop25Dates()
    with open("scores.txt", "w") as output_file:
        print("Set scores to 0", file=output_file)
        initialze_score(output_file)
        print("Generating Scores", file=output_file)
        teams = generateTeams()
        print("made team")
        games = generateGames(teams, output_file)
        # TO ADD
        # RANKINGS AFTER WEEK 3
        # CONFERENCE CHAMPS
        # REGULAR SEASON CONFERENCE CHAMPS
        # LAST PLACE FINISH
        # POY
        # Uncomment to find missing teams
        # find_missing_teams(teams)
        print(SCORES, file=output_file)


# Check if this script is the main program (not imported as a module)
if __name__ == "__main__":
    main()
