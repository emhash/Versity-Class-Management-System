
# Versity class task management system




## Locally Setup

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
(You can activate the virtual envoirnment using any terminal)

Now install the necessary module & start the server:
```bash 
pip install -r requirements.txt
python manage.py runserver

```
** In case of migration problem migrate and then run the server **
```bash 
python manage.py migrate
python manage.py makemigrations

```
## Tech Stack

**Front-End:** Html, CSS, Bootstrap, JavaScript

**Back-End:** Django, Sqlite, Python


## Author

- [@emhash](https://www.github.com/emhash)

