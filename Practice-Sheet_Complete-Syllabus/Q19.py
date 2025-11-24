class Club:
    def __int__(self,name,students):
        self.name = name
        self.students = students

class StudentClubs(Club):
    def add_club(self,club_name):
        self.clubs = {}
        self.clubs[club_name] = []

    def add_student(self,club_name,student_id,position):
        self.clubs[club_name] = []
        self.clubs[club_name].append([student_id,position])
    return self.clubs

    def remove_student(self,club_name,student_id):
        for i in self.clubs[club_name]:
            if i[0] == student_id:
                self.clubs[club_name].remove(i)
    return self.clubs

    def add_position(self,club_name,student_id,new_position):
        for i in self.clubs[club_name]:
            if i[0] == student_id:
                i[1] = new_position
    return self.clubs
        
    def remove_position(self,club_name,student_id):
        for i in self.clubs[club_name]:
            if i[0] == student_id:
                i[1] = None
    return self.clubs


sc=StudentClubs()
sc.add_club("Science")
sc.add_student("Science",1,"President")
sc.add_position("Science",1,"Member")
sc.remove_position("Science",1)
sc.remove_student("Science",1)
sc.add_student("Math",2,"Leader")