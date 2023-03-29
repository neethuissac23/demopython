from django.shortcuts import render
from ecommerceapp.models import Product
from django.db.models import Q


# Create your views here.
def search(request):
    products = None
    query = None
    if request.method == "GET":
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
        return render(request, 'search.html', {'query': query, 'products': products})
