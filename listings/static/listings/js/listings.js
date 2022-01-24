$(document).ready(function() {
    $('.dev-selector').css("color", "#aab7c4")
    $('.nintendo-games').css("display", "none")
    $('.sony-games').css("display", "none")
    $('.sega-games').css("display", "none")
    $('.atari-games').css("display", "none")
})

$('.dev-selector').change(function() {
    // Initializes variables for brevity within the function
    let selector = $('.dev-selector')
    let selectorOption = selector.val()

    if (selectorOption != 'default') {
        // If the option is not the default placeholder, the placeholder colour
        // is changed and only the correct options are displayed
        selector.css("color", "black")
        $(`.${selectorOption}-games`).css("display", "block")
        $('.all-games').css("display", "none")

    } else if (selector.val() == 'default') {
        // If the the placeholder option is reselected, the selector div 
        // returns to normal
        selector.css("color", "#aab7c4")
        $('.all-games').css("display", "block")
        $('.nintendo-games').css("display", "none")
        $('.sony-games').css("display", "none")
        $('.sega-games').css("display", "none")
        $('.atari-games').css("display", "none")
    }
})