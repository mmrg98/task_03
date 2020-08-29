from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    "my_list":[{"restaurant_name":"Mac", "food_type":"Burger"},
    {"restaurant_name":"Pizza Hut","food_type":"Pizza"},
    {"restaurant_name":"Steak House","food_type":"Steak"}]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object":{"restaurant_name":"Steak House","food_type":"Steak"}

    }
    return render(request, 'detail.html', context)
