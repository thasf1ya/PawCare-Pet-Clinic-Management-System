from tkinter import *
from tkinter import ttk, messagebox
from database import connection, cursor


def clear_fields():
    pet_name.delete(0, END)
    species.delete(0, END)
    breed.delete(0, END)
    age.delete(0, END)
    owner_name.delete(0, END)
    phone.delete(0, END)
    search_id.delete(0, END)


def view_pets():
    cursor.execute("SELECT * FROM pet")
    rows = cursor.fetchall()

    for item in table.get_children():
        table.delete(item)

    for row in rows:
        table.insert("", END, values=row)


def add_pet():

    if pet_name.get() == "":
        messagebox.showerror("Error", "Pet Name is required")
        return

    sql = """
    INSERT INTO pet
    (pet_name,species,breed,age,owner_name,phone)
    VALUES(%s,%s,%s,%s,%s,%s)
    """

    values = (
        pet_name.get(),
        species.get(),
        breed.get(),
        age.get(),
        owner_name.get(),
        phone.get()
    )

    cursor.execute(sql, values)
    connection.commit()

    messagebox.showinfo("Success", "Pet Added Successfully!")

    clear_fields()
    view_pets()


def search_pet():

    if search_id.get() == "":
        messagebox.showerror("Error", "Enter Pet ID")
        return

    cursor.execute(
        "SELECT * FROM pet WHERE pet_id=%s",
        (search_id.get(),)
    )

    row = cursor.fetchone()

    for item in table.get_children():
        table.delete(item)

    if row:

        table.insert("", END, values=row)

        pet_name.delete(0, END)
        species.delete(0, END)
        breed.delete(0, END)
        age.delete(0, END)
        owner_name.delete(0, END)
        phone.delete(0, END)

        pet_name.insert(0, row[1])
        species.insert(0, row[2])
        breed.insert(0, row[3])
        age.insert(0, row[4])
        owner_name.insert(0, row[5])
        phone.insert(0, row[6])

    else:
        messagebox.showinfo("Not Found", "Pet not found")


def update_pet():

    if search_id.get() == "":
        messagebox.showerror("Error", "Search a pet first")
        return

    sql = """
    UPDATE pet
    SET
    pet_name=%s,
    species=%s,
    breed=%s,
    age=%s,
    owner_name=%s,
    phone=%s
    WHERE pet_id=%s
    """

    values = (
        pet_name.get(),
        species.get(),
        breed.get(),
        age.get(),
        owner_name.get(),
        phone.get(),
        search_id.get()
    )

    cursor.execute(sql, values)
    connection.commit()

    messagebox.showinfo("Success", "Pet Updated Successfully!")

    clear_fields()
    view_pets()


def delete_pet():

    if search_id.get() == "":
        messagebox.showerror("Error", "Search a pet first")
        return

    cursor.execute(
        "DELETE FROM pet WHERE pet_id=%s",
        (search_id.get(),)
    )

    connection.commit()

    messagebox.showinfo("Success", "Pet Deleted Successfully!")

    clear_fields()
    view_pets()


def open_pet_window():

    global pet_name, species, breed, age
    global owner_name, phone
    global table, search_id

    pet = Toplevel()

    pet.title("Pet Management")
    pet.geometry("950x650")

    Label(
        pet,
        text="Pet Management",
        font=("Arial",18,"bold")
    ).grid(row=0,column=0,columnspan=4,pady=20)

    Label(pet,text="Pet Name").grid(row=1,column=0,padx=10,pady=5)
    pet_name = Entry(pet,width=30)
    pet_name.grid(row=1,column=1)

    Label(pet,text="Species").grid(row=2,column=0,padx=10,pady=5)
    species = Entry(pet,width=30)
    species.grid(row=2,column=1)

    Label(pet,text="Breed").grid(row=3,column=0,padx=10,pady=5)
    breed = Entry(pet,width=30)
    breed.grid(row=3,column=1)

    Label(pet,text="Age").grid(row=4,column=0,padx=10,pady=5)
    age = Entry(pet,width=30)
    age.grid(row=4,column=1)

    Label(pet,text="Owner Name").grid(row=5,column=0,padx=10,pady=5)
    owner_name = Entry(pet,width=30)
    owner_name.grid(row=5,column=1)

    Label(pet,text="Phone").grid(row=6,column=0,padx=10,pady=5)
    phone = Entry(pet,width=30)
    phone.grid(row=6,column=1)
    Label(pet, text="Pet ID").grid(row=7, column=0, padx=10, pady=10)
    search_id = Entry(pet, width=20)
    search_id.grid(row=7, column=1)

    Button(
        pet,
        text="Search",
        width=15,
        command=search_pet
    ).grid(row=7, column=2, padx=5)

    Button(
        pet,
        text="View Pets",
        width=15,
        command=view_pets
    ).grid(row=7, column=3, padx=5)

    Button(
        pet,
        text="Add Pet",
        width=15,
        command=add_pet
    ).grid(row=8, column=0, pady=15)

    Button(
        pet,
        text="Update Pet",
        width=15,
        command=update_pet
    ).grid(row=8, column=1)

    Button(
        pet,
        text="Delete Pet",
        width=15,
        command=delete_pet
    ).grid(row=8, column=2)

    Button(
        pet,
        text="Clear",
        width=15,
        command=clear_fields
    ).grid(row=8, column=3)

    table = ttk.Treeview(
        pet,
        columns=(
            "ID",
            "Name",
            "Species",
            "Breed",
            "Age",
            "Owner",
            "Phone"
        ),
        show="headings",
        height=12
    )

    table.heading("ID", text="ID")
    table.heading("Name", text="Pet Name")
    table.heading("Species", text="Species")
    table.heading("Breed", text="Breed")
    table.heading("Age", text="Age")
    table.heading("Owner", text="Owner Name")
    table.heading("Phone", text="Phone")

    table.column("ID", width=50)
    table.column("Name", width=140)
    table.column("Species", width=100)
    table.column("Breed", width=120)
    table.column("Age", width=60)
    table.column("Owner", width=140)
    table.column("Phone", width=120)

    table.grid(
        row=9,
        column=0,
        columnspan=4,
        padx=10,
        pady=20
    )

    view_pets()