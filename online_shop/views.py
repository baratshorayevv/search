from django.shortcuts import render, get_object_or_404
from .models import Product, Comment

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=product.category).exclude(pk=pk)[:4]
    comments = product.comments.all()
    return render(request, 'shop/product_detail.html', {'product': product, 'related_products': related_products, 'comments': comments})

def product_search(request):
    query = request.GET.get('q')
    products = []
    if query:
        products = Product.objects.filter(comments__body__icontains=query)
    return render(request, 'shop/product_search.html', {'products': products})
