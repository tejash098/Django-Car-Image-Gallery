from django.shortcuts import render, HttpResponse
from .models import Image

# Create your views here.
def index(request):
    images = Image.objects.all()
    return render(request, 'index.html', {'images': images})

def form(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        Image.objects.create(title=title, description=description, image=image)

        return render(request, 'index.html', {'images': Image.objects.all()})
    
    elif request.method == 'GET':
        return render(request, 'form.html')

def delete_image(request, image_id):
    image = Image.objects.get(id=image_id)
    image.delete()
    return render(request, 'index.html', {'images': Image.objects.all()})

