import qrcode
upi_id = input("Enter your UPI id:")
Phonepay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
Googlepay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
Bharatpay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
Phonepay_qr = qrcode.make(Phonepay_url)
Googlepay_qr = qrcode.make(Googlepay_url)
Bharatpay_qr = qrcode.make(Bharatpay_url)
Phonepay_qr.save('phonepay_qr.png')
Googlepay_qr.save('googlepay_qr.png')
Bharatpay_qr.save('bharatpay_qr.png')
Phonepay_qr.show()
Googlepay_qr.show()
Bharatpay_qr.show()
