game_dictionary = {}

def game_dict():
    home_player1 = {'number':0 ,'shoe':16 , 'points':22 ,'rebounds':12 , 'assists':12 , 'steals':3 ,'blocks': 1, 'slam_dunks': 1}
    home_player2 = {'number':30 ,'shoe':14 , 'points':12 ,'rebounds':12 , 'assists':12 , 'steals':12 ,'blocks':12 , 'slam_dunks': 7}
    home_player3 = {'number':11 ,'shoe':17 , 'points':17 ,'rebounds':19 , 'assists':10 , 'steals':3 ,'blocks':1 , 'slam_dunks': 15}
    home_player4 = {'number':1 ,'shoe':19 , 'points':26 ,'rebounds':12 , 'assists':6 , 'steals':3 ,'blocks':8 , 'slam_dunks': 5}
    home_player5 = {'number':31 ,'shoe':15 , 'points':19 ,'rebounds':2 , 'assists':2 , 'steals':4 ,'blocks':11 , 'slam_dunks': 1}

    away_player1 = {'number': 4,'shoe': 18, 'points': 10,'rebounds': 1, 'assists': 1, 'steals': 2,'blocks': 7, 'slam_dunks': 2}
    away_player2 = {'number': 0,'shoe': 16, 'points': 12,'rebounds': 4, 'assists': 7, 'steals': 7,'blocks': 15, 'slam_dunks': 10}
    away_player3 = {'number': 2,'shoe': 14, 'points': 24,'rebounds': 12, 'assists': 12, 'steals': 4,'blocks': 5, 'slam_dunks': 5}
    away_player4 = {'number': 8,'shoe': 15, 'points': 33,'rebounds': 3, 'assists': 2, 'steals': 1,'blocks': 1, 'slam_dunks': 0}
    away_player5 = {'number': 33,'shoe': 15, 'points': 6,'rebounds': 12, 'assists': 12, 'steals': 22,'blocks': 5, 'slam_dunks': 12}

    game_dictionary = {
        'home': {'team_name':'Brooklyn Nets','colors':['Black', 'White'],'players':{'Alan Anderson' : home_player1, 'Reggie Evans' : home_player2, 'Brook Lopez' : home_player3, 'Mason Plumlee' : home_player4, 'Jason Terry' : home_player5}},
        'away': {'team_name':'Charlotte Hornets','colors':['Purple'],'players':{'Jeff Adrien' : away_player1, 'Bismak Biyombo' : away_player2, 'DeSagna Diop' : away_player3, 'Ben Gordon' : away_player4, 'Brendan Haywood' : away_player5}}
    }

    return game_dictionary

game_dictionary = game_dict()












def list_of_players(game_dictionary):
    return list(game_dictionary['home']['players']) + list(game_dictionary['away']['players'])



def home_team_name():
  return game_dict()['home']['team_name']



def away_team_name():
  return game_dict()['away']['team_name']




def home_players(game_dictionary):
    return list(game_dictionary['home']['players'])



def away_players(game_dictionary):
    return list(game_dictionary['away']['players'])



#6

def find_player_dict(name, game_dictionary):
    
    if name in home_players(game_dictionary):
        
        return game_dictionary['home']['players'][name]
    
    elif name in away_players(game_dictionary):
        
        return game_dictionary['away']['players'][name]
    
    
    
def is_home_away(team_name):
    if game_dict()['home']['team_name']==team_name:
        return 'home'
    elif game_dict()['away']['team_name']==team_name:
        return 'away'
    else: 
        return None
    
    
    
#1 
def num_points_scored(name):
    return find_player_dict(name, game_dictionary)['points']

#2
def shoe_size(name):
    return find_player_dict(name, game_dictionary)['shoe']

#3

def team_colors(team_name):
    return game_dict()[is_home_away(team_name)]['colors']

#4

def team_names():
    return [game_dict()['home']['team_name']] + [game_dict()['away']['team_name']]



def jersey_number(team_name):
    
    jnums=[]
    players = away_players(game_dictionary)
    
    if team_name == game_dictionary['home']['team_name']:
        players = home_players(game_dictionary)
    
    
    return list(map(lambda player: find_player_dict(player, game_dictionary)['number'], players))



#6
def player_stats(name):
    
    return find_player_dict(name, game_dictionary)




def big_shoe_rebounds(players):
    player_and_shoes = []
    shoe_size = []
    
    
    for player in players:
        player_and_shoes.append([player, player_stats(player)['shoe'], player_stats(player)['rebounds']])
        shoe_size.append(player_stats(player)['shoe'])
    
    big_shoe_reb = list(filter(lambda p: p[1]==max(shoe_size), player_and_shoes))
    
    return print(list(map(lambda p: 'Player {} has a shoe size of {} and has {} rebounds.'.format(p[0], p[1], p[2]), big_shoe_reb)))
    


    
def most_points_scored(players):
    player_and_points = []
    points = []
    
    for player in players:
        player_and_points.append([player, player_stats(player)['points']])
        points.append(player_stats(player)['points'])
    
    top_points = list(filter(lambda p: p[1]==max(points), player_and_points))
    
    return print(list(map(lambda p: 'Player {} has the top point score of {}.'.format(p[0], p[1]), top_points)))



def sum_numeric_stat(stat, team_name, game_dictionary):
    
    home_or_away = is_home_away(team_name)
    players = []
    
    if type(stat) != str:
        return("This function only sums numbers.")
    
    if home_or_away == 'home':
        players = home_players(game_dictionary)
    
    elif home_or_away == 'away':
        players = away_players(game_dictionary)
    
    return sum(list(map(lambda player: game_dictionary[home_or_away]['players'][player][stat], players)))



def winning_team(game_dictionary):
    home_score = sum_numeric_stat('points', home_team_name(), game_dictionary)
    away_score = sum_numeric_stat('points', away_team_name(), game_dictionary)
    
    if home_score > away_score:
        return home_team_name()
    elif home_score < away_score:
        return away_team_name()
    else:
        return 'tie'
    
    
def player_with_longest_name(players):
    player_and_char = []
    chars = []
    
    for player in players:
        player_and_char.append([player, len(player)-1])
        chars.append(len(player)-1)
    
    return list(filter(lambda p: p[1]==max(chars), player_and_char))





def find_top_steals(players):
    player_and_steals = []
    steals = []
    
    for player in players:
        player_and_steals.append([player, player_stats(player)['steals']])
        steals.append(player_stats(player)['steals'])
    
    top_steals = list(filter(lambda p: p[1]==max(steals), player_and_steals))
    
    return top_steals




def long_name_steals_a_ton(players):
    max_steals= find_top_steals(players)[0][1]
    max_length= player_with_longest_name(players)[0][1]+1
    
    for player in players:
        if len(player)== max_length and find_player_dict(player, game_dictionary)['steals']==max_steals:
            
            return True
        
    else:
        return False
