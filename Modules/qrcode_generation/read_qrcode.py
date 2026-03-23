import cv2

img = cv2.imread("some_file.png")

detector = cv2.QRCodeDetector()

data, bbox, _ =detector.detectAndDecode(img)

if data:
    print(f"Считаный QR-код: {data}")
else:
    print("QR-код не найден")