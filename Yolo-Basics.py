from ultralytics import YOLO
import cv2

model = YOLO('../Yolo-Weights/yolov8n.pt')
results = model("Images/", show=True, save=True)

#img = model("Images/dsi-siang.jpg",  save=True)


#cv2.imwrite("result.jpg", img)

cv2.waitKey(0)