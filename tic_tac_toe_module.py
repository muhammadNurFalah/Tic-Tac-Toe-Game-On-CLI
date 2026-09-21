#File name: tic_tac_toe_module
#Tic Tac Toe Function

class TicTacToe:
    
    def __init__(self, version: str) -> None:
        self.version = version
        self.box_size: str = ""
        self.box: list[str] = []
        self.x_box_coordinate: list[str] = []
        self.y_box_coordinate: list[str] = []
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
                                     ">").title().strip()
            
            match choice_box_size:
                case "3 X 3" | "4 X 4" | "5 X 5" | "6 X 6" | "7 X 7" | "8 X 8" | "9 X 9":
                    self.box_size = choice_box_size
                    break
                case _:
                    print("The chosen box size is not recognized, please to try again!")
                        
    
    def create_the_box(self) -> None: #For now, just 3 x 3, i want to make another box size until it reach 9 x 9, but it will took a lot of time!. Next time i promise!
        box_art: dict[str, list[str]] = {"3 X 3": ["    A     B     C  ",
                                                   "  ----- ----- -----",
                                                   "1 |   | |   | |   |",
                                                   "  ----- ----- -----",
                                                   "2 |   | |   | |   |",
                                                   "  ----- ----- -----",
                                                   "3 |   | |   | |   |",
                                                   "  ----- ----- -----"],
                                         "4 X 4": ["    A     B     C     D  ",
                                                   "  ----- ----- ----- -----",
                                                   "1 |   | |   | |   | |   |",
                                                   "  ----- ----- ----- -----",
                                                   "2 |   | |   | |   | |   |",
                                                   "  ----- ----- ----- -----",
                                                   "3 |   | |   | |   | |   |",
                                                   "  ----- ----- ----- -----",
                                                   "4 |   | |   | |   | |   |",
                                                   "  ----- ----- ----- -----"],
                                         "5 X 5": ["    A     B     C     D     E  ",
                                                   "  ----- ----- ----- ----- -----",
                                                   "1 |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- -----",
                                                   "2 |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- -----",
                                                   "3 |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- -----",
                                                   "4 |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- -----",
                                                   "5 |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- -----"],
                                         "6 X 6": ["    A     B     C     D     E     F  ",
                                                   "  ----- ----- ----- ----- ----- -----",
                                                   "1 |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- -----",
                                                   "2 |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- -----",
                                                   "3 |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- -----",
                                                   "4 |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- -----",
                                                   "5 |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- -----",
                                                   "6 |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- -----"],
                                         "7 X 7": ["    A     B     C     D     E     F     G  ",
                                                   "  ----- ----- ----- ----- ----- ----- -----",
                                                   "1 |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- -----",
                                                   "2 |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- -----",
                                                   "3 |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- -----",
                                                   "4 |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- -----",
                                                   "5 |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- -----",
                                                   "6 |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- -----",
                                                   "7 |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- -----"],
                                         "8 X 8": ["    A     B     C     D     E     F     G     H  ",
                                                   "  ----- ----- ----- ----- ----- ----- ----- -----",
                                                   "1 |   | |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- ----- -----",
                                                   "2 |   | |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- ----- -----",
                                                   "3 |   | |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- ----- -----",
                                                   "4 |   | |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- ----- -----",
                                                   "5 |   | |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- ----- -----",
                                                   "6 |   | |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- ----- -----",
                                                   "7 |   | |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- ----- -----",
                                                   "8 |   | |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- ----- -----"],
                                         "9 X 9": ["    A     B     C     D     E     F     G     H     I  ",
                                                   "  ----- ----- ----- ----- ----- ----- ----- ----- -----",
                                                   "1 |   | |   | |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- ----- ----- -----",
                                                   "2 |   | |   | |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- ----- ----- -----",
                                                   "3 |   | |   | |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- ----- ----- -----",
                                                   "4 |   | |   | |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- ----- ----- -----",
                                                   "5 |   | |   | |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- ----- ----- -----",
                                                   "6 |   | |   | |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- ----- ----- -----",
                                                   "7 |   | |   | |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- ----- ----- -----",
                                                   "8 |   | |   | |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- ----- ----- -----",
                                                   "9 |   | |   | |   | |   | |   | |   | |   | |   | |   |",
                                                   "  ----- ----- ----- ----- ----- ----- ----- ----- -----"]}
        self.box = box_art[self.box_size]
        
        
    def determine_the_coordinate(self) -> None:
        all_x_coordinate: tuple[*str] = ("A", "B", "C", "D", "E", "F", "G", "H", "I")
        all_y_coordinate: tuple[*str] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
    
        match self.box_size:
            case "3 X 3":
                self.x_box_coordinate = all_x_coordinate[:3]
                self.y_box_coordinate = all_y_coordinate[:3]
        match self.box_size:
            case "4 X 4":
                self.x_box_coordinate = all_x_coordinate[:4]
                self.y_box_coordinate = all_y_coordinate[:4]
        match self.box_size:
            case "5 X 5":
                self.x_box_coordinate = all_x_coordinate[:5]
                self.y_box_coordinate = all_y_coordinate[:5]
        match self.box_size:
            case "6 X 6":
                self.x_box_coordinate = all_x_coordinate[:6]
                self.y_box_coordinate = all_y_coordinate[:6]
        match self.box_size:
            case "7 X 7":
                self.x_box_coordinate = all_x_coordinate[:7]
                self.y_box_coordinate = all_y_coordinate[:7]
        match self.box_size:
            case "8 X 8":
                self.x_box_coordinate = all_x_coordinate[:8]
                self.y_box_coordinate = all_y_coordinate[:8]
        match self.box_size:
            case "9 X 9":
                self.x_box_coordinate = all_x_coordinate[:9]
                self.y_box_coordinate = all_y_coordinate[:9]
        
        
    def determine_the_coordinate_to_fill(self, coordinate: str) -> list[int]:
        index_of_column: int = 0
        index_of_row: int = 0
        
        match coordinate[0]:
            case "A":
                index_of_column = 4
            case "B":
                index_of_column = 10
            case "C":
                index_of_column = 16
            case "D":
                index_of_column = 22
            case "E":
                index_of_column = 28
            case "F":
                index_of_column = 34
            case "G":
                index_of_column = 40
            case "H":
                index_of_column = 46
            case "I":
                index_of_column = 52
        
        match coordinate[1]:
            case "1":
                index_of_row = 2
            case "2":
                index_of_row = 4
            case "3":
                index_of_row = 6
            case "4":
                index_of_row = 8
            case "5":
                index_of_row = 10
            case "6":
                index_of_row = 12
            case "7":
                index_of_row = 14
            case "8":
                index_of_row = 16
            case "9":
                index_of_row = 18
        
        return [index_of_row, index_of_column]            
                
    
    def fill_the_box(self, row: int, column: int, value: str,) -> None:
        listed_string_in_row: list[str] = list(self.box[row])
        listed_string_in_row[column] = value
        
        self.box[row] = "".join(listed_string_in_row)
            
    
    def game_validation(self) -> None:
        side_length: int = int(self.box_size[0]) #If box size 4 X 4 then the difference = 4 - 3 = 1,
        difference: int = side_length - 3 + 1    #"3" is taken from 3 X 3, so it always subtract with 3. +1 is to prevent 0
        
        """So, the for loop below is to check is the there any winning move in tic tac toe game.
        Why do we need for loop? so if i'm not using for loop then it will took 81 if-else if statement.
        So, my solution is to check by 3 X 3 first then if there is no winning move in the first 3 X 3,
        move to one side to the right until the end, if there is still no winning condition then move by one side down.
        Repeat it until it found the winning solution, if founded then stop the game"""
        
        for i in range(0, difference):
            i *= 2
            for j in range(0, difference):
                j *= 6
                #Start to validate from the box number 1
                if ((self.box[2 + i][4 + j] == "X" and self.box[2 + i][10 + j] == "X" and self.box[2 + i][16 + j] == "X") or
                    (self.box[2 + i][4 + j] == "O" and self.box[2 + i][10 + j] == "O" and self.box[2 + i][16 + j] == "O")):
                    #Then...
                    self.is_playing = False
                    
                    
                elif ((self.box[2 + i][4 + j] == "X" and self.box[4 + i][4 + j] == "X" and self.box[6 + i][4 + j] == "X") or
                      (self.box[2 + i][4 + j] == "O" and self.box[4 + i][4 + j] == "O" and self.box[6 + i][4 + j] == "O")):
                      #Then...
                    self.is_playing = False
                    
                elif ((self.box[2 + i][4 + j] == "X" and self.box[4 + i][10 + j] == "X" and self.box[6 + i][16 + j] == "X") or
                      (self.box[2 + i][4 + j] == "O" and self.box[4 + i][10 + j] == "O" and self.box[6 + i][16 + j] == "O")):
                    #Then...
                    self.is_playing = False                                 
                                                                            
                #Start to validate from the box number 2
                elif ((self.box[2 + i][10 + j] == "X" and self.box[4 + i][10 + j] == "X" and self.box[6 + i][10 + j] == "X") or
                      (self.box[2 + i][10 + j] == "O" and self.box[4 + i][10 + j] == "O" and self.box[6 + i][10 + j] == "O")):
                    #Then...
                    self.is_playing = False
                    
                #Start to validate from the box number 3
                elif ((self.box[2 + i][16 + j] == "X" and self.box[4 + i][10 + j] == "X" and self.box[6 + i][4 + j] == "X") or
                      (self.box[2 + i][16 + j] == "O" and self.box[4 + i][10 + j] == "O" and self.box[6 + i][4 + j] == "O")):
                    #Then...
                    self.is_playing = False      
                        
                elif ((self.box[2 + i][16 + j] == "X" and self.box[4 + i][16 + j] == "X" and self.box[6 + i][16 + j] == "X") or
                      (self.box[2 + i][16 + j] == "O" and self.box[4 + i][16 + j] == "O" and self.box[6 + i][16 + j] == "O")):
                    #Then...
                    self.is_playing = False
                    
                #Start to validate from the box number 4
                elif ((self.box[4 + i][4 + j] == "X" and self.box[4 + i][10 + j] == "X" and self.box[4 + i][16 + j] == "X") or
                      (self.box[4 + i][4 + j] == "O" and self.box[4 + i][10 + j] == "O" and self.box[4 + i][16 + j] == "O")):
                    #Then...
                    self.is_playing = False
                    
                #Let's skip to validate from the box number 5 and also 6,
                #because there are already mentioned at the validation of number 4 and 3
                
                #Start to validate from the box number 7 and skip number 8 and 9
                elif ((self.box[6 + i][4 + j] == "X" and self.box[6 + i][10 + j] == "X" and self.box[6 + i][16 + j] == "X") or
                      (self.box[6 + i][4 + j] == "O" and self.box[6 + i][10 + j] == "O" and self.box[6 + i][16 + j] == "O")):
                    #Then...
                    self.is_playing = False
                
        
    def start_the_game(self) -> None:
        already_selected_move: list[str] = [] #This list is for the already selected move, so it will prevent both player to select the same move
        self.determine_the_coordinate() #Determine the coordinate that used based on the size!
        
        for column in self.box: #This for loop is to display the empty tic tac toe box for the first time
            print(column)
        
        while True:
            print("How to play?: Select the coordinate of the tic tac toe box!")
            print("Example: A1, B5, etc")
            
            for player, play_as in {"One": "X", "Two": "O"}.items():
                while True:
                    player_move: str = input(F"Player {player} as {play_as}\nYour move: ").upper().strip()
                    if player_move in already_selected_move: #This if statement check if the player choice the same move,
                        print("Your move already exist, select the another one!") #if true, then jump to the next iteration
                        continue
                    
                    elif (player_move[0] not in self.x_box_coordinate or
                          player_move[1:] not in self.y_box_coordinate): #This if statement check if the player choice out of range 1 - 9,
                        print("Your move is invalid!")                   #if this true, then jump to the next iteration
                        continue
        
                    row, column = self.determine_the_coordinate_to_fill(player_move)
                    self.fill_the_box(row, column, play_as)
                    
                    for i in self.box: #Diplay the box for the second time
                        print(i)
    
                    already_selected_move.append(player_move) #Add the selected move, so the player won't choice the same move again!
                    
                    self.game_validation() #Calling this method to make some validation between "X" or "O" that already filled in the box.
                                           #So we could know who is the winner!                                            
                    
                    if not self.is_playing: #So, inside the game_validation method, if it's valid then self.is_playing will be "False"
                        print(F"Player {player} as \"{play_as}\" wins the game, congratulations!") #If "False" end the game will ended!
                        return
                    
                    else:
                        break            
