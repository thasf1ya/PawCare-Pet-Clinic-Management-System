from tkinter import *
from tkinter import ttk, messagebox
from database import connection, cursor


def clear_fields():
    vet_name.delete(0, END)
    specialization.delete(0, END)
    phone.delete(0, END)
    search_id.delete(0, END)


def view_vets():

    cursor.execute("SELECT * FROM veterinarian")
    rows = cursor.fetchall()

    for item in table.get_children():
        table.delete(item)

    for row in rows:
        table.insert("", END, values=row)


def add_vet():

    if vet_name.get() == "":
        messagebox.showerror("Error", "Vet Name is required")
        return

    sql = """
    INSERT INTO veterinarian
    (vet_name, specialization, phone)
    VALUES(%s,%s,%s)
    """

    values = (
        vet_name.get(),
        specialization.get(),
        phone.get()
    )

    cursor.execute(sql, values)
    connection.commit()

    messagebox.showinfo("Success", "Veterinarian Added Successfully!")

    clear_fields()
    view_vets()


def search_vet():

    if search_id.get() == "":
        messagebox.showerror("Error", "Enter Vet ID")
        return

    cursor.execute(
        "SELECT * FROM veterinarian WHERE vet_id=%s",
        (search_id.get(),)
    )

    row = cursor.fetchone()

    for item in table.get_children():
        table.delete(item)

    if row:

        table.insert("", END, values=row)

        vet_name.delete(0, END)
        specialization.delete(0, END)
        phone.delete(0, END)

        vet_name.insert(0, row[1])
        specialization.insert(0, row[2])
        phone.insert(0, row[3])

    else:
        messagebox.showinfo("Not Found", "Veterinarian not found")


def update_vet():

    if search_id.get() == "":
        messagebox.showerror("Error", "Search a vet first")
        return

    sql = """
    UPDATE veterinarian
    SET
    vet_name=%s,
    specialization=%s,
    phone=%s
    WHERE vet_id=%s
    """

    values = (
        vet_name.get(),
        specialization.get(),
        phone.get(),
        search_id.get()
    )

    cursor.execute(sql, values)
    connection.commit()

    messagebox.showinfo("Success", "Veterinarian Updated Successfully!")

    clear_fields()
    view_vets()


def delete_vet():

    if search_id.get() == "":
        messagebox.showerror("Error", "Search a vet first")
        return

    cursor.execute(
        "DELETE FROM veterinarian WHERE vet_id=%s",
        (search_id.get(),)
    )

    connection.commit()

    messagebox.showinfo("Success", "Veterinarian Deleted Successfully!")

    clear_fields()
    view_vets()


def open_vet_window():

    global vet_name, specialization, phone
    global search_id, table

    vet = Toplevel()

    vet.title("Veterinarian Management")
    vet.geometry("950x650")

    Label(
        vet,
        text="Veterinarian Management",
        font=("Arial",18,"bold")
    ).grid(row=0,column=0,columnspan=4,pady=20)

    Label(vet,text="Vet Name").grid(row=1,column=0,padx=10,pady=5)
    vet_name = Entry(vet,width=30)
    vet_name.grid(row=1,column=1)

    Label(vet,text="Specialization").grid(row=2,column=0,padx=10,pady=5)
    specialization = Entry(vet,width=30)
    specialization.grid(row=2,column=1)

    Label(vet,text="Phone").grid(row=3,column=0,padx=10,pady=5)
    phone = Entry(vet,width=30)
    phone.grid(row=3,column=1)
    Label(vet, text="Vet ID").grid(row=4, column=0, padx=10, pady=10)
    search_id = Entry(vet, width=20)
    search_id.grid(row=4, column=1)

    Button(
        vet,
        text="Search",
        width=15,
        command=search_vet
    ).grid(row=4, column=2, padx=5)

    Button(
        vet,
        text="View Vets",
        width=15,
        command=view_vets
    ).grid(row=4, column=3, padx=5)

    Button(
        vet,
        text="Add Vet",
        width=15,
        command=add_vet
    ).grid(row=5, column=0, pady=15)

    Button(
        vet,
        text="Update Vet",
        width=15,
        command=update_vet
    ).grid(row=5, column=1)

    Button(
        vet,
        text="Delete Vet",
        width=15,
        command=delete_vet
    ).grid(row=5, column=2)

    Button(
        vet,
        text="Clear",
        width=15,
        command=clear_fields
    ).grid(row=5, column=3)

    table = ttk.Treeview(
        vet,
        columns=(
            "ID",
            "Name",
            "Specialization",
            "Phone"
        ),
        show="headings",
        height=12
    )

    table.heading("ID", text="ID")
    table.heading("Name", text="Vet Name")
    table.heading("Specialization", text="Specialization")
    table.heading("Phone", text="Phone")

    table.column("ID", width=80)
    table.column("Name", width=220)
    table.column("Specialization", width=220)
    table.column("Phone", width=180)

    table.grid(
        row=6,
        column=0,
        columnspan=4,
        padx=10,
        pady=20
    )

    view_vets()