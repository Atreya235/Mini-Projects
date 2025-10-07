import qrcode 

upi_id = input("Enter your UPI ID: ")

# create the format for the url
phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name"
googlepay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name"

# make the qrcode using the make() function
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
googlepay_qr = qrcode.make(googlepay_url)

# save the qr images using the save() function
phonepe_qr.save("PhonePe.png")
paytm_qr.save("Paytm.png")
googlepay_qr.save("GooglePay.png")  # ✅ you forgot `.save()` here

# show the qrcodes
phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()