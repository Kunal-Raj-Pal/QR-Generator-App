from django.shortcuts import render, redirect
import qrcode
import os
from datetime import datetime
from django.conf import settings

# Create your views here.

def qr_gen(req):
    qr_path = None

    if req.method == 'POST':
        qr_text = req.POST.get("qr_text")
        print(qr_text)
        # qr_text = "Hello! VS-Code" 
        qr = qrcode.make(qr_text)

        save_folder = os.path.join(settings.MEDIA_ROOT, 'images')
        os.makedirs(save_folder, exist_ok=True)
        
        filename = f"img_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"

        filepath = os.path.join(save_folder,filename)
        qr.save(filepath)

        return redirect(f"/?img=images/{filename}")


    qr_path = req.GET.get("img")
    full_url = settings.MEDIA_URL + qr_path if qr_path else None

    return render (req, "index.html", {'qr_path': full_url})