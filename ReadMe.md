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
# Usage
![index](https://github.com/ujjvaljoshi45/tracker/blob/main/images/index.jpg)


# Acknowledgements And References

[Django Documentation](https://docs.djangoproject.com/en/)

[CS50W](https://cs50.harvard.edu/web/2020/)

[Bootstrap](https://getbootstrap.com/)

[CodePen.io](https://codepen.io/bennettfeely/pen/DrNgoO)
