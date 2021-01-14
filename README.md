Copy the project files
```
git clone https://github.com/mohamedar97/HotelManagmentSystem
```
```
cd HotelManagmentSystem/
```
# Backend server
```
cd Backend/
```
open console 
create a virtual environment using (you must have python 3.x installed)
```
python3 -m venv /path/to/new/virtual/environment
```
activate it using 
if Linux 
```
$ source <venv>/bin/activate
```
if windows 
```
C:\> /path/to/new/virtual/environment\Scripts\activate.bat
```
cd into the project directory
 install the requirements.txt file
```
pip install -r requirements.txt
```
 run command
```
 python manage.py runserver'
```
 to go to the dashboard:
	A - to create super user run command
	``` 
	python manage.py createsuperuser'
	```  
	B - go to 'localhost/appadmin' 
	C - sign in with your super user account
# Frontend  
```
cd ../Frontend/
```
To run the frontend server use the following commands (you need nodeJS installed)
```
npm install
```
```
npm run serv
```
