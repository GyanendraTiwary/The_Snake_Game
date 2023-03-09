import turtle as t

INITIAL_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:


   
    def __init__(self):

        global INITIAL_POSITIONS
        self.positions = INITIAL_POSITIONS
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        for i in range(3):
            new_segment = t.Turtle()
            new_segment.penup()
            new_segment.color('orange')
            new_segment.shape('circle')
            new_segment.goto(self.positions[i])
            self.segments.append(new_segment)


 
    def run(self):
        
        for i in range(len(self.segments)-1, 0 , -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)
        
    def increase_size(self):
        new_segment = t.Turtle()
        new_segment.penup()
        new_segment.color('orange')
        new_segment.shape('circle')
        new_segment.goto(self.segments[-1].pos())
        self.segments.append(new_segment)

    
         
    def up(self):
       if(self.segments[0].heading() != 270): 
            self.segments[0].setheading(90)
    def down(self):
        if(self.segments[0].heading() != 90):
            self.segments[0].setheading(270)
    def right(self):
        if(self.segments[0].heading() != 180):
            self.segments[0].setheading(0)
    def left(self):
        if(self.segments[0].heading() != 0):
            self.segments[0].setheading(180)

    
                
            