import qrcode

n = "Arya Waghmare is respected Vice President of Data Science Department." \
"He is S.Y.DS Student with rool no DS252054"

file = "Scanner.png"

img= qrcode.make(n)

img.save(file)