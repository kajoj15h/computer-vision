import cv2

img = cv2.imread(r'assets\grey.png', 0)
print(img)
cv2.imshow('img', img)

#tresh_binary = cv2.threshold(src=img, thresh=150, maxval=255, type=cv2.THRESH_BINARY)[1]
#cv2.imshow('tresh_binary', tresh_binary)

for thresh in [0, 50, 100, 150, 200]:
    tresh_binary =  cv2.threshold(src=img, thresh=thresh, maxval=255, type=cv2.THRESH_BINARY)[1]
    cv2.imshow(f'tresh_binary:, {thresh}', tresh_binary)
    cv2.waitKey(2000)
    cv2.destroyWindow(f'tresh_binary: {thresh}')

cv2.waitKey(0)