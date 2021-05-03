# 1. Create a class named Course that has instance variables title,
# instructor, price, lectures, users(list type), ratings, avg_rating.
# Implement the methods __str__, new_user_enrolled, received_a_rating
# and show_details.


class Course:

    def __init__(self, title, instructor, price, lectures, users, ratings, avg_rating):
        self.title = title
        self.instructor = instructor
        self.price = price
        self.lectures = lectures
        self.users = users
        self.ratings = ratings
        self.avg_rating = avg_rating

    def __str__(self):
        print(f"{self.title} by {self.instructor} for ${self.price}:,.2f")

    def new_user_enrolled(self, new_user):
        self.users.append(new_user)

    def received_a_rating(self, new_rating):
        self.avg_rating = (self.avg_rating * self.ratings + new_rating)/(self.ratings + 1)
        self.ratings += 1

    def show_details(self):
        print(f'Course title: {self.title}')
        print(f'Instructor: {self.instructor}')
        print(f'Price: {self.price}')
        print(f'Number of lectures: {self.lectures}')
        print(f'Users: {self.users}')
        print(f'Average rating: {self.avg_rating}')

# From the above class, inherit two classes
# VideoCourse and PdfCourse. The class VideoCourse has
# instance variable length_video and PdfCourse has instance
# variable pages.


class VideoCourse(Course):

    def __init__(self,title, instructor, price, lectures, users, ratings, avg_rating, length_video):
        super().__init__(self,title, instructor, price, lectures, users, ratings, avg_rating)
        self.length_video = length_video

    def show_details(self):
        super().show_details()
        print(f'Length of video: {self.length_video}')


class PdfCourse(Course):

    def __init__(self, title, instructor, price, lectures, users, ratings, avg_rating, pages):
        super().__init__(self, title, instructor, price, lectures, users, ratings, avg_rating)
        self.pages = pages

    def show_details(self):
        super().show_details()
        print(f'Number of pages: {self.pages}')


# 4. In the following inheritance hierarchy we have written code to add 'S'
# to id of Student, 'T' to id of Teacher and both 'T' and 'S' to id of
# Teaching Assistant. What will be the output of this code.
# If the code does not work as intended, what changes we need to make.

class Person:
    def __init__(self, id):
        self.id = id


class Teacher(Person):
    def __init__(self, id):
        Person.__init__(self, id)
        self.id += 'T'


class Student(Person):
    def __init__(self, id):
        Person.__init__(self, id)
        self.id += 'S'


class TeachingAssistant(Student, Teacher):
    def __init__(self, id):
        Student.__init__(self, id)
        Teacher.__init__(self, id)


x = TeachingAssistant('2675')
print(x.id)

y = Student('4567')
print(y.id)

z = Teacher('3421')
print(z.id)

p = Person('5749')
print(p.id)

# we should change class names use with super() so it does not cause issues with multiple inheritance


class Person:
    def __init__(self, id):
        self.id = id


class Teacher(Person):
    def __init__(self, id):
        super().__init__(id)
        self.id += 'T'


class Student(Person):
    def __init__(self, id):
        super().__init__(id)
        self.id += 'S'


class TeachingAssistant(Student, Teacher):
    def __init__(self, id):
        super().__init__(id)
