from turtle import Screen
from sec019_mine_project_class import TurtleGameClass, ResultGame

def play_game():
    screen = Screen()
    screen_x = 800
    screen_y = 600
    screen.setup(screen_x,screen_y)

    start_x = -screen_x/2 + 10
    turtles = []
    string_possible_winners = ''
    possible_colors = ['red','blue','purple','orange','green','yellow']
    amount_spaces = len(possible_colors) - 1

    ##offset_border = 2*offset_turtle
    ##ofset_turtles*amount_spaces + 2*offset_borders = screen_y
    offset_turtle = screen_y/(amount_spaces+4)
    offset_borders = 2*offset_turtle
    initial_position = -screen_y/2 + offset_borders

    turtle_positions = [(initial_position+offset_turtle*x) for x in range(len(possible_colors))]

    for i, color in enumerate(possible_colors):
        if i == 0:
            string_possible_winners += color
        else:
            string_possible_winners += f' / {color}'    
        start_y = turtle_positions[i]
        turtle = TurtleGameClass(color,start_x,start_y,screen_x) 
        turtles.append(turtle)    

    my_chosen_turtle = screen.textinput(title='Chosen turtle',prompt=f'Guess a turtle to win the game: ({string_possible_winners})')

    winning_color = []      
    continue_race = True
    while continue_race:
        for i in range(len(turtles)):
            validation = turtles[i].move_or_stay_action()
            if validation:
                winning_color.append(turtles[i].color_chosen)
                continue_race = False

    if len(winning_color) == 1:
        winning_color = winning_color[0]
        
    if str(my_chosen_turtle).lower() == winning_color:
        print(f'You won! The winning turtle was: {winning_color}')
    else:
        print(f'You lost! The winning turtle was: {winning_color}')
    
    result = ResultGame()
    result.write_winning_paddle_name(winning_color,my_chosen_turtle)
    
    screen.exitonclick()
    
play_game()