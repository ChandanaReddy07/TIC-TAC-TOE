print("Instruction - enter number according to the cell \n ")
print('7'+' | '+ '8'+' | ' +'9' )
print('- '+'+'+ ' - '+'+' +' -' )
print('4'+' | '+ '5'+' | ' +'6' )
print('- '+'+'+ ' - '+'+' +' -' )
print('1'+' | '+ '2'+' | ' +'3' )
print('\n')



def checkif(board):
    #horizontal
    if(board['7']==board['8'] and board['7']==board['9']):
    
        if(board['7']=='X'):
            print("X won")
            return 1
        elif(board['7']=='O'):
            print('O won')
            return 1
        
    if(board['4']==board['5'] and board['4']==board['6'] ):
    
        if(board['4']=='X'):
            print("X won")
            return 1
        elif(board['4']=='O'):
            print('O won')
            return 1
        
    if(board['1']==board['2'] and board['1']==board['3'] ):
    
        if(board['1']=='X'):
            print("X won")
            return 1
        elif(board['1']=='O'):
            print('O won')
            return 1
         
    #verticle
    if(board['7']==board['4'] and board['7']==board['1'] ):
    
        if(board['7']=='X'):
            print("X won")
            return 1
        elif(board['7']=='O'):
            print('O won')
            return 1
         
    if(board['8']==board['5'] and board['5']==board['2'] ):
    
        if(board['8']=='X'):
            print("X won")
            return 1
        elif(board['8']=='O'):
            print('O won')
            return 1
         
    if(board['9']==board['6'] and board['6']==board['3'] ):
    
        if(board['9']=='X'):
            print("X won")
            return 1
        elif(board['9']=='O'):
            print('O won')
            return 1
         

    #diagonal
    if(board['7']==board['5'] and board['7']==board['3'] ):
    
        if(board['7']=='X'):
            print("X won")
            return 1
        elif(board['7']=='y'):
            print('O won')
            return 1
         
    if(board['1']==board['5'] and board['9']==board['1'] ):
    
        if(board['1']=='X'):
            print("X won")
            return 1
        elif(board['1']=='O'):
            print('O won')
            return 1
         
    return 0

#againplay
def againplay(board):
    restart = input("Do want to play Again?(yes/no)")
    if restart == 'yes':  
        for key in "123456789":
            board[key] = " "

        play() 

#gamemain
print('Lets play!!\n')
def play():
    #creating a board
    board={
    '7' : ' ','8':' ','9': ' ',
    '4' : ' ','5':' ','6': ' ',
    '1' : ' ','2':' ','3': ' ',
} 

    total=0 
    player='X'
    
    while total<=9:
        print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
        print('- + - + - ')
        print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
        print('- + - + -')

        print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
        cheking_for_winning=checkif(board)
        if(cheking_for_winning==1):
            againplay(board)
            break
        if total == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")
            againplay(board)
            break
        player_input=input(f'enter ur place {player}\n',)
        if player_input in board and board[player_input]==' ':
            board[player_input]=player
            total+=1
           
            if player =='X':
                player='O'
            else:
                player='X'
        else:
            print('enter a valid num')
     

 
#main
        
if __name__ == "__main__":
    play()      
        




               

    







