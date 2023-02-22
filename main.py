import argparse
import cv2

vcap = cv2.VideoCapture("rtsp://admin:admin@192.168.101.8:554/ch0_0.264", cv2.CAP_FFMPEG)
ret, frame = vcap.read()
cv2.imwrite("out.png", frame)