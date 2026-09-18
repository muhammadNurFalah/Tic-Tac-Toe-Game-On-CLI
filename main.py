from tic_tac_toe_module import TicTacToe

def main() -> None:
    game: TicTacToe = TicTacToe("3")
    game.define_the_box_size()
    game.create_the_box()
    game.start_the_game()
    
if __name__ == "__main__":
    main()
    
    