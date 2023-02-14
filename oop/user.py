class User:
    users=0
    def __init__(self,user_name,pwd):
        self.user_name=user_name #instance variable
        self.pwd=pwd
        User.users+=1
    def register(self):
        print("registering.......")
    def login(self):
        print("Login here...")
        return self
    def greet(self):
        print("greet here...")


class Student(User):
    def __init__(self,user_name,pwd, subject,number):
        self.subject=subject
        self.number=number
        super().__init__(user_name,pwd)
        print("hi "+user_name)
    def greeting_student(self):
        pass



class Faculty(User):
    def greeting_faculty(self):
        print("hi good morning teachers")

class tempFaculty(Faculty):
    def greeting_Temp_faculty(self):
        print("hi good morning temp faculty")


class StudentFaculty(Faculty,Student):
    def greeting_student_faculty(self):
        print("hi good morning temp faculty student")