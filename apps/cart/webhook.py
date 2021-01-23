import json
import stripe

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators import csrf_exempt

from .cart import Cart


@csrf_exempt
def webhook(request):
    payload = request.body
    event = None

    stripe.api_key = settings.STRIPE_API_KEY_HIDDEN

    try:
        event = stripe.Event.construct_from(json.load(payload), stripe.api_key)
    except ValueError as e:
        return HttpResponse(status=400)

    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object
        
         