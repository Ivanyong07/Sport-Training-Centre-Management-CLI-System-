import os
import datetime

# File storage
file_path_money = "money_income.txt"
file_path_trainee_schedule = "trainee_schedule.txt"
file_path_admin = "admin_acc.txt"
file_path_coaches = "coaches_acc.txt"
file_path_receptionist = "receptionist_acc.txt"
file_path_trainee = "trainee_acc.txt"
file_path_request = "request.txt"
file_path_receipt = "receipt.txt"

# Options
sports_options = ["pingpong", "badminton",
                  "volleyball", "swimming", "pickleball", "football", "hockey", "cricket"]

main_menu_options = ["Log In", "Quit"]

admin_options = ["Register Coaches", "Delete Coaches",
                 "Register Receptionist", "Delete receptionist", "View Montly Income", "Store Money Income", "Update Profile", "Log Out", "Quit"]

receptionist_options = ["Register Trainee", "Delete Trainee",
                        "Update Trainning", "Payment", "Generate Receipt", "Request", "Update Profile", "Log Out", "Quit"]

coaches_options = ["Add Training Programs", "Update Training Program",
                   "Delete Training Program", "View Trainees", "Update Profile", "Log Out", "Quit"]

trainee_options = ["View schedule", "View payment",
                   "Request Change Training Program", "Update Profile", "Log Out", "Quit",]

update_profile_options = ["Change Username", "Change Password",
                          "Change Email", "Change Age", "Change Contact Number", "Change IC or Passport", "Change Nationality", "Change Langauge", "Back"]

send_requests = ["Send Request", "Delete Request", "Update Request", "Back"]

# Functions
width = 90


def clear_screen():

    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * width)
    print(f"{'Brilliant Sport-Training Centre(BSTC)':^80}")
    print("=" * width)


def clear_logout():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * width)
    print(f"Brilliant Sport-Training Centre(BSTC)")
    print("=" * width)
    print("Logging out...")
    print("Log out Successful...")


def input_alpha(username):
    min_name = 1

    while True:
        user_input = input(username).strip()
        if user_input.isalpha() and len(user_input) >= min_name:
            return user_input
        print("Only alphabet allowed")


def input_int(num, min_num=None, max_num=None):  # for range such as fee, phone number

    while True:
        user_input = input(num)
        try:
            val = int(user_input)

            if min_num is not None and val < min_num:
                print(f"Value must be >= {min_num}")
                continue

            elif max_num is not None and val > max_num:
                print(f"Value must be <= {max_num}")
                continue
            return str(val)  # return as string as file only accept string
        except ValueError:
            print("Error. Only number allowed")


def input_email(email):

    while True:
        user_input = input(email).strip()

        if "@" in user_input and user_input.endswith(".com"):
            return user_input
        print("Invalid input. Must contain with @ and .com")


def input_id(user_input):

    user_id = input(user_input).strip().upper()
    if not user_id.startswith("TP"):
        user_id = "TP" + user_id
    return user_id


def input_sport(sport):

    while True:

        for s in sports_options:
            print(f"-{s}")
        sport_choice = input(sport).lower().strip()
        chosen_sports = []
        invalid_sports = []

        chosen_sports = [s.strip() for s in sport_choice.split(",")]
        invalid_sports = [
            s for s in chosen_sports if s not in sports_options]

        if invalid_sports:
            print("Invalid sport(s):", ", ".join(invalid_sports))
            print("Please try again...")
        else:
            return sport_choice


def input_date(date):

    while True:
        enter_date = input(date)
        try:
            datetime.datetime.strptime(enter_date, "%d/%m/%Y")
            print("Date saved")
            return enter_date
        except ValueError:
            print("Invalid date. Please use DD/MM/YYYY (e.g 04/05/2025)")


def input_time(time):
    open_time = 900
    closed_time = 2200

    while True:
        enter_time = input(time)
        if enter_time.isdigit() and len(enter_time) == 4:
            h = int(enter_time[:2])
            m = int(enter_time[2:])
            if 0 <= h <= 23 and 0 <= m <= 59:
                time_val = int(enter_time)
                if time_val < open_time:
                    print("We haven't opened yet (operating time is 09.00 ~ 22.00)")
                elif time_val > closed_time:
                    print("We already closed (operating time is 09.00 ~ 22.00)")
                else:
                    return str(enter_time)
            else:
                print("Invalid clock time. Hours 00-23, Minutes 00-59.")
        else:
            print("Invalid time, please rewrite it in form of 2400 (e.g 2130).")


def time_conflict(start_time, end_time):

    min_time = 30
    s_time = int(start_time)
    e_time = int(end_time)

    if s_time >= e_time:
        print("\n[!] Error: Start time cannot be later than or equal to End time.")
        print(f"    (Entered: {s_time} - {e_time})")
        return True

    if (e_time - s_time) < min_time:
        print("[!] Error: Session must be at least 30 minutes long.")
        return True

    return False

# Accounts Functions


def check_id_exists(file_path, new_id):

    try:
        with open(file_path, 'r') as f:
            for line in f:
                data = [s.strip() for s in line.strip().split("|")]
                if len(data) >= 6 and data[3].upper() == new_id:
                    return True
    except FileNotFoundError:
        return False


def update_schedule_data(trainee_id, new_name):
    if not os.path.exists(file_path_trainee_schedule):
        return
    with open(file_path_trainee_schedule, 'r') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        parts = line.strip().split(" | ")
        if len(parts) >= 9 and parts[3] == trainee_id:
            parts[2] = new_name
            lines[i] = " | ".join(parts) + "\n"
    with open(file_path_trainee_schedule, 'w') as f:
        f.writelines(lines)


def login_acc(file_path, username, password):  # login page
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("---File not found---")
        return

    for line in lines:
        data = line.strip().split(" | ")
        if len(data) >= 4:
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
    email = input_email("Enter email(e.g xxx@xxx.com): ")
    while True:
        now = datetime.datetime.now()
        unique_id = "TP" + now.strftime("%d%H%M%S")
        if check_id_exists(file_path, unique_id):
            continue
        else:
            break
    age = input_int("Enter age: ", min_num=18, max_num=60)
    contact = input_int("Enter contact number: +60 ",
                        min_num=10000000, max_num=999999999)
    passport_ic = input("Enter your IC or Passport: ")
    national = input("Enter your nationality: ")
    language = input("Enter the language you know (separate with (, ,)): ")
    sport = input_sport("Enter your sport(separate with (, ,)): ")
    with open(file_path, 'a') as f:
        line = f"{name} | {password} | {email} | {unique_id} | {str(age)} | +60{contact} | {passport_ic} | {national} | {language} | {sport}\n"
        f.write(line)
    print(f"---{role} Register Successful!---")
    input("\nPress Enter to return to the Admin Menu...")
    clear_screen()


def delete_acc(file_path, role=""):
    clear_screen()
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("---File not found---")
        input("Press Enter to return...")
        return

    print("=" * width)
    print(f"{'Trainee TP':<15} {'Name':<15} {'Email':<20} {'Contact Number':<15}")
    print("=" * width)

    for line in lines:
        parts = [s.strip() for s in line.strip().split("|")]
        if len(parts) >= 4:
            print(
                f"{parts[3]:<15} {parts[0]:<15} {parts[2]:<20} {parts[5]:<15}")

    delete_tp = input(
        f"\nEnter {role}'s ID to delete (eg TP200) or 'q' to quit: ")

    if delete_tp == "q":
        return

    if not delete_tp.startswith("TP"):
        delete_tp = "TP" + delete_tp

    deleted = False
    new_lines = []
    parts = []
    for line in lines:
        parts = [s.strip() for s in line.strip().split("|")]
        if len(parts) >= 4:
            role_id = parts[3].strip()
            if role_id.upper() == delete_tp:

                deleted = True
                continue

        new_lines.append(line)

    if deleted:
        with open(file_path, "w") as f:
            f.writelines(new_lines)
        if "coaches" in file_path or "trainee_acc" in file_path:
            with open(file_path_trainee_schedule, 'r') as s:
                s_lines = s.readlines()
            updated_schd = []
            updated_schd = [l for l in s_lines if l.split(
                " | ")[0] != delete_tp and l.split(" | ")[3] != delete_tp]

            with open(file_path_trainee_schedule, 'w') as s:
                s.writelines(updated_schd)
        print("---Deleted Successful---")
    else:
        print("---{role} TP not found---")
    input(f"\nPress Enter to return to the {role} Menu...")


def update_profile(file_path, id_value):
    # ["Change Username", "Change Password", "Change Email", "Change Age", "Change Contact Number", "Change IC or Passpo", "Change Nationality", "Change Langauge", "Back"]
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("--- File Not Found ---")
        input("Press Enter to return:")
        return
    while True:
        clear_screen()
        for i, update_profile_option in enumerate(update_profile_options, start=1):
            print(f"{i}. {update_profile_option}")
        user_input = input("Enter choice: ")

        if user_input == "9":
            return

        if user_input in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            update = False

            for i in range(len(lines)):
                data = lines[i].strip().split(" | ")
                if len(data) >= 6 and data[3] == id_value:

                    if user_input == "1":
                        data[0] = input_alpha("Enter new name: ").strip()
                        print(f"Successfully changed username to {data[0]}")
                        if "trainee" in file_path:
                            update_schedule_data(id_value, data[0])

                    elif user_input == "2":
                        new_password = input(
                            "Enter new password (min 8 character): ").strip()
                        while len(new_password) < 8:
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
                        data[4] = input_int("Enter your new age: ", 18, 50)

                        print(f"Successfully changed age to {data[4]}")

                    elif user_input == "5":
                        data[5] = input_int(
                            "Enter new contact number: +60 ", min_num=10000000, max_num=999999999)
                        print(
                            f"Successfully changed contact number to {data[5]}")

                    elif user_input == "6":
                        data[6] = input_int(
                            "Enter new IC or Passport: ")
                        print(
                            f"Successfully changed IC or Passport to {data[6]}")

                    elif user_input == "7":
                        data[7] = input(
                            "Enter new Nationality: ")
                        print(
                            f"Successfully changed Nationality to {data[7]}")

                    elif user_input == "8":
                        data[8] = input(
                            "Enter new Language: ")
                        print(
                            f"Successfully changed Language to {data[8]}")

                    lines[i] = " | ".join(data) + "\n"
                    update = True
                    break

            if update:
                with open(file_path, 'w') as f:
                    f.writelines(lines)
                print("--- Profile Updated and Saved ---")
                input("Press enter to continue:")
            else:
                print("Error: User ID not found in file.")
        else:
            print("Invalid number. Please try again...")


def save_receipt(receipt_code, target_id, name, n_date, start_time, end_time, program, fee):
    clear_screen()
    receipt_template = (
        f"{'=' * 50}\n"
        f"{'Your Receipt':^45}\n"
        f"{'Brilliant Sport-Training Centre (BSTC)':^45}\n"
        f"{'(BSTC)':^45}\n"
        f"{'=' * 50}\n"
        f"{'Receipt Code:':<30} {receipt_code}\n"
        f"{'Trainee ID:':<30} {target_id}\n"
        f"{'Name:':<30} {name}\n"
        f"{'Date:':<30} {n_date}\n"
        f"{'Start Training Time:':<30} {start_time}\n"
        f"{'End Training Time:':<30} {end_time}\n"
        f"{'=' * 50}\n"
        f"{'Program:':<30} {program}\n"
        f"{'Total Amount:':<30} RM {float(fee):.2f}\n"
        f"{'=' * 50}\n"
        f"{'--- THANK YOU ---':^45}\n"
    )
    return receipt_template

# Main page


def main_menu():
    clear_screen()
    while True:
        # main_menu_options = ["Log In", "Quit"]
        for i, main_menu_option in enumerate(main_menu_options, start=1):
            print(f"[{i}]. {main_menu_option}")

        main_menu_choice = input("Enter choice (1-2): ")

        if main_menu_choice == "1":
            login_page()

        elif main_menu_choice == "2":
            print("Thank you for using Brilliant Sport-Training Centre, Goodbye!")
            return
        else:
            print("Invalid choice...please choose number between 1 to 2")


def login_page():
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
                return

        # Coaches
        if os.path.exists(file_path_coaches):
            id_value = login_acc(file_path_coaches, username, password)
            if id_value:
                coach(id_value)
                logged_in = True
                return

        # Check receptionist
        if os.path.exists(file_path_receptionist):
            id_value = login_acc(
                file_path_receptionist, username, password)
            if id_value:
                receptionist(id_value)
                logged_in = True
                return

        # Check trainee
        if os.path.exists(file_path_trainee):
            id_value = login_acc(file_path_trainee, username, password)
            if id_value:
                trainee(id_value)
                logged_in = True
                return

        login_attempts -= 1
        print("Invalid password or username...Please try again")
        print(f"Attempts left: {login_attempts}")

    print("Login failed...Please try again later...")
    exit()


# Admin Page
def admin(id_value):
    # ["Register Coaches", "Delete Coaches","Register Receptionist", "Delete receptionist", "View Montly Income", "Store Money Income", "Update profile",  "Login Out", "Quit"]
    while True:
        clear_screen()
        print("\n---Welcome to Admin Menu---")

        for i, admin_option in enumerate(admin_options, start=1):
            print(f"[{i}]. {admin_option}")

        user_input = input("Enter your choice (1-9): ")

        if user_input == "1":  # Register Coaches
            register_acc(file_path_coaches, "Coaches")

        elif user_input == "2":  # Delete Coaches
            delete_acc(file_path_coaches, "Coaches")

        elif user_input == "3":  # Register Receptionist
            register_acc_receptionist(file_path_receptionist, "Receptionist")

        elif user_input == "4":  # Delete receptionist
            delete_acc(file_path_receptionist, "Receptionist")

        elif user_input == "5":  # View Montly Income
            view_money_income()

        elif user_input == "6":  # Store Money Income
            store_monthly_income()

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


def register_acc_receptionist(file_path, role=""):
    clear_screen()
    print(f"--Register {role}---")
    name = input_alpha("Enter username: ").strip()
    password = input("Enter password (min 8 character): ").strip()
    while len(password) < 8:
        print("Password too short")
        password = input("Enter password (min 8 character): ")
    email = input_email("Enter email(must end in @gmail.com): ")
    while True:
        now = datetime.datetime.now()
        unique_id = "TP" + now.strftime("%d%H%M%S")
        if check_id_exists(file_path, unique_id):
            print("Error: This ID already exists. Registration cancelled.")
            continue
        else:
            break
    age = input_int("Enter age: ", min_num=18, max_num=60)
    contact = input_int("Enter contact number: +60 ",
                        min_num=10000000, max_num=999999999)
    passport_ic = input("Enter your IC or Passport: ")
    national = input("Enter your nationality: ")
    language = input("Enter the language you know: ")
    with open(file_path, 'a') as f:
        line = f"{name} | {password} | {email} | {unique_id} | {str(age)} | +60{contact} | {passport_ic} | {national} | {language}\n"
        f.write(line)
    print(f"---{role} Register Successful!---")
    input("\nPress Enter to return to the Admin Menu...")
    clear_screen()


def store_monthly_income():
    date = datetime.datetime.now()
    time = date.strftime("%H:%M:%S")
    s_date = date.strftime("%d/%B/%Y")

    trainee_id = input_id("Enter Trainee ID: ")

    money_income = input_int("Please enter money income: RM ")
    program_name = input_sport("Please enter program name: ")
    while True:
        payment_method = input("Paid by cash or card: ")
        if payment_method not in ["cash", "card"]:
            print("Must paid by 'cash' or 'card'")
            continue
        break
    with open(file_path_money, 'a') as income_file:
        income_file.write(
            f"{trainee_id} | {program_name} | {money_income} | {s_date} | {time} | {payment_method}\n")
    print("---Store Successful---")
    input("Press enter to quit:")


def view_money_income():
    try:
        with open(file_path_money, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("---No File Found---")
        input("Press enter to quit---")
        return
    for i in sports_options:
        print(f"-{i}")
    user_input = input("Enter Sport or 'all': ").strip().lower()
    total = 0.0
    print("=" * width)
    print(f"{'Program':<20} {'Money Income':<20} {'Payment Method':<20}")
    print("=" * width)

    found = False
    for line in lines:
        data = line.strip().split(" | ")
        if len(data) >= 5:
            current_sport = data[1].lower()
            amount = float(data[2])

            if user_input == "all" or user_input == current_sport:
                total += amount
                print(f"{data[1]:<20} {data[2]:<20} {data[5]:<20}")
                found = True
    if found:
        print("=" * width)
        print(f"{'Total Income:':<20}"+f"RM{total:.2f}")
    else:
        print("No record found")
    input("Press enter to return:")

# Receptionist


def receptionist(id_value):

    # ["Register Trainee", "Delete Trainee", "Update Trainning", "Payment", "Generate Receipt", "Request", "Update Profile", "Log Out", "Quit"]

    while True:
        clear_screen()
        print("\n---Welcome to Receptionist Menu---")

        for i, receptionist_option in enumerate(receptionist_options, start=1):
            print(f"[{i}]. {receptionist_option}")

        user_input = input("Enter your choice (1-9): ")

        if user_input == "1":
            register_acc(file_path_trainee, "Trainee")

        elif user_input == "2":
            delete_acc(file_path_trainee, "Trainee")

        elif user_input == "3":
            update_program()

        elif user_input == "4":
            payment()

        elif user_input == "5":
            generate_receipt()

        elif user_input == "6":
            view_request()

        elif user_input == "7":
            update_profile(file_path_receptionist, id_value)

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


def update_program():
    clear_screen()
    try:
        with open(file_path_trainee, 'r') as f:
            trainee_lines = f.readlines()
        with open(file_path_trainee_schedule, 'r') as c:
            schd_lines = c.readlines()
    except FileNotFoundError:
        print("---No File Found---")
        input("Press Enter to return...")
        return

    print("=" * width)
    print(f"{'Trainee ID':<20} {'Name':<20}{'Current Program':<20}")
    print("=" * width)

    for t_line in trainee_lines:
        t_data = [item.strip() for item in t_line.split("|")]
        if len(t_data) >= 10:
            t_id = t_data[3]
            is_paid = False
            for s_line in schd_lines:
                s_data = [item.strip() for item in s_line.split("|")]

                if len(s_data) >= 9 and s_data[3] == t_id and s_data[8] == "Paid":
                    is_paid = True
                    break

        if not is_paid:  # Trainees who have paid cannot change training programs again
            print(f"{t_data[3]:<20} {t_data[0]:<20}{t_data[9]:<20}")
    target_id = input("Please enter trainee TP to update or 'q' to quit: ")
    if target_id == 'q':
        return
    new_sport = input_sport("Please enter new sport: ")
    update_function(target_id, new_sport)


def update_function(input_id, new_sport):
    try:
        with open(file_path_trainee_schedule, 'r') as c:
            schd_lines = c.readlines()
        with open(file_path_coaches, 'r') as s:
            coach_lines = s.readlines()
        with open(file_path_trainee, 'r') as f:
            trainee_lines = f.readlines()
    except FileNotFoundError:
        print("---No File Found---")
        input("Press Enter to return...")
        return
    target_id = input_id

    found_trainee = False
    payment_status = "Unpaid"
    has_schedule = False
    for s_line in schd_lines:  # Check for Existing Schedule & Payment
        s_parts = s_line.strip().split(" | ")
        if s_parts[3] == target_id:
            payment_status = s_parts[8]
            has_schedule = True
            break

    for i, line in enumerate(trainee_lines):  # Verify Trainee Existence
        if line.split(" | ")[3] == target_id:
            found_trainee = True
            break

    if not found_trainee:
        print("\nError: Trainee ID does not exist")
        input("Press enter to quit")
        return

    if payment_status == "Paid":  # check for payment status
        print("\nError. Trainee already paid cannot change")
        input("Press enter to quit")
        return

    for i, line in enumerate(trainee_lines):  # Join new data
        t_data = line.strip().split(" | ")
        if t_data[3] == target_id:
            t_data[9] = new_sport
            trainee_lines[i] = " | ".join(t_data) + "\n"
            break

    coach_id = None
    coach_name = None
    for coach_line in coach_lines:  # help assign new coach
        c_data = coach_line.strip().split(" | ")
        if len(c_data) >= 9 and new_sport in c_data[9].lower():
            coach_id = c_data[3]
            coach_name = c_data[0]
            break

    if not coach_id:  # no coach
        print(f"\nNo coach found for {new_sport}.")
        if has_schedule:
            print("Cancelling your schedule until a coach is found.")
            schd_lines = [l for l in schd_lines if l.split(" | ")[
                3] != target_id]
            with open(file_path_trainee_schedule, 'w') as f:
                f.writelines(schd_lines)

        with open(file_path_trainee, 'w') as t:
            t.writelines(trainee_lines)
        print("Update Successful! Account updated.")
        input("Press Enter to return...")
        return

    schedule_updated = False
    for i, line in enumerate(schd_lines):
        s_data = line.strip().split(" | ")
        if s_data[3] == target_id:
            s_data[0] = coach_id
            s_data[1] = coach_name
            s_data[2] = new_sport
            schd_lines[i] = " | ".join(s_data) + "\n"
            schedule_updated = True
            break

    with open(file_path_trainee, 'w') as t:
        t.writelines(trainee_lines)

    if schedule_updated:
        with open(file_path_trainee_schedule, 'w') as s:
            s.writelines(schd_lines)
        print(
            # automatic assign new coach new schedule
            f"\nUpdate Successful! Account and Schedule updated to {new_sport}.")
    else:
        print(
            # update trainee data but no schedule
            f"\nUpdate Successful for Account! (No schedule existed for {target_id})")

    input("Press Enter to quit:")


def payment():
    date = datetime.datetime.now()
    time = date.strftime("%H:%M:%S")
    s_date = date.strftime("%d/%B/%Y")

    try:
        with open(file_path_trainee_schedule, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("---No File Found---")
        return

    print("--Trainee that haven't paid the fee---")
    print("=" * width)
    print(f"{'Program Name':<15} {'Trainee ID':<15} {'Fee':<13} {'Payment Status':<20}")
    print("=" * width)

    found = False
    for line in lines:
        data = line.strip().split(" | ")
        if len(data) >= 8 and data[8] == "Unpaid":
            print(
                f'{data[1]:<15} {data[3]:<15} {data[4]:<15} {data[8]:<15}')
            found = True

    if not found:
        print("---All trainees have paid---")

    while True:

        target_id = input(
            "Enter Trainee's ID to pay(e.g TP090955) or 'q' to quit: ")
        if target_id == "q":
            break

        if not target_id.startswith("TP"):
            target_id = "TP" + target_id

        success = False
        for i, line in enumerate(lines):
            trainee_data = line.strip().split(" | ")
            if len(trainee_data) >= 8 and target_id == trainee_data[3]:

                payment_status = input(
                    f"{trainee_data[3]} paid? (y/n): ").lower()
                if payment_status == "y":
                    payment_method = input(
                        f"{trainee_data[3]} paid by cash or card?: ").lower().strip()
                    fee = float(trainee_data[4].strip())
                    if payment_method == "cash":
                        print(f"Program fee is: RM {fee:.2f}")
                        receive = float(input("System receive: RM "))
                        return_change = receive - fee
                        print(f"Returning change: RM {return_change:.2f}")
                        trainee_data[8] = "Paid"
                        lines[i] = " | ".join(trainee_data) + "\n"
                        success = True
                        break

                    elif payment_method == "card":
                        print(f"Program fee is: RM {fee:.2f}")
                        card_pin = input_int(
                            "Enter PIN number to do transaction: ")
                        print("Transaction complete")
                        trainee_data[8] = "Paid"
                        lines[i] = " | ".join(trainee_data) + "\n"
                        success = True
                        break

        if success:
            with open(file_path_money, 'a') as m:
                m.write(
                    f"{trainee_data[3]} | {trainee_data[1]} | {trainee_data[4]} | {s_date} | {time} | {payment_method}\n")
            with open(file_path_trainee_schedule, 'w') as f:
                f.writelines(lines)
            print("--Successfully paid---")
            break
        else:
            print("---Trainee ID not found or already paid---")
    input("Press enter to quit:")


def generate_receipt():
    try:
        with open(file_path_trainee_schedule, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("\n---No File Found---")
        input("Press enter to quit:")
        return
    now = datetime.datetime.now()
    print("\n--Trainee that already paid the fee---")
    print("=" * width)
    print(f"{'Program Name':<20} {'Trainee TP':<20} {'Fee(RM)':<20} {'Payment Status':<20}")
    print("=" * width)

    new_lines = []
    found = False
    receipt_code = now.strftime("%f%M%H%S")
    for line in lines:
        data = [item.strip() for item in line.strip().split("|")]
        payment_status = data[8]
        if len(data) >= 8 and payment_status == "Paid":
            print(f"{data[1]:<20} {data[3]:<20} {data[4]:<20} {data[8]:<20}")
            found = True
    if not found:
        print("\n---No trainee have paid---")
        input("Press enter to quit:")
        return

    while True:
        target_id = input_id(
            "Enter Trainee's ID to pay(e.g TP090955) or 'q' to quit: ").strip()
        if target_id == "q":
            break

        if not target_id.startswith("TP"):
            target_id = "TP" + target_id

        generate = False
        for i, line in enumerate(lines):
            trainee_data = line.strip().split(" | ")
            payment_status = trainee_data[8]
            if len(trainee_data) >= 8 and target_id == trainee_data[3]:
                if payment_status == "Paid":
                    print_receipt = save_receipt(receipt_code, trainee_data[3], trainee_data[2],
                                                 trainee_data[5], trainee_data[6], trainee_data[7],
                                                 trainee_data[1], trainee_data[4])
                    generate = True
                    break

        if generate:
            with open(file_path_receipt, 'a') as f:
                f.write(print_receipt)
            print(print_receipt)
            print(
                f"Successfully generated receipt for {target_id} and saved into file.Please check!.")
            break
        else:
            print("---Generate Failed---")
            return
    input("Press enter to quit:")


def view_request():
    try:
        with open(file_path_request, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("---file not found---")
        input("Press enter to quit")
        return

    print("=" * width)
    print(f"{'Trainee ID':<20} {'New Program':<20} {'Old Program':<20}{'Status':<20} ")
    print("=" * width)

    found = False
    for line in lines:
        request_data = line.strip().split(" | ")
        if len(request_data) >= 4 and request_data[3] == "Pending":
            print(
                f"{request_data[0]:<20} {request_data[1]:<20} {request_data[2]:<20} {request_data[3]:<20}")
            found = True
    if not found:
        print("\nNo Request found")
        input("Press enter to quit")
        return
    target_id = input("Please enter trainee's TP to update or 'q' to quit: ")
    decision = input("Approve or Reject request? (a/r): ").lower()
    update_schedule_data = False
    for i, line in enumerate(lines):
        change_data = line.strip().split(" | ")
        if len(change_data) >= 4 and change_data[0] == target_id:
            if decision == "a":
                change_data[3] = "Approved"
                new_sport = change_data[1]
                # reuse the function
                update_function(target_id, new_sport)
            elif decision == "r":
                change_data[3] = "Rejected"
            else:
                print("Invalid choice")
                return

            lines[i] = " | ".join(change_data) + "\n"
            updated = True

    if updated:
        with open(file_path_request, 'w') as w:
            w.writelines(lines)
        print("\n--- Program updated successfully ---")
    else:
        print("---No pending or request found---")


# ========  Coach


def coach(id_value):
    # ["Add Training Programs", "Update Training Program", "Delete Training Program", "View the list of trainees", "Update Profile", "Login Out", "Quit"]
    while True:
        clear_screen()
        print("\n---Welcome to Coach Menu---")
        for i, coaches_option in enumerate(coaches_options, start=1):
            print(f"[{i}]. {coaches_option}")

        choice = input("Choice: ")

        if choice == "1":
            add_program(id_value)

        elif choice == "2":
            update_training(id_value)

        elif choice == "3":
            delete_program(id_value)

        elif choice == "4":
            view_program(id_value)

        elif choice == "5":
            update_profile(file_path_coaches, id_value)

        elif choice == "6":
            print("Logging Out....")
            clear_logout()
            return

        elif choice == "7":
            clear_screen()
            print(
                "Thank you for using Admin Sport-Training Centre Management System..Good Bye!")
            exit()
        else:
            clear_screen()
            print("Invalid Answer, please try again")


def add_program(id_value):
    try:
        with open(file_path_coaches, 'r') as c:
            coach_lines = c.readlines()
        with open(file_path_trainee, 'r') as f:
            lines = f.readlines()
        with open(file_path_trainee_schedule, 'r') as r:
            schedule_lines = r.readlines()
    except FileNotFoundError:
        print("---No File Found---")
        return

    coach_sport = None
    coach_id = id_value
    for coach_line in coach_lines:
        check_data = coach_line.strip().split(" | ")
        if len(check_data) >= 10 and coach_id == check_data[3]:
            coach_sport = check_data[9]
    if not coach_sport:
        print("Can't find your record")
        return

    print(f"{'---Your Current Schedule---':^90}")
    print("=" * width)
    print(f"{'Program Name':<25} {'Trainee TP':<17} {'Date':<10} {'Start Time':<10} {'End TIme':<5} {'Fee':<5}")
    print("=" * width)
    for print_line in schedule_lines:
        print_data = print_line.strip().split(" | ")
        if len(print_data) >= 9 and id_value == print_data[0]:
            print(
                f"{print_data[1]:<25} {print_data[3]:<15} {print_data[5]:<15} {print_data[6]:<10} {print_data[7]:<5} {print_data[4]:<5}")

    charge = input_int("\nCharge: RM", min_num=50, max_num=300)
    date = input_date("Enter your date DD/MM/YYYY (e.g 04/05/2025): ")
    while True:
        from_time = input_time(
            "Enter your start time 2400 format (e.g 2130): ")
        to_time = input_time(
            "Enter your end time 2400 format (e.g 2130): ")
        if time_conflict(from_time, to_time):
            print("Error: End time must be after start time")
            continue

        conflict_found = False
        for schedule_line in schedule_lines:
            schedule_data = schedule_line.strip().split(" | ")
            file_coach_id = schedule_data[1]
            if file_coach_id == id_value:
                if len(schedule_data) > 6 and schedule_data[5] == date:
                    start_time = schedule_data[6]
                    end_time = schedule_data[7]
                    if from_time < end_time and to_time > start_time:
                        conflict_found = True
                        break

        if conflict_found:
            print(f"You already have a class during that time.")
            continue
        else:
            break

    found = False
    trainee_name = ""
    trainee_id = ""
    for line in lines:
        data = line.strip().split(" | ")
        if len(data) > 6:
            trainee_name = data[0]
            trainee_id = data[3]

            assign = False
            for assign_trainee in schedule_lines:
                assign_data = assign_trainee.strip().split(" | ")
                if len(assign_data) >= 10 and assign_data[3] == trainee_id:
                    assign = True
                    break
            if assign:
                continue
            trainee_sport = data[9].lower().strip()
            coach_sports_list = [s.strip().lower()
                                 for s in coach_sport.split(",")]
            trainee_sports_list = [s.strip().lower()
                                   for s in trainee_sport.split(",")]
            same_sport = [
                s for s in trainee_sports_list if s in coach_sports_list]
            if same_sport:
                match_sport = same_sport[0]
                found = True
                break

    if found:
        record = coach_id + " | " + match_sport + " | " + trainee_name + " | " + trainee_id + \
            " | " + charge + " | " + date + " | " + from_time + \
            " | " + to_time + " | " + "Unpaid" + "\n"
        with open(file_path_trainee_schedule, "a") as file:
            file.write(record)
        print(f"---Program added successfully---")
    else:
        print("---Add Failed.No trainee register this program yet---")
    input("Press enter to quit:")


def update_training(id_value):
    try:
        with open(file_path_trainee_schedule, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("--- No File Found ---")
        return

    # --- Step 1: Display Unpaid Programs ---
    print(f"\n{'--- Unpaid Programs Managed by You ---':^90}")
    print("=" * width)
    print(f"{'Program Name':<25} {'Trainee TP':<15} {'Date':<12} {'Start':<10} {'End':<5} {'Fee':<5}")
    print("=" * width)

    found_any = False
    for line in lines:
        data = line.strip().split(" | ")
        # Ensure index 8 exists (Payment Status) and coach matches
        if len(data) >= 9 and data[0] == id_value:
            if data[8].strip() == "Unpaid":
                print(
                    f"{data[1]:<25} {data[3]:<15} {data[5]:<12} {data[6]:<10} {data[7]:<5} {data[4]:<5}")
                found_any = True

    if not found_any:
        print("--- No unpaid programs found ---")
        return

    target_id = input_id(
        "\nEnter trainee TP to change training details (e.g., TP090955): ")

    updated = False
    for i in range(len(lines)):
        data = lines[i].strip().split(" | ")

        if len(data) >= 9 and data[0] == id_value and data[3] == target_id:

            if data[8].strip() != "Unpaid":
                print("Error: You cannot update a trainee that has already paid.")
                return

            print(f"\n--- Updating Program: {data[1]} ---")

            new_charge = input_int(
                "New charge: RM ", min_num=50, max_num=300)
            new_date = input_date("New date (DD/MM/YYYY): ")
            new_start = input_time("Start time (HHMM): ")
            new_end = input_time("End time (HHMM): ")

            if time_conflict(new_start, new_end):
                print("Update failed: End time must be after start time.")
                return

            data[4] = str(new_charge)
            data[5] = new_date
            data[6] = new_start
            data[7] = new_end

            lines[i] = " | ".join(data) + "\n"
            updated = True
            break

    if updated:
        with open(file_path_trainee_schedule, "w") as f:
            f.writelines(lines)
        print("\n--- Program updated successfully ---")
    else:
        print("\n--- Trainee ID not found in your unpaid list ---")

    input("Press enter to return to menu...")


def delete_program(id_value):
    try:
        with open(file_path_trainee_schedule, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("---No File Found---")
        input("Press enter to quit")
        return
    print(f"{'---Program that you add---':^70}")
    print("=" * width)
    print(f"{'Program Name':<15}{'Trainee TP':<17} {'Date':<12} {'Start Time':<15} {'End Time':<15} {'Fee':<15}")
    print("=" * width)

    found = False
    for line in lines:
        data = line.strip().split(" | ")
        if len(data) >= 9 and data[0] == id_value:
            print(
                f"{data[1]:<14} {data[3]:<15} {data[5]:<15} {data[6]:<15} {data[7]:<15} {data[4]:<15}")
            found = True
    if not found:
        print("\n---No program found or program already paid---")
        input("\nPress enter to quit")
        return

    target = input_id(
        "\nEnter Trainee ID to delete or enter to back: ")
    new_lines = []
    deleted = False
    if target == "q":
        return

    for line in lines:
        data = line.strip().split(" | ")

        value_id = data[0]
        trainee_id = data[3].strip()

        if value_id == id_value and trainee_id == target:
            deleted = True
        else:
            new_lines.append(line)

    if deleted:
        with open(file_path_trainee_schedule, "w") as f:
            f.writelines(new_lines)
        print("\n---Program deleted successfully---")
    else:
        print("\n---Program not found---")
    input("Press enter to quit: ")


def view_program(id_value):
    try:
        with open(file_path_trainee_schedule, "r") as f:
            print(f"\n{'--- PROGRAM LIST ---':^90}")
            print("=" * width)
            print(
                f"{'Program Name':<16} {'Trainee TP':<15} {'Trainee Name':<15} {'Fee(RM)':<10} {'Date':<8} {'Start Time':<8} {'End Time':<10}")
            print("=" * width)
            found = False
            for line in f:
                data = line.strip().split(" | ")
                if len(data) >= 9 and data[0] == id_value:
                    print(
                        f"{data[1]:<16} {data[3]:<15} {data[2]:<15} {data[4]:<7} {data[5]:<14} {data[6]:<10} {data[7]:<10}")
                    found = True
            if not found:
                print("\n---No programs found---")
    except FileNotFoundError:
        print("\n---No File Found---")
        return
    input("\nPress enter to quit: ")

# ========  Trainee


def trainee(id_value):
    while True:
        # ["View schedule", "View payment","Request", "Update Profile", "Login Out", "Quit"]
        clear_screen()
        print("\n---Welcome to Trainee Menu---")
        print("\nOpen time: 9am morning")
        print("Closed time: 10pm night\n")

        for i, trainee_option in enumerate(trainee_options, start=1):
            print(f"[{i}]. {trainee_option}")

        user_input = input("Enter your choice (1-6): ")

        if user_input == "1":
            view_schedule(id_value)

        elif user_input == "2":
            view_payment(id_value)

        elif user_input == "3":
            request(id_value)

        elif user_input == "4":  # Update Profile
            update_profile(file_path_trainee, id_value)

        elif user_input == "5":  # Login Out
            print("Logging Out....")
            clear_logout()
            return

        elif user_input == "6":
            print(
                "Thank you for using Admin Sport-Training Centre Management System..Good Bye!")
            exit()
        else:
            print("Invalid number..Please try again....")


def view_schedule(id_value):
    try:
        with open(file_path_trainee_schedule, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("\n---No Scehedule Found---")
        return

    print("=" * width)
    print(f"{'Program Name':<15} {'Trainee TP':<15}{'Coach TP':<13}{'Date':<13} {'Start Time':<13} {'End Time':<15}")
    print("=" * width)
    view = False
    for line in lines:
        data = line.strip().split(" | ")
        if len(data) >= 9 and data[3] == id_value:
            print(
                f"{data[1]:<15} {data[3]:<15} {data[0]:<12}{data[5]:<15} {data[6]:<12} {data[7]:<15}")
            view = True

    if not view:
        print("\n---No record found---")
    input("Press enter to quit:")


def view_payment(id_value):
    try:
        with open(file_path_trainee_schedule, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("---No Scedule Found---")
        return
    total = 0.0
    print("=" * width)
    print(f"{'Program Name':<15} {'Trainee TP':<15} {'Fee(RM)':<15} {'Payment Status':<15}")
    print("=" * width)
    view = False
    for line in lines:
        data = line.strip().split(" | ")
        amount = float(data[4])
        payment_status = data[8].strip()
        if len(data) >= 9 and data[3] == id_value:
            if payment_status == "Unpaid":
                total += amount
                print(
                    f"{data[1]:<15} {data[3]:<15} {data[4]:<15} {payment_status:<15}")
                view = True
    if view:
        print("=" * width)
        print(f"{'Total Income:':<30}"+f"RM{total:.2f}")
    else:
        print("---No record found---")
    input("Press enter to quit:")


def request(id_value):
    # ["Send Request","Delete Request", "Update Request", "Back"]

    account_exists = False
    try:
        with open(file_path_trainee, 'r') as t:
            for line in t:
                data = line.strip().split(" | ")
                if len(data) >= 10 and data[3] == id_value:
                    account_exists = True
                    old_program = data[9]
                    break
    except FileNotFoundError:
        print("---Trainee database not found---")
        input("---Press enter to quit---")
        return

    if not account_exists:
        print("Error: No account found for this ID.")
        input("---Press enter to quit---")
        return

    while True:
        clear_screen()
        try:
            with open(file_path_request, 'r') as f:
                request_lines = f.readlines()
            with open(file_path_trainee_schedule, 'r') as f:
                schedule_lines = f.readlines()
        except FileNotFoundError:
            request_lines = []
            print("---No Schedule found---")
            return

        print("\n--- Request Management ---")
        for i, send_request in enumerate(send_requests, start=1):
            print(f"[{i}]. {send_request}")

        print("="*60)
        print(
            f"{'Trainee ID':15} {'New Program':<15} {'Old Program':<15}{'Status':<15}")
        print("="*60)

        view_found = False
        for line in request_lines:
            view_data = line.strip().split(" | ")
            if len(view_data) >= 4 and view_data[0] == id_value:
                print(
                    f"{id_value:<15} {view_data[1]:<15} {old_program:<15} {view_data[3]:<15}")
                view_found = True
        for request_line in request_lines:
            delete_data = request_line.strip().split(" | ")

        if not view_found:
            print("---You have no pending requests---")
        print("="*60 + "\n")

        user_input = input("Enter your choice: ")
        if user_input == "4":
            return

        if user_input == "1":
            new_program = input_sport("Enter new sport: ")
            with open(file_path_request, 'a') as f:
                f.write(
                    f"{id_value} | {new_program} | {old_program} | Pending\n")
            print("---Request sent successfully---")
            input("Press enter to quit: ")

        elif user_input == "2":
            delete_program = input_sport(
                "Enter the request program that you send: ")
            new_lines = []
            deleted = False
            forbidden = False
            for request_line in request_lines:
                delete_data = request_line.strip().split(" | ")
                if len(delete_data) >= 4:
                    program_data = delete_data[1].strip()
                    trainee_id = delete_data[0].strip()
                    pending_status = delete_data[3].strip()
                    if program_data.lower() == delete_program and trainee_id == id_value:
                        if pending_status == "Pending":  # check is the requests is "Pending"
                            deleted = True
                            continue
                        else:
                            forbidden = True
                new_lines.append(request_line)
            with open(file_path_request, 'w') as f:
                f.writelines(new_lines)
            if deleted:
                print("---Deleted Successful------")
            elif forbidden:
                print("---Cannot delete approved or rejected requests---")
            else:
                print("---Request not found---")

            input("Press enter to quit: ")

        elif user_input == "3":  # Update program
            request_program = input_sport(
                "Enter request program that you assign: ")
            update = False
            forbidden = False  # to check the forbidden data
            for i, request_line in enumerate(request_lines):
                update_data = request_line.strip().split(" | ")
                if len(update_data) >= 4:
                    check_program = update_data[1].lower()
                    pending_status = update_data[3].strip()
                    if request_program == check_program and pending_status == "Pending":  # check is the requests is "Pending"
                        update_data[1] = input_sport("Enter new program: ")
                        request_lines[i] = " | ".join(update_data) + "\n"
                        update = True  # change data
                        break
                    else:
                        # forbidden the status if is approved or rejected
                        forbidden = True
            if update:
                with open(file_path_request, 'w') as f:
                    f.writelines(request_lines)
                print("---Update Successful---")
            elif forbidden:
                print("---Cannot delete approved or rejected requests---")
            else:
                print("Request not found or request already update cannot change---")
            input("Press enter to quit:")


 # start system
if __name__ == "__main__":
    main_menu()
