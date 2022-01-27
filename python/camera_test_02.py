import time
import shutil
import picamera
n = 0
print("running")
effects = ['none', 'negative', 'sketch', 'denoise', 'emboss', 'oilpaint', 'hatch', 'gpen', 'pastel', 'watercolor', 'film', 'blur', 'saturation']
with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    for s in effects:
        while n < 5:
            camera.image_effect = s
            camera.capture("../pics/" + s + ".jpg")
            n = n + 1
            print(n)
print("done")
