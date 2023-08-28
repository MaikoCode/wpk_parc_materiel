var materiels = [];
var employes = [];
var materiels2 = [];
document.getElementById("materiel").childNodes.forEach(function(option) {
    if (option.value) materiels.push(option);
});

document.getElementById("employe").childNodes.forEach(function(option) {
    if (option.value) employes.push(option);
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

function filterFunctionEmploye() {
    console.log("hello");
    var input, filter, select;
    input = document.getElementById("myInputEmploye");
    filter = input.value.toUpperCase();
    select = document.getElementById("employe");

    // Clear the options
    select.innerHTML = "";

    // Add only the options that match the filter, excluding the default option
    employes.forEach(function(option) {
        if (option.text.toUpperCase().indexOf(filter) > -1 && option.value !== " ") {
            select.appendChild(option);
        }
    });
}


document.getElementById("materiel2").childNodes.forEach(function(option) {
    if (option.value) materiels2.push(option);
});

function filterFunctionMateriel() {
    var input, filter, select;
    input = document.getElementById("myInputMateriel");
    filter = input.value.toUpperCase();
    select = document.getElementById("materiel2");

    // Clear the options
    select.innerHTML = "";

    // Add only the options that match the filter
    materiels2.forEach(function(option) {
        if (option.text.toUpperCase().indexOf(filter) > -1) {
            select.appendChild(option);
        }
    });
}