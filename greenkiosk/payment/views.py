from django.shortcuts import render
from .forms import PaymentUploadForm
from .models import Payment
# from django.shortcuts import render,redirect

# Create your views here.
def payment_upload_view(request):
    if request.method == "POST":
        form = PaymentUploadForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form =  PaymentUploadForm()
    return render(request,"payment/payment_upload.html",{"form":form})

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, "payment/payment_list.html", {"payment":payment})