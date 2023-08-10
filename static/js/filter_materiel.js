function searchMaterial() {
    var filter = document.getElementById('searchInput').value.toLowerCase();
    var materials = document.querySelectorAll('.material-row');
    var found = false; // Pour vérifier si un matériel correspondant a été trouvé

    for (var i = 0; i < materials.length; i++) {
        var material = materials[i];
        var textContent = material.textContent.toLowerCase(); // Obtient tout le contenu textuel du matériel

        if (textContent.indexOf(filter) > -1) {
            material.style.display = "";

            // Trouvez la sous-catégorie parente de ce matériel
            var subCategoryContainer = material.closest('.collapse');

            // Déroulez cette sous-catégorie
            $(subCategoryContainer).collapse('show');

            // Trouvez la catégorie parente de cette sous-catégorie
            var categoryContainer = subCategoryContainer.closest('.collapse');

            // Déroulez cette catégorie
            $(categoryContainer).collapse('show');

            found = true;
            // Faire défiler jusqu'à l'élément
            window.scrollTo(0, material.offsetTop);
        } else {
            material.style.display = "none";
        }
    }

}

function resetSearch() {
    // Réinitialiser l'affichage de tous les éléments
    var materials = document.querySelectorAll('.material-row');
    for (var i = 0; i < materials.length; i++) {
        materials[i].style.display = "";
    }

    // Vider le champ de recherche
    document.getElementById('searchInput').value = "";

    // Réinitialiser l'affichage des catégories et sous-catégories
    var categories = document.querySelectorAll('.category-row, .sub-category-row');
    for (var i = 0; i < categories.length; i++) {
        categories[i].querySelector('.collapse-indicator').classList.remove('collapsed');
        var target = categories[i].dataset.target;
        document.querySelector(target).classList.remove('show');
    }
}
