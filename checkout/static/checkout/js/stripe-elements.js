/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// Initializes the keys from the json template filters in html
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
// With the above key, initializes an instance of Stripe
var stripe = Stripe(stripePublicKey);
// Then initializes an instance of Stripe elements
var elements = stripe.elements();

// Defines the style of the element for use
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#8f8f8f'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
// Uses this to create a card element
var card = elements.create('card', {
    style: style
});

// Mounts card element to a div present in checkout.html
card.mount('#card-element');
