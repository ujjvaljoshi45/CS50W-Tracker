# Tracker
Hey Reader!
Hope you will like my project!
So, The idea came up when I was struggling with my expenses in college. We all do.
So, I thought why not make an expense tracker of my own.
So here I am with a web application tracker

# Technicals
1. Models
I came up with 3 models
            - User
            - Expense
            - TotalAmount
i. User
This is a simple user model.
I used the same model that the course used

ii. Expense
Expense model will be used to store the expenses
name,amount,description everything you want to store for your expense

iii. TotalAmount
This model only constains track of the total amount you got (You can always add or remove money from your total amount)

2. Views
The web application got 3 views other then regular login and register views
The main layout file contains the navigation, greeting and Total Amount tracker 

i. Index
We got two forms over here
Add Money or Expense from this view

ii. track record
Here all the expenses that you had added so far are present

iii. about
A small note for the vistor

3. Urls
I had used apis to fetch data
in this way the web application takes very less no of reloads

i.add money
Api to add money that will return a message if the money is added or not

ii. add expense
Api to add expense that will use a function from views.py to do so
The expense will only be added if you have enough money
If there is not enough money the user will be notified 
Else the user will notified if the expense is added

iii. get expense
This api will be called to get all the expenses the user had added so far.
Then the data is presented in trackrecord.html webpage

iv. get total amount
This api will return total amount that is left with user

4. Javascript files
I had created two js files, as the things were mixing up too much.
in Index.js we got all the add functionality and control over index webpage

In ExpenseView we call api to get all the expenses and then we show it in html div
Like a list

5. CSS files
index.css and about.css are two css files
index.css controls the style of whole website exept about webpage

about.css contains balloon animation from https://codepen.io/bennettfeely/pen/DrNgoO

This was what I belive I truely learned so far from the course
So yeah thats it I think I am ready!

Thank You CS50 ❤️
Hope you will like it 🤞