import random
import time
_cmp = {'c1':"1", 'c2':"2", 'c3':"3", 'c4':"4", 'c5':"5", 'c6':"6", 'c7':"7", 'c8':"8", 'c9':"9"}
#_cmp['c1'] = "X"
#print(_cmp)

_computervals = {'c1':"1", 'c2':"2", 'c3':"3", 'c4':"4", 'c5':"5", 'c6':"6", 'c7':"7", 'c8':"8", 'c9':"9"}
_uservals = {'c1':"1", 'c2':"2", 'c3':"3", 'c4':"4", 'c5':"5", 'c6':"6", 'c7':"7", 'c8':"8", 'c9':"9"}

win_pattern = ()

print("Welcome to X and O")


def game_env():
    print(_cmp['c1'], end=" ")
    print(_cmp['c2'], end=" ")
    print(_cmp['c3'])

    print(_cmp['c4'], end=" ")
    print(_cmp['c5'], end=" ")
    print(_cmp['c6'])

    print(_cmp['c7'], end=" ")
    print(_cmp['c8'], end=" ")
    print(_cmp['c9'])

def computer_player():
    key_list = []
    for i in _computervals.keys():
        key_list.append(i)
    try:    
        computer_player.rand_key = random.choice(key_list)
        
    except IndexError:
        computer_player.game_draw = True
        print("Game is Draw!")  

input_validate = False
game_env()


def win_cases():
    global run
    if _cmp["c1"] == _cmp["c2"] == _cmp["c3"]:
        if _cmp["c1"] == "X":
            print("You win")
            win_cases.run = False
        else:
            print("You lose")
            win_cases.run = False    
    elif _cmp["c1"] == _cmp["c4"] == _cmp["c7"]:
        if _cmp["c1"] == "X":
            print("You win")
            win_cases.run = False
        else:
            print("You lose")
            win_cases.run = False     
    elif _cmp["c2"] == _cmp["c5"] == _cmp["c8"]:
        if _cmp["c2"] == "X":
            print("You win")
            win_cases.run = False
        else:
            print("You lose")
            win_cases.run = False
    elif _cmp["c3"] == _cmp["c6"] == _cmp["c9"]:
        if _cmp["c3"] == "X":
            print("You win")
            win_cases.run = False
        else:
            print("You lose")
            win_cases.run = False 
    elif _cmp["c4"] == _cmp["c5"] == _cmp["c6"]:
        if _cmp["c4"] == "X":
            print("You win")
            win_cases.run = False
        else:
            print("You lose")
            win_cases.run = False 
    elif _cmp["c7"] == _cmp["c8"] == _cmp["c9"]:
        if _cmp["c7"] == "X":
            print("You win")
            win_cases.run = False
        else:
            print("You lose")
            win_cases.run = False
    elif _cmp["c1"] == _cmp["c5"] == _cmp["c9"]:
        if _cmp["c1"] == "X":
            print("You win")
            win_cases.run = False
        else:
            print("You lose")
            win_cases.run = False
    elif _cmp["c3"] == _cmp["c5"] == _cmp["c7"]:
        if _cmp["c3"] == "X":
            print("You win")
            win_cases.run = False
        else:
            print("You lose")
            win_cases.run = False
                                                             
        
#147, 258, 369, 123, 456, 789, 159, 357
win_cases()
win_cases.run = True
while win_cases.run==True:
    
    usr = input("Enter box number: ")

    if usr in _uservals.keys():
            
        _cmp[usr] = "X"
        del _uservals[usr]
        del _computervals[usr]
        win_cases()
        if win_cases.run == False:
            game_env()
            break
        #print("Comp",_computervals)
        computer_player()

        comp_inp = _cmp[computer_player.rand_key]="O"
        if len(_uservals) > 1:
            del _uservals[computer_player.rand_key]
            del _computervals[computer_player.rand_key]
        #print("User",_uservals)
        win_cases()
    #print(_cmp)
    game_env()
