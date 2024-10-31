import cv2

capture = cv2.VideoCapture(0)

while True:

    ret, frame = capture.read()

    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    hit, wth, dth = frame.shape
    
    for i in range(hit):
        for j in range(wth//2):
            frame[i][j] = frame[i][wth - 1 - j]

    cv2.imshow("Frame", frame)

    if cv2.waitKey(32) >= 0:
        break

capture.release()