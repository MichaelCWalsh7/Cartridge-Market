"""
Defines the function that is called when Stripe webhooks are sent
"""
# pylint: disable=broad-except,invalid-name
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

import stripe

from checkout.webhook_handler import StripeWH_Handler


@require_POST
@csrf_exempt
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

    print('Success!')
    return HttpResponse(status=200)
