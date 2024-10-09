current_year = 2024
class students:
    def __init__(self,age,name,height,yeargroup,gender):
        self.age = age
        self.name = name
        self.height = height
        self.yeargroup = yeargroup
        self.gender = gender
    def birthyear(self):
        print(current_year - self.age)

object = students(11,"joe",167,7,"male")
object.birthyear()
print(object.age)
object2 = students(13,"mark",173,9,"male")
print(object2.age)


    