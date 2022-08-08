
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from store.models import Product, Collection, Order, OrderItem


def say_hello(request):

    return render(request, 'hello.html', {'name': 'Mosh'})
