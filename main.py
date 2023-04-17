import qrcode

def get_text(text):
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_001.png")

# Allow user Input to save Qrcode 
userUrl_001 = input("Enter your Url: ")
get_text(userUrl_001)