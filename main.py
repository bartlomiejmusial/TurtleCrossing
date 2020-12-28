import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)

# Turn off the tracer
screen.tracer(0)

turtle_player = Player()

screen.listen()
screen.onkey(fun=turtle_player.move_up, key="Up")

car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
iteration = 0
while game_is_on:
    iteration += 1
    time.sleep(0.1)
    # Screen update every 0.1s
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if turtle_player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect successful crossing
    if turtle_player.is_at_finish_line():
        turtle_player.go_to_start()
        car_manager.level_up()
        scoreboard.update_score()

screen.exitonclick()

