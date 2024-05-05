<h4 align='center'>
  
![Logo](https://github.com/emhash/Mini-Project-Python_2022/assets/109217697/c94e6138-76fd-487f-a62a-9ba0cb5c2e8a)

</h4>

<h4 align='center'>
  
![Static Badge](https://img.shields.io/badge/version-1.0.0-red)
![Static Badge](https://img.shields.io/badge/university_class_task_management_system-blue)
![Static Badge](https://img.shields.io/badge/python-django-green)
</h4>

<hr>
<h2 align='center'> Versity class task management system </h2>


<p>
This project is helpful for the CRs who suffers to manage the class tasks. Each time the CR has to mention about the re-shedule classes, new assignments, notify about the upcoming CT or Tests and so on. All these different task have to perform in different platform such as - Google Classroom, Messenger, Whatsapp or Google Sheet and so on, What if all these can be manage in one platform ? 
YES. This is the solution.
  
</p>

## Demo:

Live Website: https://bubtcr.pythonanywhere.com/
<br>
CR mail: demo@democr.com
<br>
Password: 111111qqqqqq

## Demo Screenshots

<div class="image-container">
<p align='center'>
<img alt="demo" width="400" src="https://github.com/emhash/Mini-Project-Python_2022/assets/109217697/3af3e280-4e5a-43ee-be56-cde7d4aa6a46">
<img alt="demo" width="400" src="https://github.com/emhash/Mini-Project-Python_2022/assets/109217697/a8f31d73-da7c-4c36-9348-c0fbe8efbac6">
<img alt="demo" width="400" src="https://github.com/emhash/Mini-Project-Python_2022/assets/109217697/56241c1b-3995-4def-9e8c-9b3238806dce">
<img alt="demo" width="400" src="https://github.com/emhash/Mini-Project-Python_2022/assets/109217697/1195905d-d885-41d4-a5ff-d7a5fe8c4ec0">
</p>
</div>



## Locally Setup

Note: You can add both MySQL or SQLite database. The configuration is added in the settings.py so you just have to uncomment the code and set database host, user, password and port. 

Warning: If you face any database related error then you have to add the information by using python-dot-env or directly in the code of MySQL setup.

Clone the repository & Navigate to the project directory:

```bash
  git clone https://github.com/emhash/Versity-Class-Management-System.git

  cd Versity-Class-Management-System
```

Create a virtual envoirnment:

```bash 
python -m venv myenv
```
Active virtual envoirnment with Bash terminal:
```bash 
source myenv/Scripts/activate
```
(You can activate the virtual envoirnment using any terminal. Based on the terminal the activation process of virtual envoirnment might be different)

Now install the necessary module & start the server:
```bash 
pip install -r requirements.txt
python manage.py runserver

```
** In case of migration problem migrate and then run the server **
```bash 
python manage.py makemigrations
python manage.py migrate

```
## Tech Stack

**Front-End:** Html, CSS, Bootstrap, JavaScript

**Back-End:** Django, Sqlite, Python


## Author

- [@emhash](https://www.github.com/emhash)

![App Screenshot](https://github.com/emhash/Mini-Project-Python_2022/assets/109217697/8434472f-afb6-4d0c-9eed-15ea24754167)


