from django.shortcuts import render
from .forms import FileUploadForm
from PIL import Image, ImageFilter

# Create your views here.
def index(request):
    posted = 0
    if request.method == 'POST' and posted == 0:
        posted += 1
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            my_filename = str(form.cleaned_data['image'])
            my_transformation = form.cleaned_data['transformation']

            if my_transformation.lower() == 'gray':
                image_file = Image.open('media/images/' + my_filename)
                image_file = image_file.convert('L')
                image_file.save('media/images/gray_' + my_filename)
                return render(request, "filtering.html", {'img_src': 'media/images/gray_' + my_filename})

            elif my_transformation.lower() == 'blur':
                image_file = Image.open('media/images/' + my_filename)
                blurred = image_file.filter(ImageFilter.BoxBlur(2))
                blurred.save('media/images/blurred_' + my_filename)
                return render(request, "filtering.html", {'img_src': 'media/images/blurred_' + my_filename})

            elif my_transformation.lower() == 'edge':
                image_file = Image.open('media/images/' + my_filename)
                edged = image_file.filter(ImageFilter.FIND_EDGES)
                edged.save('media/images/edged_' + my_filename)
                return render(request, "filtering.html", {'img_src': 'media/images/edged_' + my_filename})

            return render(request, "filtering.html", {'img_src': 'media/images/my_filename'})

    elif request.method == 'POST' and posted == 1:
        posted -= 1
        form = FileUploadForm()
    else:
        form = FileUploadForm()

    return render(request, 'image_upload.html', {'form': form})
