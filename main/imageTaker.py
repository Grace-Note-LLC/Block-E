import cv2
import time

cam = cv2.VideoCapture(1)

def take():
	while True:
		ret, image = cam.read()
		h_GRID_SIZE = 60
		w_GRID_SIZE = 70
		y = 0
		x = 0
		image = image[y:y+(h_GRID_SIZE*8), x:x+(w_GRID_SIZE*9)]

		height, width, channels = image.shape
		for i in range(0, height - 1, h_GRID_SIZE):
			cv2.line(image, (0,i), (width, i), (255, 0, 0), 1, 1)
		for i in range(0, width - 1, w_GRID_SIZE):
			cv2.line(image, (i, 0), (i, height), (255, 0, 0), 1, 1)
		cv2.imshow('Imagetest',image)
		k = cv2.waitKey(7)
		if k != -1:
			break
	cv2.imwrite('./blockImage/big.jpg', image)
	time.sleep(2)
	cv2.imwrite('./blockImage/big2.jpg', image)
	cam.release()
	cv2.destroyAllWindows()