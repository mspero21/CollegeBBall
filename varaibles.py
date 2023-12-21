drafted_teams = [
    "Duke",
    "Kentucky",
    "USC",
    "TCU",
    "Saint Mary's",
    "St. John's",
    "Indiana",
    "Texas Tech",
    "Missouri",
    "Georgetown",
    "VCU",
    "Michigan",
    "Purdue",
    "Marquette",
    "Houston",
    "Texas A&M",
    "North Carolina",
    "Maryland",
    "Auburn",
    "Mississippi State",
    "Oregon",
    "Clemson",
    "Rutgers",
    "Duquesne",
    "Michigan State",
    "Arizona",
    "Texas",
    "UConn",
    "San Diego State",
    "Wisconsin",
    "Virginia",
    "Kansas State",
    "Dayton",
    "Providence",
    "Oklahoma",
    "Tulane",
    "Kansas",
    "Florida Atlantic",
    "Gonzaga",
    "Miami",
    "Alabama",
    "Villanova",
    "Ohio State",
    "UCLA",
    "Florida",
    "Iowa State",
    "Boise State",
    "Oklahoma State",
    "Tennessee",
    "Baylor",
    "Creighton",
    "Arkansas",
    "Illinois",
    "Colorado",
    "Memphis",
    "Xavier",
    "New Mexico",
    "Northwestern",
    "St. Bonaventure",
    "Ole Miss",
]

team_mappings = {
    "Michigan State": "Michigan State",
    "Florida Atlantic": "Florida Atlantic",
    "Miami (FL)": "Miami",
    "USC": "USC",
    "Saint Mary's": "Saint Mary's",
    "Connecticut": "UConn",
    "James Madison": "James Madison",
    "Mississippi State": "Mississippi State",
    "Kansas St." : "Kansas State",
    "BYU": "BYU",
    "Colorado State": "Colorado State",
    "Mississippi" : "Ole Miss"
}

new_mappings = {
    "Ohio St." : "Ohio State",
    "Fla. Atlantic": "Florida Atlantic",
    "Mississippi St." : "Mississippi State",
    "Colorado St."    :  "Colorado State",
    "Mississippi" : "Ole Miss"
}

conferences_dict = {
    "Big 12": [
        "Kansas",
        "Kansas State",
        "Texas",
        "Texas Tech",
        "Baylor",
        "Oklahoma",
        "Oklahoma State",
        "Iowa State",
        "TCU",
        "West Virginia",
    ],
    "Big East": [
        "Marquette",
        "Creighton",
        "UConn",
        "Villanova",
        "St. John's",
        "Xavier",
        "Providence",
        "Seton Hall",
        "Georgetown",
        "Butler",
        "Depaul",
    ],
    "SEC": [
        "Tennessee",
        "Texas A&M",
        "Kentucky",
        "Florida",
        "Auburn",
        "Alabama",
        "Arkansas",
        "Mississippi State",
        "Missouri",
        "Ole Miss",
        "LSU",
        "Georgia",
        "South Carolina",
    ],
    "ACC": [
        "Duke",
        "North Carolina",
        "Virginia",
        "Miami",
        "Clemson",
        "NC State",
        "Wake Forest",
        "Pitt",
        "Syracuse",
        "FSU",
        "Boston College",
        "Georgia Tech",
        "Louisville",
        "Notre Dame",
    ],
    "PAC": [
        "Arizona",
        "USC",
        "Colorado",
        "UCLA",
        "Oregon",
        "Stanford",
        "Utah",
        "Washington",
        "California",
        "Arizona St",
        "Washington St",
        "Oregon State",
    ],
    "AAC": [
        "Florida Atlantic",
        "Memphis",
        "UAB",
        "Tulane",
        "Wichita St",
        "USF",
        "Charlotte",
        "Temple",
        "SMU",
        "East Carolina",
        "Houston",
        "UCF",
        "Cincinnati",
        "Tulsa",
    ],
    "WCC": [
        "Gonzaga",
        "Saint Mary's",
        "San Fran",
        "Santa Clara",
        "Loyola Marymount",
        "Portland",
        "Pepperdine",
        "San Diego",
        "BYU",
    ],
    "Mountain West": [
        "San Diego State",
        "New Mexico",
        "Boise State",
        "Colorado State",
        "Nevada",
        "UNLV",
        "Utah St",
        "Fresno St",
        "Wyoming",
    ],
    "A10": [
        "George Mason",
        "UMass",
        "Dayton",
        "George Washington",
        "La Salle",
        "Saint Joseph's",
        "Duquesne",
        "St. Bonaventure",
        "Davidson",
        "Loyola Chicago",
        "Rhode Island",
        "Richmond",
        "Saint Louis",
        "Fordham",
        "VCU",
    ],
    "Big 10": [
        "Michigan",
        "Michigan State",
        "Ohio State",
        "Wisconsin",
        "Indiana",
        "Purdue",
        "Maryland",
        "Rutgers",
        "Iowa",
        "Minnesota",
        "Northwestern",
        "Nebraska",
        "Penn State",
        "Illinois",
    ],
}


teamsConference = {
    "Kansas": "Big 12",
    "Kansas St": "Big 12",
    "Texas": "Big 12",
    "Texas Tech": "Big 12",
    "Baylor": "Big 12",
    "Oklahoma": "Big 12",
    "OK State": "Big 12",
    "Iowa St": "Big 12",
    "TCU": "Big 12",
    "West Virginia": "Big 12",
    "Marquette": "Big East",
    "Creighton": "Big East",
    "UConn": "Big East",
    "Villanova": "Big East",
    "St Johns": "Big East",
    "Xavier": "Big East",
    "Providence": "Big East",
    "Seton Hall": "Big East",
    "Georgetown": "Big East",
    "Butler": "Big East",
    "Depaul": "Big East",
    "Tennessee": "SEC",
    "Texas A&M": "SEC",
    "Kentucky": "SEC",
    "Florida": "SEC",
    "Auburn": "SEC",
    "Alabama": "SEC",
    "Arkansas": "SEC",
    "Mississippi St": "SEC",
    "Missouri": "SEC",
    "Ole Miss": "SEC",
    "LSU": "SEC",
    "Georgia": "SEC",
    "South Carolina": "SEC",
    "Duke": "ACC",
    "UNC": "ACC",
    "Virginia": "ACC",
    "Miami": "ACC",
    "Clemson": "ACC",
    "NC State": "ACC",
    "Wake Forest": "ACC",
    "Pitt": "ACC",
    "Syracuse": "ACC",
    "FSU": "ACC",
    "Boston College": "ACC",
    "Georgia Tech": "ACC",
    "Louisville": "ACC",
    "Notre Dame": "ACC",
    "Arizona": "PAC",
    "USC": "PAC",
    "Colorado": "PAC",
    "UCLA": "PAC",
    "Oregon": "PAC",
    "Stanford": "PAC",
    "Utah": "PAC",
    "Washington": "PAC",
    "California": "PAC",
    "Arizona St": "PAC",
    "Washington St": "PAC",
    "Oregon St": "PAC",
    "FAU": "AAC",
    "Memphis": "AAC",
    "UAB": "AAC",
    "Tulane": "AAC",
    "Wichita St": "AAC",
    "USF": "AAC",
    "Charlotte": "AAC",
    "Temple": "AAC",
    "SMU": "AAC",
    "East Carolina": "AAC",
    "Houston": "AAC",
    "UCF": "AAC",
    "Cincinnati": "AAC",
    "Tulsa": "AAC",
    "Gonzaga": "WCC",
    "St Mary's": "WCC",
    "San Fran": "WCC",
    "Santa Clara": "WCC",
    "Loyola Marymount": "WCC",
    "Portland": "WCC",
    "Pepperdine": "WCC",
    "San Diego": "WCC",
    "BYU": "WCC",
    "SDSU": "Mountain West",
    "New Mexico": "Mountain West",
    "Boise St": "Mountain West",
    "Colorado St": "Mountain West",
    "Nevada": "Mountain West",
    "UNLV": "Mountain West",
    "Utah St": "Mountain West",
    "Fresno St": "Mountain West",
    "Wyoming": "Mountain West",
    "Dayton": "A10",
    "VCU": "A10",
    "Duquesne": "A10",
    "Richmond": "A10",
    "Davidson": "A10",
    "St Joe's": "A10",
    "SLU": "A10",
    "George Mason": "A10",
    "URI": "A10",
    "UMass": "A10",
    "Fordham": "A10",
    "GW": "A10",
    "La Salle": "A10",
    "Michigan": "Big 10",
    "Michigan St": "Big 10",
    "Ohio State": "Big 10",
    "Wisconsin": "Big 10",
    "Indiana": "Big 10",
    "Purdue": "Big 10",
    "Maryland": "Big 10",
    "Rutgers": "Big 10",
    "Iowa": "Big 10",
    "Minnesota": "Big 10",
    "Northwestern": "Big 10",
    "Nebraska": "Big 10",
    "Penn State": "Big 10",
    "Illinois": "Big 10",
}


def create_team_to_conference_dict():
    team_to_conference_dict = {}
    for conference, teams in conferences_dict.items():
        for team in teams:
            team_to_conference_dict[team] = conference
    return team_to_conference_dict


# Use the function to create the new dictionary
team_to_conference = create_team_to_conference_dict()
