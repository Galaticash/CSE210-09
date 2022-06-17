import constants

from game.cast import Cast
from game.food import Food
from game.score import Score
from game.snake import Snake
from game.script import Script
from game.control_actors_action import ControlActorsAction
from game.move_actors_action import MoveActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.draw_actors_action import DrawActorsAction
from game.director import Director
from game.keyboard_service import KeyboardService
from game.video_service import VideoService
from game.color import Color
from game.point import Point

def main():
    # create the cast
    cast = Cast()
    cast.add_actor("foods", Food())
    cast.add_actor("snakes", Snake())
    cast.add_actor("scores", Score())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()