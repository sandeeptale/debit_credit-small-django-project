Navigate to the project directory:

bash
Copy code
cd office-transaction-system
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply database migrations:

bash
python manage.py migrate
How to Run
Start the Django development server:

bash

python manage.py runserver
Access the application in your web browser at http://127.0.0.1:8000/.

Navigating to Project Folder and Files
To navigate to the project folder in the command line, use the cd command followed by the path to the project directory. For example:

bash

cd path/to/office-transaction-system
To access the project files, you can use a text editor or IDE of your choice. Open the project folder in your editor to view and modify the files.


also u can create a superusers


python manage.py createsuperuser


python manage.py runserver

and go to admin api than diectly access the database and also there add the things default

Usage
Click on "Home" to view the list of transactions.
Click on "Add Transaction" to add a new transaction.
