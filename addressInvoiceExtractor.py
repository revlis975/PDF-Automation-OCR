# import easyocr
import cv2
import pytesseract
import numpy as np

class Address():
    def __init__(self) -> None:
        pass

    def addressInvoice(self, r_easy_ocr, st, path):

        img = cv2.imread(path)
        for i in r_easy_ocr:
            for c, j in enumerate(i):
                if c == 1:
                    if j == st:
                        bb = i[0]
        x = bb[0][0]
        y = bb[0][1]
        w = (bb[1][0] - bb[0][0]) + 400

        if st == "Invoice Number":
            h = (bb[2][1] - bb[1][1])
        else:
            h = (bb[2][1] - bb[1][1]) * 7

        crop_img = img[y:y + h, x:x + w]
        print("Running OCR on Cropped Image ....")

        # Use if you want accuracy over speed

        # reader = easyocr.Reader(['en'], gpu=False)
        # res = reader.readtext(crop_img)
        # abc = ""
        # for r in res:
        #     abc = abc + r[1] + " "

        # Use if you want speed over accuracy
        gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        sharpen_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
        thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        out = pytesseract.image_to_string(thresh)

        lines = out.split("\n")
        non_empty_lines = [line for line in lines if line.strip() != ""]

        abc = ""
        for r in non_empty_lines:
            abc = abc + r + " "

        return abc


# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         sharpen_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
#         sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
#         thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
#
#         out = pytesseract.image_to_string(thresh)
#         lines = out.split("\n")
#
#         non_empty_lines = [line for line in lines if line.strip() != ""]
#
#         abc = ""
#         for r in non_empty_lines:
#             abc = abc + r + " "