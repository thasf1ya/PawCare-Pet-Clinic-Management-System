from tkinter import *

from pet import open_pet_window
from veterinarian import open_vet_window
from appointment import open_appointment_window

root = Tk()

root.title("PawCare - Pet Clinic Management System")
root.geometry("650x500")
root.configure(bg="#EAF6F6")

Label(
    root,
    text="🐾 PawCare",
    font=("Arial", 24, "bold"),
    bg="#EAF6F6",
    fg="#00695C"
).pack(pady=(30,5))

Label(
    root,
    text="Pet Clinic Management System",
    font=("Arial", 14),
    bg="#EAF6F6"
).pack(pady=(0,25))

Button(
    root,
    text="🐶 Pet Management",
    font=("Arial",12),
    width=25,
    height=2,
    bg="#80CBC4",
    command=open_pet_window
).pack(pady=10)

Button(
    root,
    text="👨‍⚕️ Veterinarian Management",
    font=("Arial",12),
    width=25,
    height=2,
    bg="#80CBC4",
    command=open_vet_window
).pack(pady=10)

Button(
    root,
    text="📅 Appointment Management",
    font=("Arial",12),
    width=25,
    height=2,
    bg="#80CBC4",
    command=open_appointment_window
).pack(pady=10)


root.mainloop()