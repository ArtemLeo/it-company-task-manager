# Task manager for IT company

**Task Manager** is a simple web application built with Django 5.1 for managing tasks, workers and positions.

## Check this out!

[Task Manager project deployed to Render](https://it-company-task-manager-project.onrender.com)

You can use the following user to log in:

```
login: user
password: user12345
```

## Installation

Run the following code in terminal:

```shell
git clone https://github.com/ArtemLeo/it-company-task-manager-project.git
cd it-company-task-manager
python3 -m venv venv
source venv/bin/activate (for MacOS)
venv\Scripts\activate (for Windows)
pip3 install -r requirements.txt
python3 manage.py runserver
```

After that, you can easily open the project in your browser.

### For testing with data

- Use this command to load prepared data from the fixture:

`python manage.py loaddata task_manager_db_data.json`

- After loading data from the fixture you can use the following superuser:

```
login: admin.user
password: 1qazcde3
```

## Features

- **User Authentication**: The application allows users to create new accounts, log in, and log out.
- **Task Management**: Users can create, view, update, and delete tasks and task types. Additionally,
there is a search function to look up tasks by name. 
- **Workers Management**: Users can search for other workers by username and view details of 
the workers and tasks they are assigned to.
- **Home page**: On the main page of the application, users can view the number of workers, 
positions, and task types currently created at their company.

#### Home Page:
![image](images/home_page.png)

#### DB Structure:
![image](images/db_structure.png)

#### Task List:
![image](images/task_list.png)

#### Random Worker:
![image](images/worker.png)

#### Log In:
![image](images/log_in.png)

#### All Positions:
![image](images/positions.png)

#### All Workers:
![image](images/workers.png)
