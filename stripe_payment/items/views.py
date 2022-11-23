import stripe
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from items.models import Item

from stripe_payment import config

stripe.api_key = config.STRIPE_API_KEY
YOUR_DOMAIN = config.YOUR_DOMAIN


class CancelView(TemplateView):
    template_name = "cancel.html"


class SuccessView(TemplateView):
    template_name = "success.html"


def item_list(request):
    template_name = "item_list.html"
    context = {"items": Item.objects.all()}
    return render(request, template_name, context)


def item_detail(request, pk):
    template_name = "item_detail.html"
    context = {"item": get_object_or_404(Item, pk=pk)}
    return render(request, template_name, context)


def buy_item(request, pk):
    item = get_object_or_404(Item, pk=pk)

    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "unit_amount": int(item.price) * 100,
                    "product_data": {"name": item.name},
                },
                "quantity": 1,
            },
        ],
        metadata={"item_id": item.id},
        mode="payment",
        success_url=YOUR_DOMAIN + "/success/",
        cancel_url=YOUR_DOMAIN + "/canceled/",
    )
    return redirect(checkout_session.url)
