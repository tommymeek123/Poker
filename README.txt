Western Carolina University
CS352 - Organization of Programming Languages
Project 4: Functional Programming
Tommy Meek
April, 2020

To run this program, navigate to the main directory and type the following: 
python3 poker/driver.py

This program simulates a game of 5 Card Draw. Two hands are dealt, one for you 
and one for your computer opponent. After the hands are dealt, you will be given 
the opportunity to discard as many of your cards as you wish and replace them 
with new cards from the deck. User input should be the indices of the unwanted 
cards separated by spaces. After this, your hand will be compared to the 
computer's hand and a winner will be determined based on standard hand rankings 
in 5 card poker variants. If your hand is of the same rank as your opponent's, 
the winner will be the player who has the highest value card. In this game, an 
Ace only counts as 'high' not 'low'. A straight may not be formed with Ace, Two, 
Three, Four, Five.\

All of the functions which fulfill the requirements of this project are 
in the funcy.py module except for reduce which is in the poker_io module.