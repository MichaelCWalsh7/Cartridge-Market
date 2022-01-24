// Disables the 'DELETE' button until the delete check has been completed
$(document).ready(
    disableDelete()
)

function disableDelete() {
    $('#deleteStoreFrontButton').bind('click', false);
    $('#deleteStoreFrontButton').css("opacity", ".5")
    $('#deleteStoreFrontButton').css("cursor", "not-allowed")
}

$('#deleteCheck').keyup(function() {
    let deleteInput = $('#deleteCheck').val()
    if (deleteInput == 'delete') {
        $('#deleteStoreFrontButton').unbind('click', false);
        $('#deleteStoreFrontButton').css("opacity", "1")
        $('#deleteStoreFrontButton').css("cursor", "pointer")
    } else {
        disableDelete()
    }
})


// Grabs the image filename and passes it through to the form on the backend.
$('#id_image').change(function() {
    let filepath = $('#id_image').val()
    let filename = filepath.split('\\').pop();
    $('input[name="image_url"]').val(filename)
})