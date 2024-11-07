import cv2
from ultralytics import YOLO

coco128 = open('./coco128.txt', 'r')

capture = cv2.VideoCapture('IMG_2845.mov')
class_list = coco128.read().split('\n')
coco128.close
model = YOLO("./yolov8n.pt")

while True:

    ret, frame = capture.read()
    if not ret:
        break

    detection = model(frame)[0]

    for data in detection.boxes.data.tolist():
        confidence = float(data[4])
        if confidence < 0.6:
            continue

        xmin, ymin, xmax, ymax = int(data[0]), int(data[1]), int(data[2]), int(data[3])
        cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

        label = class_list[int(data[5])]
        cv2.putText(frame, label, (xmin, ymin-5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(32) >= 0:
        break

capture.release()
