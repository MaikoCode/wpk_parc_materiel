const amounts = dataFromServer.map(item => item.total_montant);
let ctx = document.getElementById('myBarChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Jan','Feb','Mars','Apr','Mai','Juin','Juil','Aout','Sep','Oct','Nov','Dec'],
        datasets: [{
            label: 'Montants par mois',
            data: dataFromServer,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});