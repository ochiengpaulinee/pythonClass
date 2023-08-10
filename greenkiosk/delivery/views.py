from django.shortcuts import render
from .forms import DeliveryUploadForm

# Create your views here.
def delivery_upload_view(request):
    if request.method == "POST":
        form = DeliveryUploadForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form =  DeliveryUploadForm()
    return render(request,"delivery/delivery_upload.html",{"form":form})