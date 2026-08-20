# DOCTOR login - SMART CLINIC
from appointments import appointments, load_appointment

class Doctor:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # Doctor Login
    def login(self):
        username = input("Enter doctor username: ")
        password = input("Enter doctor password: ")

        if username == self.username and password == self.password:
            print("\nLogin successful!")
            return True
        else:
            print("\nInvalid username or password.")
            return False

    # Search Patient by ID
    def search_by_id(self, patients):
        patient_id = input("Enter Patient ID: ")

        for patient in patients:
            if str(patient.patient_id) == str(patient_id):
                print("\nPatient Found")
                print("Name:", patient.name)
                print("ID:", patient.patient_id)
                return patient

        print("Patient not found.")
        return None

    # Search Patient by Name
    def search_by_name(self, patients):
        name = input("Enter Patient Name: ")

        for patient in patients:
            if patient.name.lower() == name.lower():
                print("\nPatient Found")
                print("Name:", patient.name)
                print("ID:", patient.patient_id)
                return patient

        print("Patient not found.")
        return None

    # Show All Patients
    def show_all_patients(self, patients):
        if len(patients) == 0:
            print("No patients registered.")
            return

        print("\n===== All Patients =====")

        for patient in patients:
            print("Name:", patient.name)
            print("ID:", patient.patient_id)
            print("-----------------------")

    def view_patient_records(self, patients):
        load_records()
        patient = self.search_by_id(patients)

        if patient is not None:
            print("\n===== Patient Records =====")
            found = False

            for record in records:
                if str(record.patient_id) == str(patient.patient_id):
                    print("\n--------------------")
                    print("Date:", record.date)
                    print("Diagnosis:", record.diagnosis)
                    print("Treatment:", record.treatment)
                    print("Notes:", record.notes)
                    found = True

            if not found:
                print("No records found.")
    # View All Appointments (تم تعديل الدالة لتستورد المواعيد من ملف المواعيد مباشرة)
    def view_all_appointments(self, patients):
        load_appointment()
        print("\n===== All Appointments =====")

        if not appointments:
            print("No appointments found.")
            return

        for appointment in appointments:
            patient_name = "Unknown"
            for patient in patients:
                if str(patient.patient_id) == str(appointment.patient_id):
                    patient_name = patient.name
                    break

            print("Patient Name:", patient_name)
            print("Patient ID:", appointment.patient_id)
            print("Date & Time:", appointment.date_time)
            print("Amount:", appointment.amount)
            print("Status:", appointment.status)
            print("----------------------------")

    # Doctor Menu
    def doctor_menu(self, patients):
        while True:
            print("\n========================")
            print("       DOCTOR MENU")
            print("========================")
            print("1. Search Patient")
            print("2. Show All Patients")
            print("3. Add Patient Records")
            print("4. View All Appointments")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("\n1. Search by ID")
                print("2. Search by Name")

                search_choice = input("Enter your choice: ")

                if search_choice == "1":
                    self.search_by_id(patients)
                elif search_choice == "2":
                    self.search_by_name(patients)
                else:
                    print("Invalid choice.")

            elif choice == "2":
                self.show_all_patients(patients)

            elif choice == "3":
                self.view_patient_records(patients)

            elif choice == "4":
                self.view_all_appointments(patients)

            elif choice == "5":
                print("Logging out...")
                break

            else:
                print("Invalid choice.")


if __name__ == "__main__":
    doctor = Doctor("doctor1", "1234")
    if doctor.login():
        patients = []
        doctor.doctor_menu(patients)