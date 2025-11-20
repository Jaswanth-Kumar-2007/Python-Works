class Club:
    def __int__(self,name,students):
        self.name = name
        self.students = students

class StudentClubs(Club):
    def __init__(self,name,students):
        super().__init__(name,students)

    def add_club(self,club_name):
        self.clubs = {}
        self.clubs[f"{club_name}"]


    def add_student(self,club_name,student_id,position):
        pass
