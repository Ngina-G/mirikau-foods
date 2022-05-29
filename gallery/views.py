from django.http  import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'index.html')

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(home)

    return render(request, 'gallery/index.html')