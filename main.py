import os
import datetime


# File storage
file_path_money = "money_income.txt"
file_path_trainee_schedule = "trainee_schedule.txt"

# File Acc
file_path_admin = "admin_acc.txt"
file_path_coaches = "coaches_acc.txt"
file_path_receptionist = "receptionist_acc.txt"
file_path_trainee = "trainee_acc.txt"

# Sport
sports = ["pingpong", "badminton", "football",
          "volleyball", "swimming", "pickleball"]

# Register and login
main_menu_options = ["Log In", "Quit"]

# Admin page -ivan
admin_options = ["Register Coaches", "Delete Coaches",
                 "Register Receptionist", "Delete receptionist", "View Montly Income", "Store Money Income", "Update Profile", "Login Out", "Quit"]

# Receptionist page - yewcheng
receptionist_options = ["Regiter Trainee",
                        "Update Trainning", "Payment", "Generate Receipt", "Request", "Update Profile", "Login Out", "Quit"]

# Coach page - mun chong
coach_options = ["Add Training Programs", "Update Training Program",
                 "Delete Training Program", "View the list of trainees", "Update Profile", "Login Out", "Quit"]

# Trainee page - lewen
trainee_options = ["View schedule", "Change Training program",
                   "View payment", "Update Profile", "Login Out", "Quit"]

update_profile_options = ["Change Username", "Change Password",
                          "Change Email", "Change Age", "Change Contact Number", "Quit "]


print("=" * 50)
print("Brilliant Sport-Training Centre(BSTC)")
print("=" * 50)


def main_menu():

    while True:
        # main_menu_options = ["Log In", "Register", "Quit"]
        for i, main_menu_option in enumerate(main_menu_options, start=1):
            print(f"[{i}]. {main_menu_option}")

        main_menu_choice = input("Enter your choice (1-2): ")

        if main_menu_choice == "1":  # Log in
            clear_screen()
            login_page()

        elif main_menu_choice == "2":
            print("Thank you for using Brilliant Sport-Training Centre, Goodbye!")
            return
        else:
            clear_screen()
            print("Invalid choice...please choose number between 1 to 2")
            continue
        return False


def login_page():
    while True:
        login_attempts = 3

        while login_attempts > 0:
            print("Please follow the instruction to login:")
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            logged_in = False

            # Check admin
            if os.path.exists(file_path_admin) and login_acc(file_path_admin, username, password):
                admin()
                logged_in = True

            # Check coaches
            elif os.path.exists(file_path_coaches) and login_acc(file_path_coaches, username, password):
                coach()
                logged_in = True

            # Check receptionist
            elif os.path.exists(file_path_receptionist) and login_acc(file_path_receptionist, username, password):
                receptionist()
                logged_in = True

            # Check trainee
            elif os.path.exists(file_path_trainee) and login_acc(file_path_trainee, username, password):
                trainee()
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


# ======== Admin


def admin():
    # ["Register Coaches", "Delete Coaches","Register Receptionist", "Delete receptionist", "View Montly Income", "Store Money Income", "Update profile",  "Login Out", "Quit"]
    clear_screen()
    while True:

        print("Welcome to Admin Sport-Training Centre Management System")

        for i, admin_option in enumerate(admin_options, start=1):
            print(f"[{i}]. {admin_option}")

        user_input = input("Enter your choice (1-9): ")

        if user_input == "1":  # Register Coaches
            register_acc(file_path_coaches)

        elif user_input == "2":  # Delete Coaches
            admin_delete_coaches()

        elif user_input == "3":  # Register Receptionist
            register_acc(file_path_receptionist)

        elif user_input == "4":  # Delete receptionist
            admin_delete_receptionist()

        elif user_input == "5":  # View Montly Income
            view_montly_income()

        elif user_input == "6":  # Store Money Income
            store_montly_income()

        elif user_input == "7":  # Update Profile
            update_profile(file_path_admin)

        elif user_input == "8":  # Login Out
            print("Logging Out....")
            clear_logout()
            return

        elif user_input == "9":
            clear_screen()  # Quit
            print(
                "Thank you for using Admin Sport-Training Centre Management System..Good Bye!")
            exit()
        else:
            clear_screen()
            print("Invalid number..Please try again....\n\n")


def admin_delete_coaches():

    while True:
        coaches_id = input(
            "Enter the coach's TP that you want to remove: TP ").strip()
        with open(file_path_coaches, 'r') as f:
            lines = f.readlines()

            if not lines:
                print("No coaches found....")
                admin_register = input(
                    "Do you want to register coaches right now(y/n)").lower().strip()
                if admin_register == "y":
                    admin_register_coaches()
                    return

                elif admin_register == "n":
                    admin()

                else:
                    print("Invalid Answer, please try again")
            else:
                with open(file_path_coaches, 'w') as f:
                    for line in lines:
                        data = line.strip().split(" | ")

                        if data[3] == coaches_id:
                            f.write(line)

                clear_screen()
                print("=" * 50)
                print(f"Coaches TP {coaches_id} has been deleted.")
                return


def admin_delete_receptionist():
    while True:

        receptionist_id = input(
            "Enter the receptionist's TP that you want to remove: ").strip()
        with open(file_path_receptionist, 'r') as f:
            lines = f.readlines()

            if not lines:
                print("No receptionist found....")
                admin_register = input(
                    "Do you want to register receptionist right now(y/n)").lower().strip()
                if admin_register == "y":
                    admin_register_receptionist()
                    return

                elif admin_register == "n":
                    admin()

                else:
                    print("Invalid Answer, please try again")

            else:
                with open(file_path_receptionist, 'w') as f:
                    for line in lines.readlines():
                        data = line.split(" | ")
                        if data[3] == receptionist_id:
                            f.write(line)

                clear_screen()
                print("=" * 50)
                print(f"Coaches TP {receptionist_id} has been deleted.")
                return


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

        clear_screen()
        print("=" * 50)
        print("Store Successful!")


def view_montly_income():

    while True:

        with open(file_path_money, 'r') as income_file:
            for line in income_file:
                data = line.strip().split(" | ")
                print("=" * 60)
                print(
                    f"Money:RM {data[0]} | Month: {data[1]} | Time: {data[2]} | Year: {data[3]}")
                print("=" * 60)

        user_input = input("Please enter q to quit the view: ").lower().strip()

        if user_input == "q":
            clear_screen()
            return
        else:
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


def coach():
    print("Coach menu....")

# ========  Trainee


def trainee():
    print("Trainee menu...")

# ========  Function


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


def login_acc(file_path, username, password):  # login page
    if not os.path.exists(file_path):
        return False
    with open(file_path, 'r') as f:
        for line in f:
            data = line.strip().split(" | ")
            if username == data[0] and password == data[1]:
                clear_screen()
                print("Login Successful")
                return True
    return False


def register_acc(file_path):
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
                "TP" + acc_id + " | " + str(age) + " | " + contact_number + " | " + sport_choice + "\n")
    clear_screen()
    print("-" * 50)
    print("Register Successful!")


def update_profile(file_path):

    password_length = 8
    min_age = 18
    max_age = 80
    min_contact_num = 8
    max_contact_num = 9

    # update_profile_options = ["Change Username", "Change Password", "Change Email", "Change Age" "Change Contact Number", "Quit"]
    while True:

        clear_screen()

        for i, update_profile_option in enumerate(update_profile_options, start=1):
            print(f"{i}. {update_profile_option}")

        user_input = input("Enter your choice (1-6): ")

        if user_input == "1":  # new username
            while True:
                new_username = input("Enter your new username: ").strip()

                if not new_username.isalpha():
                    print("Invalid name..Please make sure name is alphabet")
                    continue
                else:
                    break

            with open(file_path, 'r') as f:
                lines = f.readlines()

            with open(file_path, 'w') as f:
                for line in lines:
                    data = line.strip().split(" | ")
                    data[0] = new_username
                    f.write(" | ".join(data) + "\n")

            print(f"Successfully changed username to {new_username}")

        elif user_input == "2":  # new password
            while True:
                new_password = input("Enter your new password: ").strip()

                if len(new_password) < password_length:
                    print(f"Password must be at least {password_length} word")
                    continue

                else:
                    clear_screen()
                    break

            with open(file_path, 'r') as f:
                lines = f.readlines()

            with open(file_path, 'w') as f:
                for line in lines:
                    data = line.strip().split(" | ")
                    data[1] = new_password
                    f.write(" | ".join(data) + "\n")

            print(f"Successfully changed password to {new_password}")

        elif user_input == "3":  # new email
            while True:
                new_email = input("Enter your new password: ").strip()

                if not new_email.lower().endswith("@gmail.com"):
                    print("Invalid Email..Please try again")
                    continue
                else:
                    clear_screen()
                    break

            with open(file_path, 'r') as f:
                lines = f.readlines()

            with open(file_path, 'w') as f:
                for line in lines:
                    data = line.strip().split(" | ")
                    data[2] = new_email
                    f.write(" | ".join(data) + "\n")

            print(f"Successfully changed email to {new_email}")

        elif user_input == "4":  # new age

            while True:
                new_age = input("Enter your new age: ").strip()

                if not new_age.isdigit():
                    print("Age must be a number")
                    continue

                age = int(new_age)

                if min_age <= age <= max_age:
                    clear_screen()
                    break
                else:
                    print(f"Age must be between {min_age} to {max_age}")

            with open(file_path, 'r') as f:
                lines = f.readlines()

            with open(file_path, 'w') as f:
                for line in lines:
                    data = line.strip().split(" | ")
                    data[4] = str(age)
                    f.write(" | ".join(data) + "\n")

            print(f"Successfully changed age to {age}")

        elif user_input == "5":  # new contact number
            while True:
                new_contact_number = input("Enter coach contact number: +60 ")
                if not new_contact_number.isdigit():
                    print("Invalid contact number")
                    continue

                if min_contact_num <= len(new_contact_number) <= max_contact_num:
                    clear_screen()
                    break
                else:
                    print("Invalid phone number...please try again")
                    continue

            with open(file_path, 'r') as f:
                lines = f.readlines()

            with open(file_path, 'w') as f:
                for line in lines:
                    data = line.strip().split(" | ")
                    data[0] = new_contact_number
                    f.write(" | ".join(data) + "\n")

            print(
                f"Successfully changed contact number to {new_contact_number}")

        elif user_input == "6":
            clear_screen()
            return
        else:
            print("Invalid number.Please try again...")


# start system
main_menu()
