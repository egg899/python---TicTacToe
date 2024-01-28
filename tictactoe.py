numsBoard = [[1,2,3],[4,5,6],[7,8,9]]
def createBoard():

    for i in range(3):
        print('------') 
        for j in range(3):
            
            print(numsBoard[i][j], end="|")
            
        print('') 
        
    print('------') 




createBoard()

circle = "O"
cross = "X"
player1 = ""
player2 = ""
turn = input("Select circle or cross ")

if turn.lower() == "circle":
    turn = circle
if turn.lower() == "cross":
    turn = cross
player1 = turn
player2 = turn

if player1 == circle:
    player2 = cross
    
if player1 == cross:
    player2 = circle






arr1=[]
arr2 =[]


def modify(num, sign):
    
    if num == 1:
        numsBoard[0][0] = sign
        if sign == 'X':
            arr1.append(1)
        if sign == 'O':
            arr2.append(1)
        
    if num == 2:
        numsBoard[0][1] = sign
        if sign == 'X':
            arr1.append(2)
        if sign == 'O':
            arr2.append(2)
        
    if num == 3:
        numsBoard[0][2] = sign
        if sign == 'X':
            arr1.append(3)
        if sign == 'O':
            arr2.append(3)
        
        
    if num == 4:
        numsBoard[1][0] = sign
        if sign == 'X':
            arr1.append(4)
        if sign == 'O':
            arr2.append(4)

    if num == 5:
        numsBoard[1][1] = sign
        if sign == 'X':
            arr1.append(5)
        if sign == 'O':
            arr2.append(5)

    if num == 6:
        numsBoard[1][2] = sign
        if sign == 'X':
            arr1.append(6)
        if sign == 'O':
            arr2.append(6)
        
    if num == 7:
        numsBoard[2][0] = sign
        if sign == 'X':
            arr1.append(7)
        if sign == 'O':
            arr2.append(7)

            
    if num == 8:
        numsBoard[2][1] = sign
        if sign == 'X':
            arr1.append(8)
        if sign == 'O':
            arr2.append(8)

                
    if num == 9:
        numsBoard[2][2] = sign
        if sign == 'X':
            arr1.append(9)
        if sign == 'O':
            arr2.append(9)
        
    




names = ["Player 1","Player 2"]
players = [player1, player2]
rounds_played = 0
max_rounds = 9

grouped_arr1=[]
grouped_arr2=[]

 



def take_turn(player):
    print(f"It's {player}'s turn")
    
    

#def check_winner(arr, win_map):
  #  for row in arr:
 #       if row in win_map:
#             return row
            
        
    #return None
#winMap = [123, 456, 789, 147, 258, 369, 357, 159]
winMap = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [3,5,7], [1,5,9]]
#def check_winner(player_moves):
#    for win_combo in winMap:
##        if all(move in player_moves for move in str(win_combo)):
##            return True
#    return False    
def check_winner(player_moves, win):
    for win_combo in win:
        if(set(win_combo).intersection(set(player_moves)) == set(win_combo)):
            return True
    return False    



while rounds_played < max_rounds:
    
    #for i in range(0,len(arr1), 3):
     #   group = arr1[i:i+3]
     #   grouped_arr1.append(group)

    #for i in range(0,len(arr2), 3):
       # group = arr2[i:i+3]
       # grouped_arr2.append(group)
   
   # winner_row_arr1 = check_winner(grouped_arr1, winMap)
   # winner_row_arr2 = check_winner(grouped_arr2, winMap)
    
   # if winner_row_arr1 is not None:
        #print(f"Player 1 wins with row: {winner_row_arr1}")
    #    break
            
            
   # if winner_row_arr2 is not None:
        #print(f"Player 2 wins with row: {winner_row_arr2}")
   #     break
                
   if check_winner(arr1, winMap):
        #print("Player 1 wins!!!")
        break
        
   if check_winner(arr2, winMap):
        #print("Player 2 wins!!!")
        break
        
   elif(rounds_played == max_rounds) and (check_winner(arr2, winMap)==False and check_winner(arr1, winMap)== False):
        print("It's a tie dude")
        
        
   for i in range(2):
        
            
        take_turn(names[i])
        
        
        
        
        
        
        while True:
            try:
                play = int(input('add a number between 1 and 9: '))
                row = (play - 1) // 3
                col = (play -1) % 3



                if 1 <= play <= 9 and numsBoard[row][col] not in ["X", "O"]:
                    break
                else:
                    print("Invalid choice. Please choose an available box.")
            except ValueError:
                print("Invalid input. Please enter an number between 1 and 9.")
                                                     
                


        
        
        modify(play, players[i])    
        
        createBoard()
         
        #for i in range(0,len(arr1), 3):
          #  group = arr1[i:i+3]
         #   grouped_arr1.append(group)

        #for i in range(0,len(arr2), 3):
          #  group = arr2[i:i+3]
         #   grouped_arr2.append(group)

        #winner_row_arr1 = check_winner(grouped_arr1, winMap)
        #winner_row_arr2 = check_winner(grouped_arr2, winMap)

        #if winner_row_arr1 is not None:
          #  print(f"Player 1 wins with row: {winner_row_arr1}")
         #   break
            
            
        #if winner_row_arr2 is not None:
       #     print(f"Player 2 wins with row: {winner_row_arr2}")
      #      break
        
        if check_winner(arr1, winMap):
            print("Player 1 wins!!!")
            break
        
        if check_winner(arr2, winMap):
            print("Player 2 wins!!!")
            break
        
        elif(rounds_played == max_rounds) and (check_winner(arr2, winMap)==False and check_winner(arr1, winMap)== False):
            print("It's a tie dude")
        #else:
         #   print(check_winner(arr2, winMap), check_winner(arr2, winMap))
         #   print(rounds_played)
        rounds_played += 1
        
        if(rounds_played == max_rounds):
            break
        
        
        
#print(winner_row_arr1)
#print(winner_row_arr2)
#if (winner_row_arr1 is None and winner_row_arr2 is None) and rounds_played == max_rounds :
  #  print("No winner. It's a tie.")
        
#if check_winner(arr1):
 #   print("Player 1 wins!!!")
#if check_winner(arr2):
 #   print("Player 2 wins!!!")
#else:
 #   print("It's a tie dude")
print('arr1',arr1)
print('arr2', arr2)
#print('arr1',grouped_arr1)
#print('arr2', grouped_arr2)
    


            
            



        
#print(numsBoard)            
    





 
