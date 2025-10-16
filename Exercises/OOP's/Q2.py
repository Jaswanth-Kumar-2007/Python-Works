# Movie Class 
class Movie:
    def __init__(self,title,genre,rating,year):
        self.title = title
        self.genre = genre
        self.rating = rating
        self.year = year

    def display_info(self):
        print(f"Title --> {self.title}")
        print(f"Genre --> {self.genre}")
        print(f"Rating --> {self.rating}")
        print(f"Year --> {self.year}")

    def update_rating(self,new_rating):
        self.rating = new_rating
        print(f"Updated Rating is {self.rating}")

movie1 = Movie("Doctor","Comedy",10.0,2022)

movie1.display_info()
movie1.update_rating(9.5)
movie1.display_info()