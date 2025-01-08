import cv2

from src.component.camera.usb_camera import UsbCamera

camera = UsbCamera(0)

try:
  while True:
    image = camera.capture()
    frame = image.get_value()
    cv2.imshow("Test", frame)
    cv2.waitKey(1)
except KeyboardInterrupt:
  print("end")
finally:
  cv2.destroyAllWindows()
