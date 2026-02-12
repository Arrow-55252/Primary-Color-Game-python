import random

class ColorsApp:

    #numerical limitations along with points
    MAX_ATTEMPTS = 3
    TOTAL_POINTS = 0

    #Dictionary with 2 colors that result in another color when mixed
    def __init__ (self):
        
        self.primary = {("red", "yellow"):"Orange",
        ("blue", "yellow"): "Green",
        ("blue", "red"): "Purple"}

    
    def ran_list(self):
       color = ["Orange", "Green", "Purple"]
       random.shuffle(color)

       for colors in color:
           return colors

    def main(self):

        attempts = ColorsApp.MAX_ATTEMPTS
        points = ColorsApp.TOTAL_POINTS
        
        while attempts > 0:

            ran_list = self.ran_list()
            color_question = (f"What makes the color {ran_list}? ")
            print(color_question)
            color_input = (input("color 1: "), input("color 2: "))
            sorted_colors = tuple(sorted(color_input))

            result = self.primary.get(sorted_colors)

            if result == ran_list:
                points += 1
                print("CORRECT!")
                print(f" Number correct: {points}")
                continue

            else:
                attempts -= 1
                if attempts >= 1:
                    print(f"Sorry please try again you have {attempts} attempts left!") 

                if attempts < 1:
                    print("You do not have any attempts left!")   

        print("Game Over")


user = ColorsApp()
user.main()
