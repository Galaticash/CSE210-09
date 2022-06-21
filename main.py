from director import Director

def main():
    cycle_game = Director()
    cycle_game.start_game()
    while not cycle_game.get_game_over():
        cycle_game.update_game()    
    cycle_game.end_game()

if __name__ == "__main__":
    main()