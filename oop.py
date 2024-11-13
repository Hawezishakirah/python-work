#Object Oriented Programming
#It always has classes and objects
#a class has properties/attributes
#methods are items of the class
#objects come from a class
#an object takes on the properties of a class
#a class name starts with a capital letter 
#Class is always singular

#sntax of OOP
#1.Creating classes
#Cohort classes
class Cohort:
   name
   description
   start_date
   end_date


   #add a constractor for the cohort class
#add a metthod to the class that prints the cohort name and the number of students
# create a new instance/object of the cohort class

#a
class Cohort:
    def __init__(self, cohort_name, number_of_students):
        
        self.cohort_name = cohort_4
        self.number_of_students = 50

    def print_cohort_details(self):
        
        print(f"Cohort Name: {self.cohort_name}")
        print(f"Number of Students: {self.number_of_students}")

# b
cohort_4 = Cohort("Python 101", 30)

#c
cohort_4.print_cohort_details()
