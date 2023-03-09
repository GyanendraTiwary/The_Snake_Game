from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
 

def main():
    screen = Screen()
    screen.clearscreen()
    screen.bgcolor('black')
    screen.setup(600,600)
    screen.title('Snake Game')
    screen.tracer(0)


    mysnake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(mysnake.up,"Up")
    screen.onkey(mysnake.down,"Down")
    screen.onkey(mysnake.right,"Right")
    screen.onkey(mysnake.left,"Left")
    screen.onkey(main, "space")

    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        mysnake.run()
        
        
        #detecting collision with wall
        if mysnake.head.xcor() > 280 or mysnake.head.xcor() < -280 or mysnake.head.ycor() > 280 or mysnake.head.ycor() < -280:
            game_on = False
            scoreboard.game_over()
            
        #detecting collision with snake itself
        for segment in mysnake.segments[1:]:
            if mysnake.head.distance(segment) < 10:
               game_on = False
               scoreboard.game_over() 

        #detecting collision of snake and food

        if (mysnake.head.distance(food) <= 15):
            food.change_pos()
            mysnake.increase_size()
            scoreboard.increase_score()
        

        
        


    screen.exitonclick()
    
            
main()

    



        