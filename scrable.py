#This my personal solution to "Scrable" Project in Codecademy included in the Learn Python 3 Course.
#https://www.codecademy.com/courses/learn-python-3/projects/scrabble

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Implementation for lowercase inputs
lower = []
for letter in letters:
  lower.append(letter.lower())
letters += lower
points += points
#Comprehension to convert 2 lists into a dictionary using zip 
letter_to_points = {letter:point for letter, point in zip(letters, points)}

letter_to_points[""]=0

#Function that takes in a word and return how many points it's worth
def score_word(word):
  point_total=0
  for letter in word:
   point_total += letter_to_points.get(letter,0)
  return point_total
#Function that updates the total points of all players
def update_point_totals(player_to_words,player_to_points):
  for player in player_to_words.items():
   player_points=0
   for value in player[1]:
    player_points += score_word(value)
    player_to_points[player[0]]=player_points

#Function to add new words to an existing player
def play_word(player,word):
  if player in player_to_words:
    player_to_words[player].append(word)

#TESTING THE FUNCTIONS:

#Calculating the value of a word both upper and lowercase
brownie_points= "BROWNIE"
print(score_word(brownie_points))
rownie_points= "brownie"
print(score_word(brownie_points))

#Create a new dictionary for testing update_point_totals and play_word functions
player_to_words={"player1":["BLUE","TENNIS","EXIT"],"wordNerd":["EARTH","EYES","MACHINE"],"Lexi Con":["ERASER","BELLY","HUSKY"],"Prof Reader":["ZAP","COMA","PERIOD"]}
player_to_points={}

#Testing update_point_totals and play_word functions
update_point_totals(player_to_words,player_to_points)
print(player_to_points)
play_word("player1", "HELLO")
print(player_to_words)
update_point_totals(player_to_words,player_to_points)
print(player_to_points)
