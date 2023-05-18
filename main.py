import turtle 
import pandas as pd

# A game that you can test your knowledge of US States

screen = turtle.Screen()
screen.title('U.S States Game')
path = 'blank_states_img.gif'
screen.addshape(path)
turtle.shape(path)
t = turtle.Turtle()
t.hideturtle()
t.penup()
# Where we keep our states coordinations
dataset = pd.read_csv('50_states.csv')
# Taking only the sates as a list to compare our guess
all_states = dataset.state.to_list()

# Keeping track of the states we correctly guessed
guessed_states = []
  
# Gonna work until we guess all the states correctly or use the secret(!) code exit
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt='Name A State').title()
    
    # When we want to exit, it creates another csv file to show which states we couldn't find. 
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    
    # When we find a state, first it takes it to our list where we keep track of correctly guessed states,
    # then, use to turtle to write the name of the state in the given coordinates in the csv file
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = dataset[dataset.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)



