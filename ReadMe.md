# Tracker
Final Project [CS50's Web Programming with Pyhton and JavaScript](https://cs50.harvard.edu/web).

Thank you CS50 team❤️ for amazing course and the experience.

## About Tracker
Tracker is your pocket tracker it helps you keep a track of your money.

In Tracker you can add your money that you got to spend.
Every time you do some expense come to tracker and register it on the tracker.
In this way we can never lose track of our expenses.

Tracker is a part of project ExpenseManager.

## Distinctiveness and Complexity

Tracker is very much distinct from all other projects in this course.
It is also not based on the old CS50W Pizza project.

Tracker i made with Django using 3 models and JavaScript.

The web application is mobile responsive.

## Overview

|   Filename    |   Description|
| :---: | :---: |
| ``tracker/models.py`` | Contains three models User, Expense and TotalAmount.  |
| ``tracker/views.py``  | All the main implementation of web application is in views.py.    |
| ``tracker/urls.py``   | All the urls and apis are listing in the urls.py. |
| ``tracker/static/index.js``   | Contains the JavaScript Code for index page which will add money and expense. |
| ``tracker/static/ExpenseView.js`` | Contain JavaScript to maintain the trackrecord.html. It will load all the expenses that the user had added so far.    |
| ``tracker/static/style.css``  | CSS for the style of webpages.    |
| ``tracker/static/about.css``  | Contains Animation for about me page. |
| ``tracker/templates`` | This folder contains all the html pages that are available.   |

## Build with

[![VSCODE](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/docs)

## How to Run
1. Clone or download the repo
2. Open a terminal and locate the folder containing manage.py file
3. Make sure that latest version of python and django are already installed
4. Install the requirements using ``pip install -r requirements.txt``
5. Run django server
```
python manage.py runserver
```
6. Open your browser and go to the url
```
127.0.0.1:8000
```
## How to Use
1. On firing 127.0.0.1:8000 you will land on this page.
You have to sign in to your account (if you have register) to get all your records. <br>

![login](https://github.com/ujjvaljoshi45/tracker/blob/main/images/login.jpg)

2. By clicking on 'register' hyper link at the botton you will land on the register page.Over here if you are a new user you have to register your self first add you username you wish to use and confirm your password.<br>

![register](https://github.com/ujjvaljoshi45/tracker/blob/main/images/register.jpg)

3. Now you will land on the main page of the website by signing in

![index](https://github.com/ujjvaljoshi45/tracker/blob/main/images/index.jpg)
<br>
-> On the index page we have most of our web app<br>
-> You can add money to the add or expense.<br>
-> There is a bar at top right displaying the total sum you have in your account<br>
-> And then we have a navigation bar at the top of the page from where you can navigate to the different parts of the webpage<br>
<br>
4. Add Money

![add money](https://github.com/ujjvaljoshi45/tracker/blob/main/images/add%20money.jpg)<br>

-> Fill some value at the given bar and add the amount you just earned to the application<br>

5. Add Expense<br>

![add expense](https://github.com/ujjvaljoshi45/tracker/blob/main/images/add%20expense.jpg)<br>

-> This part is used to add expense to the tracker<br>
-> Note that you can only add expense to the app only if you have enough money in the application<br>
-> Adding expense that is more thant the money you have in the app will result in throwing an alert says "Not having enough money'!<br>
-> Else you expense will be added<br>

6. View Expense

![view expense](https://github.com/ujjvaljoshi45/tracker/blob/main/images/view%20expense.jpg)

-> Now the final part of the application where all the expenses that you have made so far are listed<br>
-> It will list all the expenses along with expense name, amount, date and description<br>


## Acknowledgements And References

[Django Documentation](https://docs.djangoproject.com/en/)

[CS50W](https://cs50.harvard.edu/web/2020/)

[Bootstrap](https://getbootstrap.com/)

[CodePen.io](https://codepen.io/bennettfeely/pen/DrNgoO)
