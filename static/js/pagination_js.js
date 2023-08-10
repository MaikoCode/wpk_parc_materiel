let currentPage = {};

function loadMaterials(subcategory_id, direction = 0) {
    if (!currentPage[subcategory_id]) {
        currentPage[subcategory_id] = 1;
    }

    if (direction === 1) {
        currentPage[subcategory_id]++;
    } else if (direction === -1 && currentPage[subcategory_id] > 1) {
        currentPage[subcategory_id]--;
    }

    $.ajax({
        url: `/get_materials_for_subcategory/${subcategory_id}/${currentPage[subcategory_id]}/`,
        method: 'GET',
        dataType: 'json',
        success: function(response) {
             let materialsContainer = $(`#materiel-${subcategory_id} .list-group`);
            //let materialsContainer = $(`#materiel-${subcategory_id} .materials-list`);

            materialsContainer.empty();

            response.data.forEach(material => {
                materialsContainer.append(`
                    <div class="material-row" style="padding: 10px 20px; border-bottom: 1px solid #ccc; margin-bottom: 1%;">
                        <div class="d-flex flex-wrap align-items-center">
                            <div class="flex-grow-1">
                                <strong>Nom:</strong> ${material.nomMateriel}<br>
                                <strong>Numéro de série:</strong> ${material.NumSerie}<br>
                                <strong>Description:</strong> ${material.description}
                            </div>
                            <div>
                                <button type="button" class="btn btn-link edit-button" data-toggle="modal" data-target="#editModal-${material.idMateriel}">
                                    <i class="fas fa-edit"></i>
                                </button>
                                <button type="button" class="btn btn-link delete-button" data-toggle="modal" data-target="#deleteConfirmationModal-${material.idMateriel}" style="color: red;">
                                    <i class="fas fa-trash"></i>
                                </button>
                                <button type="button" class="btn btn-link history-button" data-toggle="modal" data-target="#historyModal-${material.idMateriel}">
                                    <i class="fas fa-history"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                `);
            });

            // Change the button visibility based on the page.
            if (currentPage[subcategory_id] <= 1) {
                $(`#prev-${subcategory_id}`).attr("disabled", true);
            } else {
                $(`#prev-${subcategory_id}`).attr("disabled", false);
            }

            if (!response.has_next) {
                $(`#next-${subcategory_id}`).attr("disabled", true);
            } else {
                $(`#next-${subcategory_id}`).attr("disabled", false);
            }

        },
        error: function(error) {
            console.error('Error loading materials:', error);
        }
    });
}

$(document).ready(function() {
    // Lorsque la page est chargée, pour chaque div de matériel, chargez les matériaux
    $('[id^=materiel-]').each(function() {
        let subCategoryId = $(this).data('id'); // Récupère la valeur de l'attribut 'data-id'
        loadMaterials(subCategoryId);
    });
});



