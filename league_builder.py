# importing csv and random modules for use in script
import csv
import random

# opening csv file with player info
with open('soccer_players.csv') as csvfile:
    teamreader = csv.reader(csvfile, delimiter=',')
    
    # skipping first row in csv file
    next(teamreader, None)
    
    # the script will not execute upon import
    if __name__ == "__main__":
    
        # lists for experienced and inexperienced players
        experienced_players = []
        inexperienced_players = []
        
        # team lists
        Sharks = []
        Dragons = []
        Raptors = []
        
        # separating experienced and inexperienced players
        for line in teamreader:
            player_name = line[0]
            prev_exp = line[2]
            # deleting 'height' from returned data
            del line[1]
            if prev_exp == 'YES':
                experienced_players.append(line)
            else:
                inexperienced_players.append(line)
                
        # using random module to pull 3 player samples from the main experienced
        # player list. executed twice. remaining names are last team
        sharks_exp_rand = random.sample(experienced_players, 3)
        for player_name in sharks_exp_rand:
            experienced_players.remove(player_name)
        raptors_exp_rand = random.sample(experienced_players, 3)
        for player_name in raptors_exp_rand:
            experienced_players.remove(player_name)
        dragons_exp_rand = experienced_players
        
        # using random module to pull 3 player samples from the main inexperienced
        # player list. executed twice. remaining names are last team
        sharks_inexp_rand = random.sample(inexperienced_players, 3)
        for player_name in sharks_inexp_rand:
            inexperienced_players.remove(player_name)
        raptors_inexp_rand = random.sample(inexperienced_players, 3)
        for player_name in raptors_inexp_rand:
            inexperienced_players.remove(player_name)
        dragons_inexp_rand = inexperienced_players
        
        # concatenating the experienced and inexperienced players to 
        # form the final teams
        Sharks = sharks_exp_rand + sharks_inexp_rand
        Raptors = raptors_exp_rand + raptors_inexp_rand
        Dragons = dragons_exp_rand + dragons_inexp_rand
        
        # defining the text blocks that will be used in .write() below
        # how the lines will be formatted - with title of team name
        # followed by a row for each player
        # each player includes their name, experience (YES/NO), guardian(s)
        def team1(Sharks):
            skip = ''
            for i in Sharks:
                skip = (skip + ', '.join(i)) + '\n'
            return 'Sharks' + '\n' + skip + '\n'
        def team2(Raptors):
            skip = ''
            for i in Raptors:
                skip = (skip + ', '.join(i)) + '\n'
            return 'Raptors' + '\n' + skip + '\n'
        def team3(Dragons):
            skip = ''
            for i in Dragons:
                skip = (skip + ', '.join(i)) + '\n'
            return 'Dragons' + '\n' + skip
        
        # writing the text into the teams.txt file
        with open('teams.txt', 'w') as f:
            f.write(team1(Sharks))
            f.write(team2(Raptors))
            f.write(team3(Dragons))
            f.close()
    
            
            
            
            
