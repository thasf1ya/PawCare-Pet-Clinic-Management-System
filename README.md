# PawCare-Pet-Clinic-Management-System
# 🐾 PawCare – Pet Clinic Management System

A desktop-based pet clinic management application built with **Python Tkinter** and **MySQL** to manage pet records, veterinarian information, and appointments through a simple graphical user interface.

## 📌 Project Overview

PawCare is a Database Management System (DBMS) academic project designed to simplify veterinary clinic record management by replacing manual, paper-based record keeping with a structured relational database.

The application provides a user-friendly dashboard for managing pets, veterinarians, and appointments. It demonstrates fundamental database concepts, including CRUD operations, relational database design, primary and foreign keys, data validation, and SQL queries.

## ✨ Features

- **Dashboard:** Navigate between different management modules.
- **Pet Management:** Add, view, update, delete, and search pet records.
- **Veterinarian Management:** Manage veterinarian information and specializations.
- **Appointment Management:** Schedule, view, update, delete, and search appointments.
- **Relational Database:** Connect pets, veterinarians, and appointments using foreign keys.
- **Input Validation:** Validate user input before committing records to the database.
- **Persistent Storage:** Store and retrieve records using MySQL.

## 🛠️ Technologies Used

| Technology             | Purpose                        |
| ---------------------- | ------------------------------ |
| Python                 | Application logic              |
| Tkinter                | Graphical user interface (GUI) |
| MySQL                  | Relational database management |
| mysql-connector-python | Python–MySQL connectivity      |
| MySQL Workbench        | Database setup and management  |

## 🗄️ Database Design

The PawCare database consists of three main tables:

### 1. `pet`

Stores information about pets and their owners.

| Column       | Description                        |
| ------------ | ---------------------------------- |
| `pet_id`     | Primary key; unique pet identifier |
| `pet_name`   | Name of the pet                    |
| `species`    | Animal species                     |
| `breed`      | Breed of the pet                   |
| `age`        | Age in years                       |
| `owner_name` | Name of the pet's owner            |
| `phone`      | Owner's contact number             |

### 2. `veterinarian`

Stores veterinarian information.

| Column           | Description                                 |
| ---------------- | ------------------------------------------- |
| `vet_id`         | Primary key; unique veterinarian identifier |
| `vet_name`       | Veterinarian's name                         |
| `specialization` | Area of specialization                      |
| `phone`          | Contact number                              |

### 3. `appointment`

Stores appointment details and connects pets with veterinarians.

| Column             | Description                                   |
| ------------------ | --------------------------------------------- |
| `appointment_id`   | Primary key; unique appointment identifier    |
| `pet_id`           | Foreign key referencing `pet.pet_id`          |
| `vet_id`           | Foreign key referencing `veterinarian.vet_id` |
| `appointment_date` | Scheduled appointment date                    |
| `reason`           | Reason for the visit                          |

### Entity Relationships

- **Pet → Appointment:** One pet can have multiple appointments.
- **Veterinarian → Appointment:** One veterinarian can attend multiple appointments.
- Each appointment belongs to one pet and is associated with one veterinarian.

These relationships maintain referential integrity through primary and foreign key constraints.

## 📂 Project Structure

```text
PawCare/
├── main.py           # Main dashboard and application entry point
├── database.py       # Database connection and configuration
├── pet.py            # Pet management module
├── veterinarian.py   # Veterinarian management module
├── appointment.py    # Appointment management module
└── README.md         # Project documentation
```

*Note: The structure above reflects the project's intended organization. Adjust filenames if your actual repository differs.*

## ⚙️ Installation and Setup

### Prerequisites

Make sure you have installed:

- Python 3.x
- MySQL Server
- MySQL Workbench (optional, for database administration)

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd PawCare
```

Replace `<your-repository-url>` with your GitHub repository URL.

### Step 2: Install Dependencies

Install the MySQL connector:

```bash
pip install mysql-connector-python
```

Tkinter is generally included with standard Python installations. On some Linux systems, it may need to be installed separately.

### Step 3: Create the Database

Open MySQL Workbench or your MySQL client and execute:

```sql
CREATE DATABASE pawcare;
USE pawcare;
```

Create the required tables using the project's database schema. Ensure that the `pet` and `veterinarian` tables are created before the `appointment` table so that the foreign key relationships can be established.

### Step 4: Configure the Database Connection

Update the database connection settings in `database.py` to match your local MySQL configuration.

Make sure the database name is `pawcare` and configure the correct username, password, and host.

**Security note:** Do not upload real database passwords or other sensitive credentials to GitHub.

### Step 5: Run the Application

Start the application from the project directory:

```bash
python main.py
```

The PawCare dashboard should open, allowing you to navigate between the pet, veterinarian, and appointment management modules.


