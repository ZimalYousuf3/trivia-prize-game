def play_game():

  print('WELCOME TO THE GAME! \n')
  questions = [
    " 1. In Harry Potter and the Sorcerer's Stone, what position does Harry play on the Gryffindor Quidditch team?\n a) Beater \t b) Chaser \n c) Seeker \t d) Keeper \n ",
    " 2. Which Taylor Swift album features the hit tracks 'Blank Space' and 'Shake It Off'? \n a) Red \t b) 1989 \n c) Lover \t d) Reputation \n ",
    " 3. In the iconic Bollywood film DDLJ, in which European country do Raj and Simran first meet during their train trip? \n a) Switzerland\t b) France \n c) Italy \t d) Germany \n ",
    " 4. Which Taylor Swift song from 1989 features a clip of an actual heart monitor beating sampled in the background track? \n a) Style \t b) Wildest Dreams \n c) Blank Space\t d) Out of the Woods \n  ",
    " 5. In the epic Season 3 finale, Dustin and his girlfriend Suzie sing a duet of which song over the radio to get Planck's Constant? \n a) Material Girl \t b) Take On Me \n c) NeverEnding Story \t d) Should I Stay or Should I Go \n "
]
  answers = ['c', 'b', 'a', 'b', 'c' ]
  prize = [10000, 20000, 50000, 150000, 500000]
  prize_money = 0

  for i, question in enumerate(questions):
    print(question)
    ans = input('Enter the correct option(a,b,c,d): ').strip().lower()

    while ans not in ['a', 'b', 'c', 'd']:
      print('Invalid Option!')
      ans = input('Enter the correct option(a,b,c,d): ').strip().lower()
      
    if ans == answers[i]:
      print('\nCorrect Answer!\n')
      prize_money = prize_money + prize[i]
      print(f'Current prize money: PKR {prize_money}\n')
      
    else:
      print('\nIncorrect Answer\n')
      break
        
  if prize_money > 0:
    print(f'Congratulations! You have won PKR {prize_money}')
  
  else:
    print('Better Luck Next Time!')

play_game()
