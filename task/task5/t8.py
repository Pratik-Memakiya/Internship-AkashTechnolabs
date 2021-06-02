
'''
Write a program with use of inheritance: Define a class publisher that
stores the name of the title. Derive two classes book and tape, which
inherit publisher. Book class contains member data called page no and
tape class contain time for playing. Define functions in the appropriate
classes to get and print the details. 
'''
class Publisher:
    title_name ="John Carter"
    def display(self):
        print("Name : ",self.title_name)
class book(Publisher):
    no_pages = 200
    def display1(self):
      
        print('Pages:',self.no_pages)

class tape(book):
    time = 3
    def display2(self):
        
        print('time :{} hrs'.format(self.time))

obj1 = Publisher()
obj2 = book()
obj3 = tape()
print("----Publisher display()----")
obj1.display() 
print("----Book display()----")
obj2.display1() 
obj2.display() 
print("----Tape display()----")
obj3.display2() 
obj3.display1() 
obj3.display() 