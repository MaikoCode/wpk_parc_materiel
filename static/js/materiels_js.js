// Gérer le basculement de la flèche de catégorie lors du clic
    $('.category-row').click(function (event) {
        event.stopPropagation();
        $(this).find('.collapse-indicator').toggleClass('collapsed');
        var target = $(this).data('target');
        $(target).toggleClass('show');
    });

    $('.sub-category-row').click(function (event) {
        event.stopPropagation();
        $(this).find('.collapse-indicator').toggleClass('collapsed');
        var target = $(this).data('target');
        $(target).toggleClass('show');
    });

    function handleCategoryChange(select) {
        var newCategoryInput = document.getElementById("new_category_input");
        var newCategoryOption = document.querySelector("#categorie option[value='new']");

        if (select.value === "new") {
            newCategoryInput.style.display = "block";
        } else {
            newCategoryInput.style.display = "none";
            document.getElementById("new_category_name").value = "";
            document.getElementById("new_category_description").value = "";
        }

        // Activer/désactiver les options de sous-catégorie en fonction de la catégorie sélectionnée
        var selectedCategoryId = select.value;
        var subCategoryOptions = document.querySelectorAll('.sub-category-option');
        for (const option of subCategoryOptions) {
            const optionCategory = option.dataset.category;
            option.disabled = optionCategory !== selectedCategoryId && optionCategory !== "";
        }
    }

    function handleSubCategoryChange(select) {
        var newSubCategoryInput = document.getElementById("new_sub_category_input");
        var newSubCategoryOption = document.querySelector("#sub_category option[value='new']");

        if (select.value === "new") {
            newSubCategoryInput.style.display = "block";
        } else {
            newSubCategoryInput.style.display = "none";
            document.getElementById("new_sub_category_name").value = "";
            document.getElementById("new_sub_category_description").value = "";
        }
    }
