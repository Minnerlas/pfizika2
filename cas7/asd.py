import cv2
vidcap = cv2.VideoCapture('snimci/referentni_klip.avi')
success,image = vidcap.read()
count = 0
while success:
    cv2.imwrite(f"frm/frame{count:03}.png", image)
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1
