from connect import get_connection


def show_table():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM profesores')
        teachers = cursor.fetchall()
        if not teachers:
            print('Teachers table is empty')
        for teacher in teachers:
            print(teacher)
        print("---------------------------------")
        print(f"Total profesores: {len(teachers)}")
        print("---------------------------------")
    finally:
        conn.close()

def insert_teacher():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        name = input('Enter the name of the new teacher: ')
        cursor.execute('INSERT INTO profesores (name) VALUES (%s)', (name,))
        conn.commit()
    finally:
        conn.close()    

def menu():
    print(" === MENU === ")
    print("1. Show teachers")
    print("2. Insert new teacher")
    print("3. Exit")
    
    option = input("Select option: ")
    if option == '1':
        show_table()
    elif option == '2':
        insert_teacher()
    elif option == '3':
        exit()
        print("Exit")
    else:
        print("Invalid option")

if __name__ == "__main__":
    while True:
        menu()