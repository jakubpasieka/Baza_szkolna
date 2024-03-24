from Student import Student
from Teacher import Teacher
from Tutor import Tutor


class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.tutors = []

    def create_student(self, name, class_name):
        student = Student(name, class_name)
        self.students.append(student)

    def create_teacher(self, name, subject, class_names):
        teacher = Teacher(name, subject, class_names)
        self.teachers.append(teacher)

    def create_tutor(self, name, class_name):
        tutor = Tutor(name, class_name)
        self.tutors.append(tutor)

    def manage_students(self, class_name):
        students_in_class = [student.name for student in self.students if student.class_name == class_name]
        tutor_in_class = [tutor.name for tutor in self.tutors if tutor.class_name == class_name]
        return students_in_class, tutor_in_class

    def manage_teachers(self, teacher_name):
        teacher_classes = [teacher.class_names for teacher in self.teachers if teacher.name == teacher_name]
        return teacher_classes

    def manage_tutors(self, tutor_name):
        tutor_students = [student.name for student in self.students for tutor in self.tutors
                          if tutor.name == tutor_name and student.class_name == tutor.class_name]
        return tutor_students

    def get_student_lessons(self, student_name):
        student = next((student for student in self.students if student.name == student_name), None)
        if student is not None:
            lessons = [(teacher.subject, teacher.name) for teacher in self.teachers
                       if student.class_name in teacher.class_names]
            return lessons
        else:
            return []


school = School()

while True:
    command = input("Wprowadź polecenie ('u' - utwórz, 'z' - zarządzaj, 'x' - koniec): ")
    if command == 'u':
        while True:
            user_type = input("Wprowadź typ użytkownika ('u' - uczeń, 'n' - nauczyciel, 'w' - wychowawca, "
                              "'x' - powrót): ")
            if user_type == 'u':
                name = input("Wprowadź imię i nazwisko ucznia: ")
                class_name = input("Wprowadź nazwę klasy: ")
                school.create_student(name, class_name)
            elif user_type == 'n':
                name = input("Wprowadź imię i nazwisko nauczyciela: ")
                subject = input("Wprowadź nazwę przedmiotu: ")
                class_names = []
                while True:
                    class_name = input("Wprowadź nazwę klasy lub 'x', aby zakończyć: ")
                    if class_name == 'x':
                        break
                    class_names.append(class_name)
                school.create_teacher(name, subject, class_names)
            elif user_type == 'w':
                name = input("Wprowadź imię i nazwisko wychowawcy: ")
                class_name = input("Wprowadź nazwę klasy: ")
                school.create_tutor(name, class_name)
            elif user_type == 'x':
                break

    elif command == 'z':
        while True:
            manage_type = input("Wprowadź typ zarządzania ('k' - klasa, 'u' - uczeń, 'n' - nauczyciel, "
                                "'w' - wychowawca, 'x' - powrót): ")
            if manage_type == 'k':
                class_name = input("Wprowadź nazwę klasy: ")
                students, tutor = school.manage_students(class_name)
                print(f"Uczniowie w klasie {class_name}: {', '.join(students)}")
                print(f"Wychowawca klasy {class_name}: {tutor[0]}")
            elif manage_type == 'u':
                student_name = input("Wprowadź imię i nazwisko ucznia: ")
                lessons = school.get_student_lessons(student_name)
                if lessons:
                    lessons_str = ', '.join([f'{lesson[0]} ({lesson[1]})' for lesson in lessons])
                    print(f"Lekcje ucznia {student_name}: {lessons_str}")
                else:
                    print(f"Uczeń {student_name} nie uczestniczy w żadnych lekcjach.")
            elif manage_type == 'n':
                teacher_name = input("Wprowadź imię i nazwisko nauczyciela: ")
                class_names = school.manage_teachers(teacher_name)
                print(f"Nauczyciel {teacher_name} prowadzi zajęcia z klasami: {', '.join(class_names[0])}")
            elif manage_type == 'w':
                tutor_name = input("Wprowadź imię i nazwisko wychowawcy: ")
                students = school.manage_tutors(tutor_name)
                print(f"Uczniowie wychowawcy {tutor_name}: {', '.join(students)}")
            elif manage_type == 'x':
                break

    elif command == 'x':
        break
