import turtle 
import pandas as pd


screen = turtle.Screen()
screen.title('U.S States Game')
path = 'blank_states_img.gif'
screen.addshape(path)
turtle.shape(path)

dataset = pd.read_csv('50_states.csv')


answer_state = screen.textinput(title="Answer", prompt='Name A State')  



screen.exitonclick()