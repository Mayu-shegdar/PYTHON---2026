class Patient:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        status_names = ["Normal", "Urgent", "Super Urgent"]
        return f"{self.name} ({status_names[self.status]})"


class Specialization:
    MAX_QUEUE = 5

    def __init__(self, name):
        self.name = name
        self.patients = []

    def add_patient(self, patient):
        if len(self.patients) >= self.MAX_QUEUE:
            print("Queue is full")
            return

        if patient.status == 2:
            self.patients.insert(0, patient)
        elif patient.status == 1:
            self.patients.insert(1 if len(self.patients) > 0 else 0, patient)
        else:
            self.patients.append(patient)

    def get_next_patient(self):
        if not self.patients:
            print("No patients in queue")
            return
        patient = self.patients.pop(0)
        print("Next patient:", patient)

    def remove_patient(self, name):
        for p in self.patients:
            if p.name == name:
                self.patients.remove(p)
                print("Patient removed")
                return
        print("Patient not found")

    def list_patients(self):
        if not self.patients:
            print("No patients")
        else:
            for p in self.patients:
                print(p)


class OperationsManager:
    def __init__(self):
        self.specializations = {
            1: Specialization("Cardiology"),
            2: Specialization("Neurology"),
            3: Specialization("Orthopedics")
        }

    def run(self):
        while True:
            print("\nHospital Patient Queue System")
            print("1. Add patient")
            print("2. Print patients")
            print("3. Get next patient")
            print("4. Remove patient")
            print("5. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                name = input("Enter patient name: ")
                spec = int(input("Enter specialization (1-3): "))
                status = int(input("Enter status (0 normal,1 urgent,2 super urgent): "))
                patient = Patient(name, status)
                self.specializations[spec].add_patient(patient)

            elif choice == "2":
                for spec in self.specializations.values():
                    print(f"\n{spec.name} patients:")
                    spec.list_patients()

            elif choice == "3":
                spec = int(input("Enter specialization (1-3): "))
                self.specializations[spec].get_next_patient()

            elif choice == "4":
                spec = int(input("Enter specialization (1-3): "))
                name = input("Enter patient name: ")
                self.specializations[spec].remove_patient(name)

            elif choice == "5":
                print("Program ended")
                break

            else:
                print("Invalid choice")


app = OperationsManager()
app.run()