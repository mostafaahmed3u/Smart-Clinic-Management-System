import os

class Patient:
    def __init__(self, patient_id, name, age, phone):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.phone = phone


    def show_patient_info(self):

        print("\n===== Patient Information =====")
        print("ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Phone:", self.phone)

patients = []


def load_patients():
    patients.clear()
    if os.path.exists("patients.txt"):
        with open("patients.txt", "r") as file:
            for line in file:
                if line.strip():
                    p_id, name, age, phone = line.strip().split("|")
                    patients.append(Patient(int(p_id), name, int(age), phone))

def save_patients():
    with open("patients.txt", "w") as file:
        for p in patients:
            file.write(str(p.patient_id) + "|" + p.name + "|" + str(p.age) + "|" + p.phone + "\n")
def register_patient():
    name = input("Enter your name: ")
    while True:
        age_input = input("Enter your age: ")
        if age_input.isdigit():
            age = int(age_input)
            break
        print("Invalid input! Please enter a number for your age.")
            
    phone = input("Enter your phone number: ")

    load_patients()
    if len(patients) == 0:
        new_id = 1
    else:
        new_id = max(p.patient_id for p in patients) + 1
    new_patient = Patient(new_id, name, age, phone)
    patients.append(new_patient)
    save_patients()

    print("\nPatient registered successfully! Your Patient ID is:" + str(new_id))
    return new_patient

def login_patient():
    load_patients()
    while True:
        id_input = input("Enter your Patient ID: ")
        if not id_input.isdigit():
            print("Invalid input! Please enter a numeric ID.")
            continue

        patient_id = int(id_input)
        for p in patients:
            if p.patient_id == patient_id:
                print("\nLogin successful! Welcome," + p.name)
                return p
            

        print("\nInvalid Patient ID")
        choice = input("Do you want to try again? (Y/N): ").lower()
        if choice != "y":
            return None
























# def patient_menu():
    while True:
        print("\n========== Patient Menu ==========")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_patient()

        elif choice == "2":
            patient = login_patient()

            if patient is not None:
                while True:
                    print("\n========== Patient Account ==========")
                    print("1. Show My Information")
                    print("2. My Medical Records")
                    print("3. My Appointments")
                    print("4. Book Appointment")
                    print("5. Cancel My Appointment")
                    print("6. Logout")

                    account_choice = input("Enter your choice: ")

                    if account_choice == "1":
                        patient.show_patient_info()

                    elif account_choice == "2":
                        view_medical_records([patient])

                    elif account_choice == "3":
                        print("Logged out successfully.")
                        break

                    else:
                        print("Invalid choice! Please try again.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


