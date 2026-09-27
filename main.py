from tic_tac_toe_module import TicTacToe

def main() -> None:
    is_playing: bool = True
    
    while is_playing:       
        game: TicTacToe = TicTacToe("2")
        game.define_the_box_size()
        game.create_the_box()
        game.start_the_game()
        
        while True:
            play_again: str = input("Would you like to play again? (yes or no)\n>").title()
            
            if play_again in ("Yes", "Y"):
                print("Let's play again!")
                break
            
            elif play_again in ("No", "N"):
                print("Good bye and have a nice day!")
                is_playing = False
                break
            
            else:
                print(F"Your input {play_again} is invalid!")
                
if __name__ == "__main__":
    main()
