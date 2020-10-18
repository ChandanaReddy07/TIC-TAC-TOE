board={
    '7' : ' ','8':' ','9': ' ',
    '4' : ' ','5':' ','6': ' ',
    '1' : ' ','2':' ','3': ' ',
} 

print("Instruction - enter number according to the cell \n ")
print('7'+' | '+ '8'+' | ' +'9' )
print('- '+'+'+ ' - '+'+' +' -' )
print('4'+' | '+ '5'+' | ' +'6' )
print('- '+'+'+ ' - '+'+' +' -' )
print('1'+' | '+ '2'+' | ' +'3' )
print('\n')



def checkif():
    #horizontal
    if(board['7']==board['8'] and board['7']==board['9'] ):
    
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
        elif(board['7']=='O'):
            print('O won')
            return 1
        
    if(board['1']==board['2'] and board['1']==board['3'] ):
    
        if(board['1']=='X'):
            print("X won")
            return 1
        elif(board['7']=='O'):
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
        elif(board['7']=='O'):
            print('O won')
            return 1
         
    if(board['9']==board['6'] and board['6']==board['3'] ):
    
        if(board['9']=='X'):
            print("X won")
            return 1
        elif(board['7']=='O'):
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
        elif(board['7']=='O'):
            print('O won')
            return 1
         
    return 0
player='X'

total=0  
#gamemain
print('Lets play!!\n')
while(True):
    print(board['7']+' | '+ board['8'] +' | ' + board['9'] )
    print('- '+'+'+ ' - '+'+' +' -' )
    print(board['4']+' | '+ board['5'] +' | ' + board['6'])
    print('- '+'+'+ ' - '+'+' +' -' )
    print(board['1']+' | '+ board['2']+' | ' + board['3'] )
    print('***********************************************************')
    chking=checkif()
    
       
    if total==9 and chking!=1 :
        print("Boom** it's a Tie!!")
        break
    if( total==9 or chking==1):
        restart = input("Do want to play Again?(1)")
        if restart == 1 :
            for key in "123456789":
                board[key] = ' '
        else:
            break

       
    while True:
        
        player_input=input(f'enter ur place {player}\n',)
        if player_input in board and board[player_input]==' ':
            board[player_input]=player
            total+=1
            if player =='X':
                player='O'
            else:
                player='X'
            break
        else:
            print('enter a valid num')
            continue
    
            
        
        




               

    




