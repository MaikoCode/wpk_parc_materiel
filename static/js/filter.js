var materiels = [];

document.getElementById("materiel").childNodes.forEach(function(option) {
    if (option.value) materiels.push(option);
});

function filterFunction() {
    var input, filter, select;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    select = document.getElementById("materiel");

    // Clear the options
    select.innerHTML = "";

    // Add only the options that match the filter
    materiels.forEach(function(option) {
        if (option.text.toUpperCase().indexOf(filter) > -1) {
            select.appendChild(option);
        }
    });
}