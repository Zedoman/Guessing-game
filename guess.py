from random import randint
from players import Player

#================           Set player objects        =============================

print ("Player 1")
player1=Player(input("Enter name:"))

print ("Player 2")
player2=Player(input("Enter name:"))

#==========               Play single game function     ============================

def playGame():
  randNum = randint(1,100)
  play = True
  print "\nNew game"
  
  while play:
    play=player1.enterGuess(randNum, play)
    play=player2.enterGuess(randNum, play)
  
  print ("\nScore: "+player1.name+" "+str(player1.score)+" | "+player2.name+" "+str(player2.score))  
  
#=====================       Game play section               ===============================

quit = False
while quit != True:
  playGame()
  keepPlaying=input("\nDo you want to quit (y/n): ")
  if keepPlaying == "y":
    quit = True
    
print ("\nFinal Score: "+player1.name+" "+str(player1.score)+" | "+player2.name+" "+str(player2.score))     
  
  
