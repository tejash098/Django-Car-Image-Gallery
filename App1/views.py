from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Image
from django.contrib.auth.decorators import login_required


def index(request):
    query = request.GET.get('query')
    images = Image.objects.all()
    if query:
        images = [i for i in images if query.lower() in i.title.lower() or query.lower() in i.description.lower()]
    return render(request, 'index.html', {'images': images})

@login_required(login_url='login')
def form(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        Image.objects.create(title=title, description=description, image=image)

        return render(request, 'index.html', {'images': Image.objects.all()})
    
    elif request.method == 'GET':
        return render(request, 'form.html')

@login_required(login_url='login')
def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    image.delete()
    return redirect('index')
    # return render(request, 'index.html', {'images': Image.objects.all()})

@login_required(login_url='login')
def update_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    if request.method == 'POST':
        image.title = request.POST.get('title')
        image.description = request.POST.get('description')
        image.image = request.FILES.get('image')
        image.save()
        return redirect('index')
    elif request.method == 'GET':
        return render(request, 'update.html', {'image': image})

