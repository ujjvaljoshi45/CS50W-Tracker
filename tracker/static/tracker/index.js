document.addEventListener('DOMContentLoaded', () => {
    getTotalAmount();
    document.querySelector('#add-money-btn').addEventListener('click', () => {
        addMoney();
    });
    document.querySelector('#add-expense-btn').addEventListener('click', () => {
        addExpense();
    });
});
function addExpense() {

    var newExpenseName = document.querySelector('#expense-name').value;
    var newExpenseAmount = document.querySelector('#expense-amount').value;
    var newExpenseDescription = document.querySelector('#expense-description').value;
    var newExpenseDate = document.querySelector('#expense-date').value;
    var newExpense = {
        name: newExpenseName,
        amount: newExpenseAmount,
        description: newExpenseDescription,
        date: newExpenseDate
    };

    fetch('/api/addExpense', {
        method: 'POST',
        body: JSON.stringify(newExpense)
    })
    .then(response => response.json())
    .then(data => {
        getTotalAmount();
        alert(data['message']);
        
    })
}

function addMoney() {
    var newAmount = document.querySelector('#new-amount').value;
        total_amount += parseFloat(newAmount);
        document.querySelector('#total-amount').innerHTML = `Total Amount : ${total_amount}`;
        document.querySelector('#add-money-form').reset();
        fetch('/api/addMoney', {
            method: 'POST',
            body: JSON.stringify({
                amount: `${newAmount}`
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            getTotalAmount();
        })
}

function getTotalAmount() {
    fetch('/api/getTotalAmount')
    .then(response => response.json())
    .then(data => {
        document.querySelector('#total-amount').innerHTML = `${data["totalAmount"]}`;
    });
}