import picamera
import linecache
from datetime import datetime

# import the DESTINATION variable from the config file:
destination_with_trailing_n=linecache.getline('../dc.config', 23)

# strip the trailing "\n" of the imported string:
destination = destination_with_trailing_n.rstrip('\n')

## import the VIDEO LENGHT variable from the config file:
#video_lenght_with_trailing_n=linecache.getline('../dc.config', 26)

## strip the trailing "\n" of the imported string:
#video_lenght = video_lenght_with_trailing_n.rstrip('\n')

camera = picamera.PiCamera(resolution=(1920, 1080),framerate=30)

camera.video_stabilization = True

for filename in camera.record_sequence(
        destination+(datetime.now().strftime('%Y-%m-%d__%H-%M-%S'))+'_%d.h264' % i for i in range(1, 1111)):
    camera.wait_recording(300)
