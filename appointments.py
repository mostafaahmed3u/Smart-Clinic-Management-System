from datetime import datetime , timedelta
class Appointment:
  def __init__(self,patient_id,date_time,amount,status):
    self.patient_id=patient_id
    self.date_time=date_time
    self.amount=amount
    self.status=status


def generate_slots (date):
  slots=[]
  starting= datetime( date.year , date.month , date.day , 18 , 0)
  finishing= datetime( date.year , date.month , date.day , 22 , 0)
  slot_duration= timedelta(minutes=20)

  if date.weekday()== 4:
    return slots

  while starting<finishing:
    end= starting + slot_duration
    slots.append((starting,end))
    starting= end

  return slots

appointments=[]
def book_appointment():
    patient_id=int(input("Please enter your id:"))
    date=datetime.strptime(input("Please enter appointment date:"),"%Y-%m-%d")
    time=datetime.strptime(input("Please enter appointment time:"),"%H:%M")
    appointment_date_time=datetime(date.year,date.month,date.day,time.hour,time.minute)
    available_slots=generate_slots(date)

    booked = False
    for starting , end in available_slots:
      if appointment_date_time == starting:
        for appointment in appointments:
          if appointment.date_time == appointment_date_time:
            booked = True
        if booked == True:
          print("this slot is already booked!")
        else:
          appointment = Appointment(patient_id,appointment_date_time,650,"booked")
          appointments.append(appointment)
          print("Appointment is booked successfully!")
          save_appointment()
        break
    else:
      print("this slot is not found!")


def view_appointments():
  for appointment in appointments:
    print(appointment.patient_id)
    print(appointment.date_time)
    print(appointment.amount)
    print(appointment.status)


def cancel_appointment():
  patient_id=int(input("Please enter your id:"))
  date=datetime.strptime(input("Please enter appointment date:"),"%Y-%m-%d")
  time=datetime.strptime(input("Please enter appointment time:"),"%H:%M")
  appointment_date_time=datetime(date.year,date.month,date.day,time.hour,time.minute)

  for appointment in appointments :
    if patient_id==appointment.patient_id and appointment_date_time==appointment.date_time:
      appointment.status="cancelled"
      print("it is cancelled now!")
      save_appointment()
      break
  else:
    print("appointment is not found!")


def save_appointment():
  file=open("appointments.txt","w")
  for appointment in appointments:
    file.write(str(appointment.patient_id)+ "|" +
               str(appointment.date_time)+ "|"+
               str(appointment.amount)+ "|" +
               appointment.status+ "\n")
  file.close()

def load_appointment():
  try:
    file=open("appointments.txt","r")

    for line in file:
      data = line.strip().split("|")
      patient_id = int(data[0])
      date_time = datetime.strptime(data[1], "%Y-%m-%d %H:%M:%S")
      amount = int(data[2])
      status = data[3]

      appointment = Appointment(patient_id, date_time, amount, status)
      appointments.append(appointment)

    file.close()

  except FileNotFoundError:
    file=open("appointments.txt","w")
    file.close()


load_appointment()

def appointment_menu():
  
  choice=0
  while choice!=4:

    print("              <<<Clinic Appointment System>>>")
    print("1.Book Appointment")
    print("2.View Appointments")
    print("3.Cancel Appointment")
    print("4.Exit")

    choice=int(input("Enter what you want number:"))
    if choice==1:
        book_appointment()
    elif choice==2:
        view_appointments()
    elif choice==3:
        cancel_appointment()
    elif choice==4:
        print("YOU ARE EXITING NOW , WE GONNA MISS YOU :)")
    else:
        print("invalid choice")