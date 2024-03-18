import psycopg2

#estbalishing connection with database server
con = psycopg2.connect(
    database="University",
    user="postgres",
    password="37293",
    host="localhost",
    port= '5432'
    )

cursor_obj = con.cursor()

#displays all students and their attributes
def get_all_students():
    cursor_obj.execute("SELECT * FROM students")
    result = cursor_obj.fetchall()
    for student in result:
        print(student)

#adds a new student from given first and last name, email and enrollment date
def add_student(first_name, last_name, email, enrollment_date):
    cursor_obj.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
    con.commit()
    print("Student added.")

#updates student email using given student id and updated email
def update_email(id, email):
    cursor_obj.execute("UPDATE students SET email = %s WHERE student_id = %s", (email, id))
    con.commit()
    print("Student email updated.")

#deletes student using given student id
def delete_student(id):
    cursor_obj.execute("DELETE FROM students WHERE student_id = %s", (id,))
    con.commit()
    print("Student deleted.")

#repeatedly displays menu till user chooses to exit. displays database operations.
def start_menu():
    choice = 0

    while(choice != 5):
        print("MENU",
            "\n1. Display all students",
            "\n2. Add a new student",
            "\n3. Update email",
            "\n4. Delete student records",
            "\n5. Exit")

        choice = input("Select (1/2/3/4/5): ")

        if (choice == '1'):
            get_all_students()

        elif (choice == '2'):
            print("Student details required -")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            add_student(first_name, last_name, email, enrollment_date)

        elif (choice == '3'):
            print("Student details required -")
            id = input("Enter student id: ")
            email = input("Enter new email: ")
            update_email(id, email)

        elif (choice == '4'):
            print("Student details required -")
            id = input("Enter id for student to be deleted: ")
            delete_student(id)

        elif (choice == '5'):
            exit()

        else:
            print("Invalid selection")

start_menu()

