from django.http  import HttpResponse
from django.shortcuts import render, redirect
from .models import Category,Location,Image

# Create your views here.
def home(request):
    try:
        # Converts data from the string Url
        images = Image.objects.all()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    locations = Location.objects.all()
    categories = Category.objects.all()

    return render(request, 'gallery/index.html', {"images":images, "locations":locations, "categories":categories})

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        images_category = request.GET.get('category')
        searched_category = Image.search_images_by_category(images_category)
        message = f"{images_category}"

        return render(request, 'gallery/search.html',{"message":message, "category_images":searched_category})

    else: 
        message = "You haven't searched for any term"
        return render(request, 'gallery/search.html', {"message":message})