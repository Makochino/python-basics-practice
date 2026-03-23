import qrcode as qr
photo = qr.make('https://pypi.org/project/qrcode/')
type(photo)
photo.save("some_file.png")