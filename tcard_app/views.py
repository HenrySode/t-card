from django.shortcuts import render, redirect
from .forms import UploadFileForm, GenerateQRForm
from .models import TCard
import csv


def home(request):
    return render(request, "tcard_app/home.html")


def login(request):
    return render(request, "tcard_app/login.html")

def guests(request):
    return render(request, "tcard_app/guests.html")

def upload_data(request):
    pass
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             csv_file = request.FILES['file']
#             data = csv.reader(csv_file.read().decode('utf-8').splitlines())
#             for row in data:
#                 TCard.objects.create(
#                     unique_id=row[0],
#                     name=row[1],
#                     gender=row[2],
#                     phone_number=row[3],
#                     card_type=row[4]
#                 )
#             return redirect('upload_data')
#     else:
#         form = UploadFileForm()
#     return render(request, 'tcard_app/upload.html', {'form': form})



def event_details(request):
    return render(request, 'tcard_app/event_details.html')
#     total_sent_cards = TCard.objects.count()
#     scanned_single = TCard.objects.filter(scanned=1).count()
#     scanned_double = TCard.objects.filter(scanned=2).count()
#     remaining = total_cards - (scanned_single + scanned_double)
#     return render(request, 'tcard_app/event_details.html', {
#         'total_cards': total_cards,
#         'scanned_single': scanned_single,
#         'scanned_double': scanned_double,
#         'remaining': remaining,
#     })




def generate_qr(request):
    pass
#     if request.method == 'POST':
#         form = GenerateQRForm(request.POST)
#         if form.is_valid():
#             for card in TCard.objects.all():
#                 card.save()  # This will generate QR codes
#             return redirect('generate_qr')
#     else:
#         form = GenerateQRForm()
#     return render(request, 'tcard_app/generate_qr.html', {'form': form})






def card_scan(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            card = TCard.objects.get(unique_id=code)
            status, card_type = 'invalid', ''
            if card.card_type == 'Single' and card.scanned == 0:
                card.scanned = 1
                card.save()
                status, card_type = 'valid', 'single'
            elif card.card_type == 'Double' and card.scanned < 2:
                card.scanned += 1
                card.save()
                status, card_type = 'valid', 'double'
            return render(request, 'tcard_app/card_scan.html', {'status': status, 'card_type': card_type})
        except TCard.DoesNotExist:
            return render(request, 'tcard_app/card_scan.html', {'status': 'Invalid card'})
    return render(request, 'tcard_app/card_scan.html')

