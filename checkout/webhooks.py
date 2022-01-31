"""
Defines the function that is called when Stripe webhooks are sent
"""
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

import stripe

from checkout.webhook_handler import StripeWH_Handler  # noqa: F401


@csrf_exempt
@require_POST
def webhook(request):
    """
    Listen for webhooks from Stripe
    """
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(  # noqa: F841
            payload, sig_header, wh_secret
        )
    except ValueError as e:  # noqa: F841
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:  # noqa: F841
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Sets up a webhook handler
    handler = StripeWH_Handler(request)

    # Maps webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_failed,
    }

    # Gets the webhook type from Stripe
    event_type = event['type']

    # If there's a handler for it, gets it from the event map
    event_handler = event_map.get(event_type, handler.handle_event)

    # Calls the event handler with the event
    response = event_handler(event)
    return response
