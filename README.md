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
open console (powershell preferred) 
create a virtual environment using Conda (you must have Anaconda installed)
```
conda create --name software
```
activate it using 

if windows 
```
conda activate software
```
install the requirements.txt file
```
pip install -r --user requirements.txt
```
create a super user using the command
```
python manage.py createsuperuser
```
to run the server use the command
```
 python manage.py runserver'
```
 open the server at the link showing in the terminal
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
open the frontend server in the link showing
