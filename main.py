import os
import datetime


# File storage
file_path_money = "money_income.txt"
file_path_trainee_schedule = "trainee_schedule.txt"
file_path_admin = "admin_acc.txt"
file_path_coaches = "coaches_acc.txt"
file_path_receptionist = "receptionist_acc.txt"
file_path_trainee = "trainee_acc.txt"

# Options
sports_options = ["pingpong", "badminton", "football",
                  "volleyball", "swimming", "pickleball"]

main_menu_options = ["Log In", "Quit"]

admin_options = ["Register Coaches", "Delete Coaches",
                 "Register Receptionist", "Delete receptionist", "View Montly Income", "Store Money Income", "Update Profile", "Login Out", "Quit"]

receptionist_options = ["Regiter Trainee",
                        "Update Trainning", "Payment", "Generate Receipt", "Request", "Update Profile", "Login Out", "Quit"]

coaches_options = ["Add Training Programs", "Update Training Program",
                   "Delete Training Program", "View the list of trainees", "Update Profile", "Login Out", "Quit"]

trainee_options = ["View schedule", "Change Training program",
                   "View payment", "Update Profile", "Login Out", "Quit"]

update_profile_options = ["Change Username", "Change Password",
                          "Change Email", "Change Age", "Change Contact Number", "Quit "]

# Functions


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 50)
    print("Brilliant Sport-Training Centre(BSTC)")
    print("=" * 50)


def clear_logout():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 50)
    print("Brilliant Sport-Training Centre(BSTC)")
    print("=" * 50)
    print("Loging out...")
    print("Login Successful...")


def input_alpha(username):
    while True:
        user_input = input(username).strip()
        if user_input.isalpha():
            return user_input
        print("Invalid input. Only alphabert allow")


def input_int(num, min_num=None, max_num=None):
    while True:
        user_input = input(num)
        if user_input.isdigit():
            num = int(user_input)
            if min_num is not None and num < min_num:
                print(f"Value must be >= {min_val}")
                continue
            if max_num is not None and num > max_num:
                print(f"Value must be <= {max_val}")
                continue
            return num
        print("Invalid input. Only digits allowed.")


def input_email(email):
    while True:
        user_input = input(email).strip()

        if user_input.endswith("@gmail.com"):
            return user_input
        print("Invalid input. Must end with @gmail.com")


def input_sport():
    while True:

        for s in sports_options:
            print(f"-{s}")
        sport_choice = input(
            "Please Assign sport(s) (separate with comma): ").lower().strip()

        chosen_sports = [s.strip() for s in sport_choice.split(",")]

        invalid_sports = [
            s for s in chosen_sports if s not in sports_options]

        if invalid_sports:
            print("Invalid sport(s):", ", ".join(invalid_sports))
            print("Please try again...")
        else:
            return True


# Accounts Functions


def login_acc(file_path, username, password):  # login page
    if not os.path.exists(file_path):
        return False
    with open(file_path, 'r') as f:
        for line in f:
            data = line.strip().split(" | ")
            if username == data[0] and password == data[1]:
                clear_screen()
                print("Login Successful")
                login_acc_id = data[3]
                return login_acc_id
    return None


def register_acc(file_path, role=""):
    clear_screen()
    print(f"--Register {role}---")
    name = input_alpha("Enter username: ").strip()
    password = input("Enter password (min 8 character): ").strip()
    while len(password) < 8:
        print("Password too short")
        password = input("Enter password (min 8 character): ")
    email = input_email("Enter email(must in @gmail.com): ")
    acc_id = input("Enter account's ID: TP")
    age = input_int("Enter age: ", 18, 80)
    contact = input_int("Enter contact number: +60 ",
                        10000000, 999999999)
    sport = input_sport()
    with open(file_path, 'a') as f:
        line = f"{name} | {password} | {email} | {acc_id} | {str(age)} | {contact} | {sport}\n"
        f.write(line)
    print(f"---{role} Register Successful!---")


def delete_acc(file_path):
    if not os.path.exists(file_path):
        print("No account found")
        return
    target = input("Enter ID to delete (eg TP200): ").strip()
    if not target.upper().startswith("TP"):
        target = "TP" + target

    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as f:
        for line in lines:
            if not line.strip():
                deleted = False
                continue

            parts = [s.strip() for s in line.strip().split("|")]
            if len(parts) < 2:
                f.write(line)
                continue

            coach_tp = parts[3]
            if coach_tp.upper() == target.upper():
                deleted = True
                continue   # skip writing this line

            f.write(line)

    if deleted:
        print("Successful")
    else:
        print("Coach TP not found")


def update_profile(file_path, id_value):
    # update_profile_options = ["Change Username", "Change Password", "Change Email", "Change Age" "Change Contact Number", "Quit"]
    while True:
        clear_screen()

        for i, update_profile_option in enumerate(update_profile_options, start=1):
            print(f"{i}. {update_profile_option}")
        user_input = input("Enter choice: ")

        if user_input == "6":
            return

        with open(file_path, 'r') as f:
            lines = f.readlines()

        with open(file_path, 'w') as f:
            for line in lines:
                data = line.strip().split(" | ")
                if data[3] == id_value:

                    if user_input == "1":
                        data[0] = input_alpha("Enter new name: ").strip()
                        print(f"Successfully changed username to {data[0]}")

                    elif user_input == "2":
                        new_password = input(
                            "Enter new password (min 8 character): ").strip()
                        while len(password) < 8:
                            print("Password too short")
                            new_password = input(
                                "Enter new password (min 8 character): ")
                        data[1] = new_password
                        print(f"Successfully changed password to {data[1]}")

                    elif user_input == "3":
                        data[2] = input_email(
                            "Enter new email(must in @gmail.com): ").strip()
                        print(f"Successfully changed email to {data[2]}")

                    elif user_input == "4":
                        data[4] = input_age("Enter your new age: ", 18, 50)

                        print(f"Successfully changed age to {str(data[4])}")

                    elif user_input == "5":
                        data[5] = input_int(
                            "Enter new contact number: +60 ")
                        print(
                            f"Successfully changed contact number to {data[5]}")
                    f.write(" | ".join(data) + "\n")
                else:
                    f.write(line)

    print("Invalid number.Please try again...")

# Main page


def main_menu():
    clear_screen()
    while True:
        # main_menu_options = ["Log In", "Register", "Quit"]
        for i, main_menu_option in enumerate(main_menu_options, start=1):
            print(f"[{i}]. {main_menu_option}")

        main_menu_choice = input("Enter choice (1-2): ")

        if main_menu_choice == "1":  # Log in
            login_page()

        elif main_menu_choice == "2":
            print("Thank you for using Brilliant Sport-Training Centre, Goodbye!")
            return
        else:
            print("Invalid choice...please choose number between 1 to 2")


def login_page():
    while True:
        login_attempts = 3

        while login_attempts > 0:
            print("Please follow the instruction to login")
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()

            logged_in = False

            # Admin
            if os.path.exists(file_path_admin):
                id_value = login_acc(file_path_admin, username, password)
                if id_value:
                    admin(id_value)
                    logged_in = True

            # Coaches
            if os.path.exists(file_path_coaches):
                id_value = login_acc(file_path_admin, username, password)
                if id_value:
                    coach(id_value)
                    logged_in = True

            # Check receptionist
            if os.path.exists(file_path_receptionist):
                id_value = login_acc(file_path_admin, username, password)
                if id_value:
                    receptionist(id_value)
                    logged_in = True

            # Check trainee
            if os.path.exists(file_path_trainee):
                id_value = login_acc(file_path_admin, username, password)
                if id_value:
                    trainee(id_value)
                    logged_in = True

            if logged_in:
                break

            login_attempts -= 1
            print("Invalid password or username...Please try again")
            print(f"Attempts left: {login_attempts}")

        if not logged_in:
            print("Login failed...Please try again later...")

        again = input("Do you want to login again? (y/n): ").lower().strip()
        if again != 'y':
            print(
                "Thank you for using Sport-Training Centre Management System..Good Bye!")
            break


# Admin Page


def admin(id_value):
    # ["Register Coaches", "Delete Coaches","Register Receptionist", "Delete receptionist", "View Montly Income", "Store Money Income", "Update profile",  "Login Out", "Quit"]
    clear_screen()
    while True:

        print("\n---Welcome to Admin Menu---")

        for i, admin_option in enumerate(admin_options, start=1):
            print(f"[{i}]. {admin_option}")

        user_input = input("Enter your choice (1-9): ")

        if user_input == "1":  # Register Coaches
            register_acc(file_path_coaches, "Coaches")

        elif user_input == "2":  # Delete Coaches
            delete_acc(file_path_coaches)

        elif user_input == "3":  # Register Receptionist
            register_acc(file_path_receptionist, Receptionist)

        elif user_input == "4":  # Delete receptionist
            delete_acc(file_path_receptionist)

        elif user_input == "5":  # View Montly Income
            view_montly_income()

        elif user_input == "6":  # Store Money Income
            store_montly_income()

        elif user_input == "7":  # Update Profile
            update_profile(file_path_admin, id_value)

        elif user_input == "8":  # Login Out
            print("Logging Out....")
            clear_logout()
            return

        elif user_input == "9":
            print(
                "Thank you for using Admin Sport-Training Centre Management System..Good Bye!")
            exit()
        else:
            clear_screen()
            print("Invalid number..Please try again....")


def store_montly_income():
    date = datetime.datetime.now()

    money_income = input("Please enter money income: RM ")
    month = date.strftime("%B")
    day = date.strftime("%A")
    time = date.strftime("%H:%M:%S")
    year = date.strftime("%Y")

    with open(file_path_money, 'a') as income_file:
        income_file.write(str(money_income) + " | " +
                          month + " | " +
                          time + " | " + year + "\n")
    print("---Store Successful---")


def view_montly_income():
    if not os.path.exists(file_path_money):
        print("No records found")

    with open(file_path_money, 'r') as f:
        for line in f:
            data = line.strip().split(" | ")
            print(
                f"Money:RM {data[0]} | Month: {data[1]} | Time: {data[2]} | Year: {data[3]}")

    user_input = input("Please enter q to quit the view: ").lower().strip()

    if user_input == "q":
        return
    print("Invalid choice.Please try again...")

# ========  Receptionist


def receptionist():

    # ["Regiter Trainee", "Update Trainning", "Payment", "Generate Receipt", "Request", "Update Profile", "Login Out", "Quit"]
    clear_screen()
    while True:
        print("Welcome to Receptionist Sport-Training Centre Management System")

        for i, receptionist_option in enumerate(receptionist_options, start=1):
            print(f"{i}, {receptionist_option}")

        user_input = input("Enter your choice (1-8)")

        if user_input == "1":
            receptionist_register_trainee()

        elif user_input == "2":
            receptionist_update_trainning()

        elif user_input == "3":
            receptionist_payment()

        elif user_input == "4":
            receptionist_generate_receipt()

        elif user_input == "5":
            receptionist_request()

        elif user_input == "6":
            update_profile(file_path_receptionist)

        elif user_input == "8":  # Login Out
            print("Logging Out....")
            clear_logout()
            return

        elif user_input == "9":
            clear_screen()  # Quit
            print(
                "Thank you for using Receptionist Sport-Training Centre Management System..Good Bye!")
            exit()
        else:
            clear_screen()
            print("Invalid number..Please try again....\n\n")


def receptionist_register_trainee():
    clear_screen()
    password_length = 8
    min_age = 18
    max_age = 80
    min_contact_num = 8
    max_contact_num = 9

    while True:
        name = input("Please enter name: ")

        if not name.isalpha():
            print("Invalid name..Please make sure name is alphabet")
            continue
        else:
            break

    while True:
        password = input("Please enter a new password: ")

        if len(password) < password_length:
            print(f"Password must be at least {password_length} word")
            continue

        else:
            break
    while True:
        email = input("Please enter email address: ")

        if not email.lower().endswith("@gmail.com"):
            print("Invalid Email..Please try again")
            continue
        else:
            break

    acc_id = input("Please register new ID: TP ")

    while True:
        age = input("Please enter age: ")

        if not age.isdigit():
            print("Age must in number")
            continue

        age = int(age)

        if min_age <= age <= max_age:
            break
        else:
            print(f"Age must be between {min_age} to {max_age}")
            continue

    while True:
        contact_number = input("Please enter contact number: +60 ")
        if not contact_number.isdigit():
            print("Invalid contact number")
            continue

        if min_contact_num <= len(contact_number) <= max_contact_num:
            break
        else:
            print("Invalid phone number...please try again")
            continue

    while True:

        for i, sport in enumerate(sports, start=1):
            print(f"{i}. {sport}")
        sport_choice = input(
            "Please Assign sport(s) (separate with comma): ").lower().strip()

        chosen_sports = [s.strip() for s in sport_choice.split(",")]

        invalid_sports = [s for s in chosen_sports if s not in sports]

        if invalid_sports:
            print("Invalid sport(s):", ", ".join(invalid_sports))
            print("Please try again...")
        else:
            break

    with open(file_path, 'a') as f:
        f.write(name + " | " + password + " | " + email + " | " +
                "TP" + acc_id + " | " + str(age) + " | " + contact_number + " | " + sport_choice + " | " + "unpaid" + "\n")
    clear_screen()
    print("-" * 50)
    print("Register Successful!")


def update_trainning():
    print("Comming Soon")


def payment():
    print("Comming Soon")


def generate_receipt():
    print("Comming Soon")


def request():
    print("Comming Soon")


# ========  Coach
File = "coach_program.txt"


def coach():
    # ["Add Training Programs", "Update Training Program", "Delete Training Program", "View the list of trainees", "Update Profile", "Login Out", "Quit"]
    while True:
        print("\n---Welcome to Coach Sport-Training Centre Management System---")
        for i, coaches_option in enumerate(coaches_options, start=1):
            print(f"[{i}]. {admin_option}")

        choice = input("Choice: ")

        if choice == "1":
            add_program()

        elif choice == "2":
            update_program()

        elif choice == "3":
            delete_program()

        elif choice == "4":
            view_program()

        elif choice == "5":
            update_profile(file_path_coaches)

        elif user_input == "6":  # Login Out
            print("Logging Out....")
            clear_logout()
            return

        elif choice == "7":
            clear_screen()  # Quit
            print(
                "Thank you for using Admin Sport-Training Centre Management System..Good Bye!")
            exit()
        else:
            clear_screen()
            print("Invalid Answer, please try again")

# adding program coach


def add_program():
    coach_program = "coach_program.txt"

    while True:

        name = input("Program Name: ")
        if not name.isalpha():
            print("Invalid name..Please make sure name is alphabet")
            continue
        else:
            break
        break

    while True:

        charge = input("Charge: RM")
        if not charge.isdecimal():
            print("Invalid charges..Please make sure it is a number")
            continue
        else:
            break
        break

    while True:

        date = input("Date (DD/MM/YYYY): ")

        try:
            datetime.strptime(date, "%d/%m/%Y")
            print("date saved")
            break
        except ValueError:
            print("Invalid date. Please use DD/MM/YYYY")

    while True:
        time = input("Time (2400 format): ")
        if time.isdigit() and len(time) == 4:
            h = int(time[:2])
            m = int(time[2:])
            if 0 <= h <= 23 and 0 <= m <= 59:
                break
        print("Invalid time, please rewrite it in form of 2400.")

    while True:

        record = name + "|" + charge + "|" + date + "|" + time + "\n"

        with open(coach_program, "a") as file:
            file.write(record)

            print("Program added successfully.")
        return


# update program
def update_program():
    if not os.path.exists(File):
        print("No file found.")
        return

    target = input("Enter program name to update: ")
    updated = False
    new_lines = []

    with open(File, "r") as f:
        for line in f:
            name, charge, date, time = line.strip().split("|")
            if name.lower() == target.lower():
                print("Program found. Enter new details.")

                new_charge = input("New charge: RM ")
                new_date = input("New date (DD/MM/YYYY): ")
                new_time = input("New time (2400): ")

                new_lines.append(
                    f"{name}|{new_charge}|{new_date}|{new_time}\n")
                updated = True
            else:
                new_lines.append(line)

    with open(File, "w") as f:
        f.writelines(new_lines)

    if updated:
        print("Program updated successfully.")
    else:
        print("Program not found.")


# delete program
def delete_program():
    if not os.path.exists(File):
        print("No file found.")
        return

    target = input("Enter program name to delete: ")
    deleted = False
    new_lines = []

    with open(File, "r") as f:
        for line in f:
            name = line.split("|")[0]
            if name.lower() == target.lower():
                deleted = True
            else:
                new_lines.append(line)

    with open(File, "w") as f:
        f.writelines(new_lines)

    if deleted:
        print("Program deleted successfully.")
    else:
        print("Program not found.")

# view program


def view_program():
    if not os.path.exists(File):
        print("No programs found.")
        return

    with open(File, "r") as f:
        print("\n--- PROGRAM LIST ---")
        for line in f:
            name, charge, date, time = line.strip().split("|")
            print(
                f"Programe name: {name}, RM{charge}, Date: {date}, Time: {time}")

# ========  Trainee


def trainee():
    print("Trainee menu...")


# start system
main_menu()
