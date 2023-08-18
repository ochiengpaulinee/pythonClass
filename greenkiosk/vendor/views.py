from django.shortcuts import render
from .forms import VendorUploadForm
# Create your views here.


def vendor_upload_view(request):
    if request.method == "POST":
        form = VendorUploadForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form =  VendorUploadForm()
    return render(request,"vendor/vendor_upload.html",{"form":form})