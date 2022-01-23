$('#id_image').change(function() {
    let filepath = $('#id_image').val()
    let filename = filepath.split('\\').pop();
    $('input[name="image_url"]').val(filename)
})