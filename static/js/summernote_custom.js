(function($) {
    $.extend($.summernote.plugins, {
        'uploadPDF': function(context) {
            var ui = $.summernote.ui;

            // Créez le bouton d'upload PDF
            var button = ui.button({
                contents: '<i class="fa fa-file-pdf"></i> Upload PDF',
                tooltip: 'Upload PDF',
                click: function() {
                    // Ouvrir une fenêtre modale pour l'upload de fichiers PDF
                    var modal = $('<div class="modal fade" tabindex="-1" role="dialog">');
                    var modalDialog = $('<div class="modal-dialog" role="document">');
                    var modalContent = $('<div class="modal-content">');
                    var modalHeader = $('<div class="modal-header">').html('<h5 class="modal-title">Upload PDF</h5><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>');
                    var modalBody = $('<div class="modal-body">');
                    var inputGroup = $('<div class="input-group mb-3">');
                    var inputFile = $('<input type="file" class="form-control" id="pdfFile" accept=".pdf" />');
                    var inputGroupAppend = $('<div class="input-group-append">');
                    var uploadButton = $('<button class="btn btn-primary" type="button">Upload</button>');

                    modal.on('hidden.bs.modal', function() {
                        modal.remove();
                    });

                    uploadButton.click(function() {
                        // Gérez ici l'upload du fichier PDF et l'insertion du lien dans Summernote
                        // Insérez le lien en utilisant context.invoke('editor.insertText', '...');

                        // Fermez la fenêtre modale
                        modal.modal('hide');
                    });

                    inputGroupAppend.append(uploadButton);
                    inputGroup.append(inputFile, inputGroupAppend);
                    modalBody.append(inputGroup);
                    modalContent.append(modalHeader, modalBody);
                    modalDialog.append(modalContent);
                    modal.append(modalDialog);
                    modal.modal('show');
                }
            });

            return button.render();
        }
    });
})(jQuery);
