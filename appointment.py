from tkinter import *
from tkinter import ttk, messagebox
from database import connection, cursor


def clear_fields():
    pet_id.delete(0, END)
    vet_id.delete(0, END)
    app_date.delete(0, END)
    reason.delete(0, END)
    search_id.delete(0, END)


def view_appointments():

    cursor.execute("SELECT * FROM appointment")
    rows = cursor.fetchall()

    for item in table.get_children():
        table.delete(item)

    for row in rows:
        table.insert("", END, values=row)


def add_appointment():

    if pet_id.get() == "" or vet_id.get() == "":
        messagebox.showerror("Error", "Pet ID and Vet ID are required")
        return

    sql = """
    INSERT INTO appointment
    (pet_id, vet_id, appointment_date, reason)
    VALUES(%s,%s,%s,%s)
    """

    values = (
        pet_id.get(),
        vet_id.get(),
        app_date.get(),
        reason.get()
    )

    cursor.execute(sql, values)
    connection.commit()

    messagebox.showinfo("Success", "Appointment Added Successfully!")

    clear_fields()
    view_appointments()


def search_appointment():

    if search_id.get() == "":
        messagebox.showerror("Error", "Enter Appointment ID")
        return

    cursor.execute(
        "SELECT * FROM appointment WHERE appointment_id=%s",
        (search_id.get(),)
    )

    row = cursor.fetchone()

    for item in table.get_children():
        table.delete(item)

    if row:

        table.insert("", END, values=row)

        pet_id.delete(0, END)
        vet_id.delete(0, END)
        app_date.delete(0, END)
        reason.delete(0, END)

        pet_id.insert(0, row[1])
        vet_id.insert(0, row[2])
        app_date.insert(0, row[3])
        reason.insert(0, row[4])

    else:
        messagebox.showinfo("Not Found", "Appointment not found")


def update_appointment():

    if search_id.get() == "":
        messagebox.showerror("Error", "Search an appointment first")
        return

    sql = """
    UPDATE appointment
    SET
    pet_id=%s,
    vet_id=%s,
    appointment_date=%s,
    reason=%s
    WHERE appointment_id=%s
    """

    values = (
        pet_id.get(),
        vet_id.get(),
        app_date.get(),
        reason.get(),
        search_id.get()
    )

    cursor.execute(sql, values)
    connection.commit()

    messagebox.showinfo("Success", "Appointment Updated Successfully!")

    clear_fields()
    view_appointments()


def delete_appointment():

    if search_id.get() == "":
        messagebox.showerror("Error", "Search an appointment first")
        return

    cursor.execute(
        "DELETE FROM appointment WHERE appointment_id=%s",
        (search_id.get(),)
    )

    connection.commit()

    messagebox.showinfo("Success", "Appointment Deleted Successfully!")

    clear_fields()
    view_appointments()


def open_appointment_window():

    global pet_id, vet_id
    global app_date, reason
    global search_id, table

    app = Toplevel()

    app.title("Appointment Management")
    app.geometry("950x650")

    Label(
        app,
        text="Appointment Management",
        font=("Arial",18,"bold")
    ).grid(row=0,column=0,columnspan=4,pady=20)

    Label(app,text="Pet ID").grid(row=1,column=0,padx=10,pady=5)
    pet_id = Entry(app,width=30)
    pet_id.grid(row=1,column=1)

    Label(app,text="Vet ID").grid(row=2,column=0,padx=10,pady=5)
    vet_id = Entry(app,width=30)
    vet_id.grid(row=2,column=1)

    Label(app,text="Appointment Date").grid(row=3,column=0,padx=10,pady=5)
    app_date = Entry(app,width=30)
    app_date.grid(row=3,column=1)

    Label(app,text="Reason").grid(row=4,column=0,padx=10,pady=5)
    reason = Entry(app,width=30)
    reason.grid(row=4,column=1)
    Label(app, text="Appointment ID").grid(row=5, column=0, padx=10, pady=10)
    search_id = Entry(app, width=20)
    search_id.grid(row=5, column=1)

    Button(
        app,
        text="Search",
        width=15,
        command=search_appointment
    ).grid(row=5, column=2, padx=5)

    Button(
        app,
        text="View Appointments",
        width=18,
        command=view_appointments
    ).grid(row=5, column=3, padx=5)

    Button(
        app,
        text="Add Appointment",
        width=18,
        command=add_appointment
    ).grid(row=6, column=0, pady=15)

    Button(
        app,
        text="Update Appointment",
        width=18,
        command=update_appointment
    ).grid(row=6, column=1)

    Button(
        app,
        text="Delete Appointment",
        width=18,
        command=delete_appointment
    ).grid(row=6, column=2)

    Button(
        app,
        text="Clear",
        width=18,
        command=clear_fields
    ).grid(row=6, column=3)

    table = ttk.Treeview(
        app,
        columns=(
            "ID",
            "Pet ID",
            "Vet ID",
            "Appointment Date",
            "Reason"
        ),
        show="headings",
        height=12
    )

    table.heading("ID", text="Appointment ID")
    table.heading("Pet ID", text="Pet ID")
    table.heading("Vet ID", text="Vet ID")
    table.heading("Appointment Date", text="Appointment Date")
    table.heading("Reason", text="Reason")

    table.column("ID", width=120)
    table.column("Pet ID", width=100)
    table.column("Vet ID", width=100)
    table.column("Appointment Date", width=180)
    table.column("Reason", width=300)

    table.grid(
        row=7,
        column=0,
        columnspan=4,
        padx=10,
        pady=20
    )

    view_appointments()