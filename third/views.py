from django.shortcuts import render, get_object_or_404
from third.models import Restaurant
from django.core.paginator import Paginator

from third.forms import RestaurantForm
from django.http import HttpResponseRedirect

def list(request):
    
    restaurants = Restaurant.objects.all()
    paginator = Paginator(restaurants, 5)
    
    page = request.GET.get('page')
    items = paginator.get_page(page)
    
    context = {
        'restaurants' : items
    }
    
    return render(request, 'third/list.html', context)


def detail(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    
    context = {
        'restaurant' : restaurant
    }
    
    return render(request, 'third/detail.html', context)






def delate(request, id):
    item = get_object_or_404(Restaurant, pk=id)
    item.delate()
    return HttpResponseRedirect('/third/list/')

