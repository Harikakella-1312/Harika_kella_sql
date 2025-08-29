#Q5. Create a class Course with attributes like title, instructor, and price.
#Create a class Student with methods to enroll(course) and complete_course(course).
#Use inheritance to create different course types: VideoCourse,
# LiveSession, Workshop. Implement a method generate_certificate() 
# when a course is completed. Implement a method generate_certificate()
#  when a course is completed.Add exception handling for 
# duplicate enrollments or incomplete prerequisites.

class DuplicateEnrollments(Exception):
    pass

class prerequisites(Exception):
    pass

class Course:
    def __init__(self, title, instructor, price, prerequisites=None):
        self.__title = title
        self.__instructor = instructor
        self.__price = price
        self.prerequisites = prerequisites or []

    def __str__(self):
        return f"{self.title} and {self._instructor} for ${self.price}"


class VideoCourse:
    def __init__(self, title, instructor, price, duration, prerequisites=0):
        super().__init__(title, instructor, price, prerequisites)
        self.duration = duration

class LiveSession:
    def __init__(self, title, instructor, price, schedule, prerequisites=0 ):
        super().__init__(title, instructor, price, prerequisites=0)
        self.schedule = schedule

class Workshop:
    def __init__(self, title, instructor, price, location, prerequisites=0):
        super().__init__(title, instructor, price, prerequisites)
        self.location = location
    

class Student:
    def __init__(self, name):

        self.name =name
        self.enrolled_courses = []
        self.completed_courses = [] 

    def enroll(self, course: Course):
        if course in self.enrolled_courses:
            raise DuplicateEnrollments(f"{self.name} is already enrolled in {course.title}")
        
        for prereq in course.prerequisites:
            if prereq not in self.completed_courses:
                raise prerequisites(f"{self.name} must be enrolled before adding into {course.title}")
            self.enrolled_courses.append(course)

    def complete_course(self, course: Course):

        if course not in self.enrolled_courses:
            raise Exception(f"{self.name} is not enrolled into {course.title}")
        self.completed_courses.append(course)
        self.generate_certificate(course)


    def generate_cerificate(self, course: Course):
        return {
            "student": self.name,
            "course_name": course.title,
            "instructor_name": course.instructor,
            "status": "completed"

        }
    
if __name__ == "__main__":
    courses = []

    n = int(input("Enter number of Courses: "))
    for _ in range(n):
        ctype = input("Enter the type of course: ")
        title = input("Enter the course title: ")
        instructor = input("Enter instructor name: ")
        price = float(input("Enter the price for the course: "))


        if ctype == "video":
            duration = input("Enter duration: ")
            course = VideoCourse(title, instructor, price, duration)
        elif ctype == "live":
            schedule = input("Enter schedule: ")
            course = LiveSession(title, instructor, price, schedule)
        elif ctype == "workshop":
            location = input("Enter location: ")
            course = Workshop(title, instructor, price, location)
        else:
            print("Invalid course type, skipping...")
            continue
        courses.append(course)

    student_name = input("\nEnter student name: ")
    s1 = Student(student_name)

    while True:
        choice = input("\nDo you want to enroll in a course? (yes/no): ").lower()
        if choice == "no":
            break
        for idx, c in enumerate(courses):
            print(f"{idx}: {c}")
        try:
            index = int(input("Enter course index to enroll: "))
            s1.enroll(courses[index])
        except Exception as e:
            print("Error:", e)

    while True:
        choice = input("\nDo you want to complete a course? (yes/no): ").lower()
        if choice == "no":
            break
        for idx, c in enumerate(courses):
            print(f"{idx}: {c}")
        try:
            index = int(input("Enter course index to complete: "))
            s1.complete_course(courses[index])
        except Exception as e:
            print("Error:", e)











    

    


        



    




        
    