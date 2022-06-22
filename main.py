from director import Director

def main():
    cycle_game = Director()
    cycle_game.start_game()
    # Slightly different here, window will not close until user presses the "X" button.
    while not cycle_game.get_window_close():
        cycle_game.update_game()    
    cycle_game.end_game()

if __name__ == "__main__":
    main()