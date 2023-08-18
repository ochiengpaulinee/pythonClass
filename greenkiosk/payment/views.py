from django.shortcuts import render,redirect
from .forms import PaymentUploadForm
from .models import Payment

# Create your views here.
def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment/payment_list.html', {'payments': payments})

def create_payment(request):
    if request.method == 'POST':
        form = PaymentUploadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment:payment_list')
    else:
        form = PaymentUploadForm()
    return render(request, 'payment/payment_upload.html', {'form': form})
