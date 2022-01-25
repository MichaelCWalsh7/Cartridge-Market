$(document).ready(function() {
    $('.dev-selector').css("color", "#aab7c4")
    $('.game-selector').css("color", "#aab7c4")
    $('.nintendo-games').css("display", "none")
    $('.sony-games').css("display", "none")
    $('.sega-games').css("display", "none")
    $('.atari-games').css("display", "none")
})

$('.dev-selector').change(function() {
    // Initializes variables for brevity within the function
    let devSelector = $('.dev-selector')
    let devSelectorOption = devSelector.val()


    if (devSelectorOption != 'default') {
        // If the option is not the default placeholder, the placeholder colour
        // is changed and only the correct options are displayed
        devSelector.css("color", "black")
        $('.all-games').css("display", "none")
        $('.nintendo-games').css("display", "none")
        $('.sony-games').css("display", "none")
        $('.sega-games').css("display", "none")
        $('.atari-games').css("display", "none")
        $(`.${devSelectorOption}-games`).css("display", "block")

    } else if (devSelector.val() == 'default') {
        // If the the placeholder option is reselected, the selector div 
        // returns to normal
        devSelector.css("color", "#aab7c4")
        $('.all-games').css("display", "block")
        $('.nintendo-games').css("display", "none")
        $('.sony-games').css("display", "none")
        $('.sega-games').css("display", "none")
        $('.atari-games').css("display", "none")
    }
})

$('.game-selector').change(function() {
    let gameSelector = $('.game-selector')
    let gameSelectorOption = gameSelector.val()

    if (gameSelectorOption != 'game-placeholder') {
        gameSelector.css("color", "black")

    } else if (gameSelectorOption == 'game-placeholder') {
        gameSelector.css("color", "#aab7c4")
    }
})

// Grabs the image filename and passes it through to the form on the backend.
$('#id_image').change(function() {
    let filepath = $('#id_image').val()
    let filename = filepath.split('\\').pop();
    $('input[name="image_url"]').val(filename)
})