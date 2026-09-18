#file name "tic_tac_toe_module.py"
#I'm still need to improve this code, currently, it only has 3 X 3 box size. So if you not choosing the 3 X 3, then it will be an error
class TicTacToe:
    
    def __init__(self, version: str) -> None:
        self.version = version
        self.box_size: str = ""
        self.box: list[str] = [] 
        self.is_playing: bool = True
        
        
    def define_the_box_size(self) -> None:
        while True:
            choice_box_size: str = input("What is the size of the box?\n"
                                     "1. 3 X 3\n"
                                     "2. 4 X 4\n"
                                     "3. 5 X 5\n"
                                     "4. 6 X 6\n"
                                     "5. 7 X 7\n"
                                     "6. 8 X 8\n"
                                     "7. 9 X 9\n"
                                     ">").title()
            
            match choice_box_size:
                case "3 X 3" | "4 X 4" | "5 X 5" | "6 X 6" | "7 X 7" | "8 X 8" | "9 X 9":
                    self.box_size = choice_box_size
                    break
                case _:
                    print("The chosen box size is not recognized, please to try again!")
                
                
    def create_the_box(self) -> None: #For now, just 3 x 3, i want to make another box size until it reach 9 x 9, but it will took a lot of time!. Next time i promise!
        box_art: dict[str, list[str]] = {"3 X 3": ["----- ----- -----",
                                                   "| 1 | | 2 | | 3 |",
                                                   "----- ----- -----",
                                                   "| 4 | | 5 | | 6 |",
                                                   "----- ----- -----",
                                                   "| 7 | | 8 | | 9 |",
                                                   "----- ----- -----"]}
        self.box = box_art[self.box_size]
            
    
    def game_validation(self) -> None:
        #Start to validate from the box number 1
        if ((self.box[1][2] == self.box[1][8] == self.box[1][14]) or
            (self.box[1][2] == self.box[3][2] == self.box[5][2]) or 
            (self.box[1][2] == self.box[3][8] == self.box[5][14])): 
            #Then...
            self.is_playing = False
                                                                    
                                                                    
        #Start to validate from the box number 2
        elif (self.box[1][8] == self.box[3][8] == self.box[5][8]):
            #Then...
            self.is_playing = False
            
        #Start to validate from the box number 3
        elif ((self.box[1][14] == self.box[3][8] == self.box[5][2]) or 
            (self.box[1][14] == self.box[3][14] == self.box[5][14])):
            #Then...
            self.is_playing = False
            
        #Start to validate from the box number 4
        elif (self.box[3][2] == self.box[3][8] == self.box[3][14]):
            #Then...
            self.is_playing = False
            
        #Let's skip to validate from the box number 5 and also 6,
        #because there are already mentioned at the validation of number 4 and 3
        
        #Start to validate from the box number 7 and skip number 8 and 9
        elif (self.box[5][2] == self.box[5][8] == self.box[5][14]):
            #Then...
            self.is_playing = False
        
        
    def start_the_game(self) -> None:
        already_selected_move: list[int] = [] #This list is for the already selected move, so it will prevent both player to select the same move
        
        for column in self.box: #This for loop is to display the empty tic tac toe box for the first time
            print(column)
        
        while True:
            print("How to play?: Select the existed number on the tic tac toe box!")
            
            for player, play_as in {"One": "X", "Two": "O"}.items():
                while True:
                    try:
                        player_move: int =  int(input(F"Player {player} as {play_as}\nYour move (select by the number!): "))
                        if player_move in already_selected_move: #This if statement check if the player choice the same move,
                            print("Your move already exist!, select another one!") #if true, then jump to the next iteration
                            continue
                        
                        elif  player_move < 1 or player_move > 9: #This if statement check if the player choice out of range 1 - 9,
                            print("Your move is out of bound!")  #if this true, then jump to the next iteration
                            continue
                            
                        match player_move: #Match the player move, then fill the box with selected move between "X" or "O" 
                            case 1:
                                self.box[1] = self.box[1].replace("1", play_as) 
                            
                            case 2:
                                self.box[1] = self.box[1].replace("2", play_as)
                            
                            case 3:
                                self.box[1] = self.box[1].replace("3", play_as)
                            
                            case 4:
                                self.box[3] = self.box[3].replace("4", play_as)
                            
                            case 5:
                                self.box[3] = self.box[3].replace("5", play_as)
                            
                            case 6:
                                self.box[3] = self.box[3].replace("6", play_as)
                            
                            case 7:
                                self.box[5] = self.box[5].replace("7", play_as)
                            
                            case 8:
                                self.box[5] = self.box[5].replace("8", play_as)
                            
                            case 9:
                                self.box[5] = self.box[5].replace("9", play_as)

                        for i in self.box: #Diplay the box for the second time
                            print(i)
        
                        already_selected_move.append(player_move) #Add the selected move, so the player won't choice the same move again!
                        
                        self.game_validation() #Calling this method to make some validation between "X" or "O" that already filled in the box.
                                               #So we could know who is the winner!                                            
                        
                        if not self.is_playing: #So, inside the game_validation method, if it's valid then self.is_playing will be "False"
                            print(F"Player {player} as \"{play_as}\" wins the game, congratulations!") #If "False" end the game with return statement!
                            return
                        
                        else:
                            break    
                        
                    except ValueError: #This is just to prevent the player move to input non numeric type!
                        print("Please only input a number for your move!")        
