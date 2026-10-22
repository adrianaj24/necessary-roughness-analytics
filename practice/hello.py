import scoring

# print( "Necessary Roughness Analytics")
# print(5 + 3)
# print("5 + 3")
# print ("5" + str(3))
# print(int("5") + int("3"))

# touchdowns = 3 
# points_per_touchdown = 6 

# print(touchdowns * points_per_touchdown)

# rushing_yards = 85 
# touchdowns = 2 
# points_per_ten_rushing_yards = 1 
# points_per_touchdown = 6 
# best_rb_in_the_planet = "Bijan Robinson"

# rushing_points = rushing_yards / 10 * points_per_ten_rushing_yards
# print(rushing_points)

# td_points = touchdowns * points_per_touchdown
# print(td_points)

# total_points = rushing_points + td_points
# print(total_points)

# print(f"{best_rb_in_the_planet} scored {total_points} fantasy points!")

# outstanding = 20 
# good = 10 
 
# if total_points >= outstanding:
#     print(f"Outstanding Performance by {best_rb_in_the_planet} with {total_points} fanstasy points")
# elif total_points >= good:
#     print(f"Good Performance by {best_rb_in_the_planet} with {total_points} fanstasy points")
# else: 
#     print(f"Disappointing Performance by {best_rb_in_the_planet} with {total_points} fanstasy points")


# projected_points = 12
# starter_points = 20
# is_superstar = True
# is_healthy = True

# if (projected_points >= starter_points or is_superstar) and is_healthy: 
#     print(f"START HIM!")
# else:
#     print(f"BENCH HIM!")



# aj_points = scoring.calculate_receiving_points(95, 2, 7)  
# print(f"AJ BROWN scored: {aj_points} fantasy points!")


# bijan_points = scoring.calculate_rushing_points(110, 2) + scoring.calculate_receiving_points(45, 0, 4)
# print(f"Bijan Robinson scored {bijan_points} fantasy points!")

# rushing_yards = [110, 85, 142]

# for each_game in rushing_yards:
#     print(scoring.calculate_rushing_points(each_game, 1 ))

# scoring.calculate_rushing_points()

players = [
    {"name": "Bijan Robinson", "position": "RB", "rushing_yards": 110},
    {"name": "AJ Brown", "position": "WR", "rushing_yards": 0},
    {"name": "Ashton Jeanty", "position": "RB", "rushing_yards": 85}
]

# for player in players: 
#     if player["position"] == "RB":
#       print(f"{player["name"]}: {player["rushing_yards"]} rushing yards")



# running_backs = []

# for running_back in players: 
#    if running_back["position"] == "RB":
#       running_backs.append(running_back)
      
# print(running_backs)

# wide_receivers = []

# for receiver in players: 
#    if receiver["position"] == "WR":
#       wide_receivers.append(receiver['name'])
      
# print(wide_receivers)

players = [
    {"name": "Bijan Robinson", "rushing_yards": 110, "touchdowns": 2},
    {"name": "Ashton Jeanty", "rushing_yards": 85, "touchdowns": 1}
]

player_scores = []

for player in players:
    if player[""]