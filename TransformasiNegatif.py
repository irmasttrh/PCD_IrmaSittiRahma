import cv2

img = cv2.imread("mammogram.jpg", 0)

img_neg = 255 - img

cv2.imshow("Original Image", img)
cv2.imshow("Negative Image", img_neg)

cv2.waitKey(0)
cv2.destroyAllWindows()
