import cv2
from pyzbar.pyzbar import decode
import numpy as np


camara = cv2.VideoCapture(0)

print("📷 Apuntá un código QR a la cámara...")

while True:
    ret, frame = camara.read()
    if not ret:
        break

    
    for qr in decode(frame):
        data = qr.data.decode('utf-8')
        print("✅ QR detectado:", data)

        
        pts = qr.polygon
        pts = [(p.x, p.y) for p in pts]
        cv2.polylines(frame, [np.array(pts, dtype="int32")], True, (0,255,0), 2)

    
    cv2.imshow("Lector QR", frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camara.release()
cv2.destroyAllWindows()
