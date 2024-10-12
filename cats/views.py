from django.shortcuts import render, get_object_or_404, redirect
from .models import Cat
from .forms import CatForm

# List of cats
def cat_list(request):
    cats = Cat.objects.all()
    return render(request, 'pages/cats/cat_list.html', {'cats': cats})

# View for a single cat
def cat_detail(request, pk):
    cat = get_object_or_404(Cat, pk=pk)
    return render(request, 'pages/cats/cat_detail.html', {'cat': cat})

# Add new cat
def cat_create(request):
    if request.method == 'POST':
        form = CatForm(request.POST, request.FILES)  # Accept files for image upload
        if form.is_valid():
            form.save()
            return redirect('cat_list')
    else:
        form = CatForm()
    return render(request, 'pages/cats/cat_form.html', {'form': form})

# Edit cat
def cat_update(request, pk):
    cat = get_object_or_404(Cat, pk=pk)
    if request.method == 'POST':
        form = CatForm(request.POST, request.FILES, instance=cat)  # Accept files for image upload
        if form.is_valid():
            form.save()
            return redirect('cat_detail', pk=cat.pk)
    else:
        form = CatForm(instance=cat)
    return render(request, 'pages/cats/cat_form.html', {'form': form})

# Delete cat
def cat_delete(request, pk):
    cat = get_object_or_404(Cat, pk=pk)
    if request.method == 'POST':
        cat.delete()
        return redirect('cat_list')
    return render(request, 'pages/cats/cat_confirm_delete.html', {'cat': cat})





