from User import User

class Teacher(User):
    def __init__(self, name, subject, class_names):
        super().__init__(name)
        self.subject = subject
        self.class_names = class_names