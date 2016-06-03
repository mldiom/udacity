class Parent ():
    def __init__(self, eye_color, last_name):
        print("parent constructor called!")
        self.eye_color = eye_color
        self.last_name = last_name

okunkwo = Parent("black", "achebe")
print(okunkwo.eye_color)
