from django.db import models

class TCard(models.Model):
    unique_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    card_type = models.CharField(max_length=10)
    scanned = models.IntegerField(default=0)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def save(self, *args, **kwargs):
        import qrcode
        from django.core.files import File
        from io import BytesIO

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.unique_id)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        self.qr_code.save(f'{self.unique_id}.png', File(buffer), save=False)
        super().save(*args, **kwargs)


class Event(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=20)
    date_issues = models.DateTimeField(auto_now_add = True)
    event_date = models.DateField()
    total_invited_guest = models.CharField(max_length=20)
     
    description = models.TextField(blank=True)
    
    
class Scan(models.Model):
    guest = models.ForeignKey(TCard, on_delete=models.CASCADE)
    scanned_at = models.DateTimeField(auto_now_add=True)
    scan_count = models.IntegerField(default=0)
    
    
