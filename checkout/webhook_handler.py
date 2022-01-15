"""
Initializes classes to handle Stripe webhooks.
"""
from django.http import HttpResponse


class StripeWH_Handler:  # pylint: disable=invalid-name
    """
    Handles Stripe webhooks.
    """
    def __init__(self, request):
        """
        Assigns 'request' as attribute of the class.
        """
        self.request = request

    def handle_event(self, event):
        """
        Handles a generic/unknown/unexpected webhook.
        """
        return HttpResponse(
            content=f'Webhook received {event["type"]}',
            status=200
        )