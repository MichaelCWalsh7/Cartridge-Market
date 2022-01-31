$(document).ready(function() {
    $('.dev-selector').css("color", "#aab7c4")
    let pageTitle = $('.page-title-text').text()
    if (pageTitle =="Edit a Game") {
        $('.dev-selector').css("color", "black")
    }
})

$('.dev-selector').change(function() {
    let devSelectorValue = $('.dev-selector').val()
    if (devSelectorValue == "default") {
        $('.dev-selector').css("color", "#aab7c4")
    } else if (devSelectorValue == "Nintendo" || "Sony" || "Sega" || "Atari") {
        $('.dev-selector').css("color", "black")
    }
    
})

// Grabs the image filename and passes it through to the form on the backend.
$('#id_image').change(function() {
    let filepath = $('#id_image').val()
    let filename = filepath.split('\\').pop();
    $('input[name="image_url"]').val(filename);
    console.log("Name = " + filename)
})

