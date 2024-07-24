import pickle

class Student:
    def __init__(self, email, names, gender):
        self.email = email
        self.names = names
        self.gender = gender
        self.courses_registered = []
        self.total_marks = 0.0
        self.GPA = 0.0

    def calculate_marks_and_grade(self):
        if not self.courses_registered:
            self.total_marks = 0.0
            self.GPA = 0.0
        else:
            total_points = sum(course.credits * marks for course, marks in self.courses_registered)
            total_credits = sum(course.credits for course, marks in self.courses_registered)
            self.total_marks = total_points / total_credits if total_credits > 0 else 0.0
            self.GPA = self.calculate_gpa_from_marks(self.total_marks)

    def calculate_gpa_from_marks(self, marks):
        # Custom GPA calculation based on marks
        if marks >= 85:
            return 4.0
        elif marks >= 75:
            return 3.7
        elif marks >= 65:
            return 3.3
        elif marks >= 55:
            return 3.0
        elif marks >= 45:
            return 2.7
        elif marks >= 35:
            return 2.3
        else:
            return 2.0

    def register_for_course(self, course, marks):
        self.courses_registered.append((course, marks))
        self.calculate_marks_and_grade()

class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, student):
        self.student_list.append(student)

    def add_course(self, course):
        self.course_list.append(course)

    def register_student_for_course(self, student_email, course_name, marks):
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, marks)
            print("The student has been registered successfully.")
        else:
            print("Student or Course not found")

    def calculate_ranking(self):
        return sorted(self.student_list, key=lambda s: s.total_marks, reverse=True)

    def search_by_grade(self, grade):
        return [student for student in self.student_list if self.grade_from_marks(student.total_marks) == grade]

    def generate_transcript(self, student_email):
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            print("............................................................")
            print("                Welcome to Our Student Transcript              ")
            print("............................................................")
            print(f"Student name: {'.' * (25 - len('Student name: '))} {student.names}")
            print(f"Student email: {'.' * (25 - len('Student email: '))} {student.email}")
            print(f"Gender: {'.' * (25 - len('Gender: '))} {student.gender}")
            print("............................................................")
            for course, marks in student.courses_registered:
                print(f"Trimester: {'.' * (25 - len('Trimester: '))} {course.trimester}")
                print(f"Course name: {'.' * (25 - len('Course name: '))} {course.name}")
                print(f"Marks: {'.' * (25 - len('Marks: ' + format(marks, '.2f')))} {marks:.2f}")
                print(f"GPA: {'.' * (25 - len('GPA: ' + format(student.GPA, '.2f')))} {student.GPA:.2f}")
                grade = self.grade_from_marks(marks)
                print(f"Grade: {'.' * (25 - len('Grade: ' + grade))} {grade}")
                print("............................................................")
                print(f"{student.names} has successfully completed {course.name}!")
                print("............................................................")
        else:
            print("Student not found")

    def grade_from_marks(self, marks):
        # Custom grading scheme based on marks
        if marks >= 85:
            return 'A'
        elif marks >= 75:
            return 'B'
        elif marks >= 65:
            return 'C'
        elif marks >= 55:
            return 'D'
        elif marks >= 45:
            return 'E'
        else:
            return 'F'

    def save_data(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

def main():
    print("Welcome to Olivier's Grading App!")
    gradebook = GradeBook()

    while True:
        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("    Welcome to Olivier's Grading App    ")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate Ranking")
        print("5. Search by Grade")
        print("6. Generate Transcript")
        print("7. Exit")
        print("8. Save Data")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        choice = input("Enter your choice: ")

        if choice == '1':
            email = input("Enter student's email: ")
            names = input("Enter student's name: ")
            gender = input("Enter student's gender (Male/Female): ").capitalize()
            student = Student(email, names, gender)
            gradebook.add_student(student)
            print("The student has been added successfully.")
        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter trimester: ")
            credits = float(input("Enter credits: "))
            course = Course(name, trimester, credits)
            gradebook.add_course(course)
            print("The course has been added successfully.")
        elif choice == '3':
            student_email = input("Enter student's email: ")
            course_name = input("Enter course name: ")
            marks = float(input("Enter marks: "))
            gradebook.register_student_for_course(student_email, course_name, marks)
        elif choice == '4':
            ranking = gradebook.calculate_ranking()
            print("Student Rankings by Total Marks:")
            for student in ranking:
                print(f"{student.names} - Total Marks: {student.total_marks}, GPA: {student.GPA}")
        elif choice == '5':
            grade = input("Enter grade to search for: ")
            students = gradebook.search_by_grade(grade)
            print("Students with the specified grade:")
            for student in students:
                print(f"{student.names} - Email: {student.email}")
        elif choice == '6':
            student_email = input("Enter student's email: ")
            gradebook.generate_transcript(student_email)
        elif choice == '7':
            print("Thank you for using our App.")
            break
        elif choice == '8':
            filename = input("Enter filename to save data (e.g., 'gradebook_data.pkl'): ")
            gradebook.save_data(filename)
            print(f"Data saved successfully to '{filename}'.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
