class MedicalRecord:
    def __init__(self, patient_id, date, diagnosis, treatment, notes):
        self.patient_id = patient_id
        self.date = date
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.notes = notes


records = []


def add_medical_record(patients):
    patient_id = input("Please enter patient id: ")

    if not patient_id.isdigit():
        print("Invalid patient ID. Please enter numbers only.")
        return

    patient = None

    for p in patients:
        if str(p.patient_id) == patient_id:
            patient = p
            break

    if patient is None:
        print("Patient not found.")
        return

    date = input("Please enter record date: ")

    for record in records:
        if str(record.patient_id) == patient_id and record.date == date:
            print("This record already exists!")
            return

    diagnosis = input("Please enter diagnosis: ")
    treatment = input("Please enter treatment: ")
    notes = input("Please enter notes: ")

    record = MedicalRecord(
        patient_id,
        date,
        diagnosis,
        treatment,
        notes
    )

    records.append(record)

    if not hasattr(patient, "records"):
        patient.records = []

    patient.records.append(record)

    save_records()

    print("Medical record added successfully!")


def view_patient_records(patients):
    patient_id = input("Please enter patient id: ")

    if not patient_id.isdigit():
        print("Invalid patient ID. Please enter numbers only.")
        return

    patient = None

    for p in patients:
        if str(p.patient_id) == patient_id:
            patient = p
            break

    if patient is None:
        print("Patient not found.")
        return

    found = False

    for record in records:
        if str(record.patient_id) == patient_id:
            print("\n--------------------")
            print("Date:", record.date)
            print("Diagnosis:", record.diagnosis)
            print("Treatment:", record.treatment)
            print("Notes:", record.notes)
            found = True

    if found == False:
        print("No medical records found!")


def update_patient_record(patients):
    patient_id = input("Please enter patient id: ")

    if not patient_id.isdigit():
        print("Invalid patient ID. Please enter numbers only.")
        return

    patient = None

    for p in patients:
        if str(p.patient_id) == patient_id:
            patient = p
            break

    if patient is None:
        print("Patient not found.")
        return

    date = input("Please enter record date: ")

    for record in records:
        if str(record.patient_id) == patient_id and record.date == date:

            record.diagnosis = input("Enter new diagnosis: ")
            record.treatment = input("Enter new treatment: ")
            record.notes = input("Enter new notes: ")

            save_records()

            print("Medical record updated successfully!")
            return

    print("Medical record is not found!")


def save_records():
    file = open("medical_records.txt", "w")

    for record in records:
        file.write(
            str(record.patient_id) + "|" +
            record.date + "|" +
            record.diagnosis + "|" +
            record.treatment + "|" +
            record.notes + "\n"
        )

    file.close()


def load_records():
    try:
        file = open("medical_records.txt", "r")

        for line in file:
            data = line.strip().split("|")

            if len(data) != 5:
                continue

            patient_id = data[0]
            date = data[1]
            diagnosis = data[2]
            treatment = data[3]
            notes = data[4]

            record = MedicalRecord(
                patient_id,
                date,
                diagnosis,
                treatment,
                notes
            )

            records.append(record)

        file.close()

    except FileNotFoundError:
        file = open("medical_records.txt", "w")
        file.close()


def medical_record_menu(patients):
    while True:
        print("\n========================")
        print("   MEDICAL RECORD MENU")
        print("========================")
        print("1. Add Medical Record")
        print("2. View Patient Records")
        print("3. Update Patient Record")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_medical_record(patients)

        elif choice == "2":
            view_patient_records(patients)

        elif choice == "3":
            update_patient_record(patients)

        elif choice == "4":
            print("Exiting Medical Record Menu...")
            break

        else:
            print("Invalid choice.")