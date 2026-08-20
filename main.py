from patient import register_patient, login_patient, load_patients, patients
from MedicalRecord import medical_record_menu
from appointments import appointment_menu
from doctor import Doctor

def menu():
    while True:
        print("\n========== Clinic Management System ==========")
        print("1. Patient Menu")
        print("2. Doctor Menu")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            patient_menu()
        elif choice == "2":
            doctor = Doctor("doctor1", "1234")
            if doctor.login():
                load_patients() # تحميل بيانات المرضى المسجلين من الملف
                doctor.doctor_menu(patients) # استدعاء المنيو عن طريق كائن الطبيب

        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


def patient_menu():
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
                    print("3. Appointments")
                    print("4. Logout")

                    account_choice = input("Enter your choice: ")

                    if account_choice == "1":
                        patient.show_patient_info()

                    elif account_choice == "2":
                        medical_record_menu([patient])

                    elif account_choice == "3":
                        appointment_menu()
                        
                    elif account_choice == "4":
                        print("Logged out successfully.")
                        break

                    else:
                        print("Invalid choice! Please try again.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

# لتشغيل البرنامج مباشرة عند تنفيذ الملف
if __name__ == "__main__":
    menu()