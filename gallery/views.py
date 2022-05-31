from django.http  import HttpResponse
from django.shortcuts import render, redirect
from .models import Category,Location,Image

# Create your views here.
def home(request):
    category =request.GET.get('category')
    try:
        category =request.GET.get('category')
        if category == None:
            images = Image.objects.all()
        else:
            images = Image.objects.filter(image_category__name=category)


    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    locations = Location.objects.all()
    categories = Category.objects.all()

    return render(request, 'index.html', {"images":images, "locations":locations, "categories":categories})

def navbar(request):
    location = request.GET.get('location')
    try:
        # category =request.GET.get('category')
        # location = request.GET.get('location'
        if location == None:
            images = Image.objects.all()
        else:
            images = Image.objects.filter(image_location__name=location)


    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    locations = Location.objects.all()
    categories = Category.objects.all()

    return render(request, 'gallery/locations.html', {"images":images, "locations":locations, "categories":categories})


def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        images_category = request.GET.get('category')
        searched_category = Image.search_images_by_category(images_category)
        message = f"{images_category}"

        return render(request, 'gallery/search.html',{"message":message, "category_images":searched_category})

    else: 
        message = "You haven't searched for any term"
        return render(request, 'gallery/search.html', {"message":message})

def image(request):
    # try:
    id = request.GET.get('id')
    image = Image.objects.get(id=id)
    # except DoesNotExist:
    #     raise Http404()
    return render(request, 'gallery/image.html', {"image":image})

