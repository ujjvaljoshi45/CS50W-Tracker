document.addEventListener('DOMContentLoaded', async () => {
    expenseView();
});

function expenseView() {
    var expenseViewDiv = document.querySelector('#expense-view');
    fetch('/api/getExpenses')
    .then(response=>response.json())
    .then(async data => {
        // console.log(data);
        data.forEach(i => {
            console.log(i);
            var trackViewDiv = document.querySelector('#track-view-div');
            var trackItem = document.createElement('div');
            trackItem.className = 'track-item';
            trackItem.id = i.id;
            trackItem.style.border = '2px solid #ccc';
            trackItem.style.textAlign = 'center';
            trackItem.innerHTML = 
            `
                <h2>${i.name}</h2>
                <h3>${i.amount}</h3>
                <h4>${i.date}</h4>
                <p>${i.description}</p>
            `;
            trackViewDiv.appendChild(trackItem);
        });
    });
}