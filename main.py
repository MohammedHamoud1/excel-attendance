import openpyxl

class Student:
    def __init__(self, name, student_id):
        self.id = student_id
        self.name = name
        self.attendance = None  # None for unrecorded, 1 for present, 0 for absent

def record_attendance(students):
    student_ids = {student.id for student in students}  # Create a set of student IDs for quick lookup
    attendance_recorded = False  # Track if any attendance was recorded

    while True:
        input_id = input("Enter a student ID to mark present (or 'done' to finish): ")
        
        if input_id.lower() == 'done':
            if not attendance_recorded:  # If no attendance was recorded
                for student in students:
                    student.attendance = 0  # Mark all as absent
                print("All students marked as absent.")
            else:
                for student in students:
                    if student.attendance is None:  # If attendance not recorded
                        student.attendance = 0  # Mark as absent
            break
        
        if input_id in student_ids:
            for student in students:
                if student.id == input_id:
                    student.attendance = 1  # Mark as present
                    print(f"{student.name} marked as present.")
                    attendance_recorded = True  # Attendance has been recorded
                    break
        else:
            print("Invalid ID! This ID will be marked as absent.")
            for student in students:
                if student.id == input_id:
                    student.attendance = 0  # Mark as absent
                    print(f"{student.name} marked as absent.")
                    break

def save_to_excel(students, filename):
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = "Attendance"

    # Write header
    worksheet.append(["ID", "Name", "Attendance"])

    # Write student data
    for student in students:
        worksheet.append([student.id, student.name, student.attendance])

    workbook.save("try.xlsx")

def main():
    students = [
Student("student 1","41"),
Student("student 2", "67"),
    ]

    record_attendance(students)

    save_to_excel(students, "try.xlsx")

    print("Attendance recorded successfully!")

if __name__ == "__main__":
    main()
