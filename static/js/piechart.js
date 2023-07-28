function getRandomColor() {
    let r = Math.floor(Math.random() * 256);
    let g = Math.floor(Math.random() * 256);
    let b = Math.floor(Math.random() * 256);
    return `rgb(${r}, ${g}, ${b})`;
}

let backgroundColors = sousCategoryNames.map(() => getRandomColor());



let chart = new Chart(document.getElementById('myPieCharte').getContext('2d'), {
    type: 'pie',
    data: {
        labels: sousCategoryNames,
        datasets: [{
            data: materielCounts,
            backgroundColor: backgroundColors,
        }]
    },
    options: {
        responsive: true,
        legend: {
            position: 'top',
        },
        title: {
            display: true,
            text: 'Répartition des matériels par sous-catégorie'
        },
        animation: {
            animateScale: true,
            animateRotate: true
        }
    }
});