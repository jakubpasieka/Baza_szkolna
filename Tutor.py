from User import User

class Tutor(User):
    def __init__(self, name, class_name):
        super().__init__(name)
        self.class_name = class_name