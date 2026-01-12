import qrcode

n = input("Enter a Text or URL for QR scanner: ")

file = "Scanner.png" #used to save our qr code image in png

img = qrcode.make(n) #here we make variable that make qrcode image from user entered data 

img.save(file)  # this saves images as fie for our file 