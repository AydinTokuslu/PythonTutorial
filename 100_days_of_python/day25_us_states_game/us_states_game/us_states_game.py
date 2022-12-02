import pandas
import turtle



screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"  # istediğimiz fotoğrafı yükledik
screen.addshape(image)
turtle.shape(image)


# #x,y koordinata göre noktayı bulma fonksiyonu
# def get_mouse_click_coor(x, y):# mouse ile dokunduğumuz yerin koordinatını verir
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop() # resmin sürekli ekranda kalmasını sağlıyor.

# elimizdeki 50_states.csv dosyasında tüm koordinatlar olduğu için,
# bu fonksiyona bu örnekte gerek yok!!!!

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    #print(answer_state)

    if answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        # #print(missing_states)
        # kısa yolu !!!!!!!
        missing_states = [state for state in all_states if state not in guessed_states]

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    #if answer_state is one of the states in all the states of the 50_states.csv
    if answer_state in all_states:
        guessed_states.append(answer_state)
        new_data = pandas.DataFrame(guessed_states)
        new_data.to_csv("states_to_be_guessed.csv")
        #if they got it right
        # create a turtle to write the name of the state at the state's x and y coordinate
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


# states_to_learn.csv



screen.exitonclick()  # click yaptığımızda haritanın kaybolmasını önlemek için bunu kaldırıyoruz.
