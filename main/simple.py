from PIL import Image
import pytesseract
import numpy as np
import cv2


# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def OCR():
    # file = 'images/coffee.webp'
    file = ''

    # for i in range(65, 91):
    for i in range(0, 1):
        tresh = 0
        # file = 'archive/Images/Images/' + chr(i) + '/'
        file = './blockImage/blocks/'
        # letter = chr(i)
        topr = ''
        # print(file)
        for j in range(0, 72):
            img = np.array(Image.open(file + str(j) + '.jpg'))
            norm_img = np.zeros((img.shape[0], img.shape[1]))
            img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
            img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
            img = cv2.GaussianBlur(img, (1, 1), 0)

            # -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
            # text = pytesseract.image_to_string(img, lang = 'eng', config='--psm 10 --oem 0')
            text = pytesseract.image_to_string(img, config=("-c tessedit"
                    "_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    " --psm 10"
                    " -l eng"
                    " "))
            text = text.replace('\n', '')
            topr += text + ' '
            print(str(j) + ":" + text + ' ')
            # if letter in text:
            #     tresh += 1
        # print(topr)
        # print(letter + ': ' + str(tresh) + "/20") #'/14990')
        # norm_img = np.zeros((img.shape[0], img.shape[1]))

        # img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
        # img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
        # img = cv2.GaussianBlur(img, (1, 1), 0)

        # text = pytesseract.image_to_string(img, lang = 'eng', config='--psm 10')

        # print(text)




    # img1 = np.array(Image.open(file))
    # img = np.array(Image.open(file))

    # norm_img = np.zeros((img.shape[0], img.shape[1]))

    # img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
    # img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
    # img = cv2.GaussianBlur(img, (1, 1), 0)

    # text = pytesseract.image_to_string(img, lang = 'eng', config='--psm 10')

    # print(text)