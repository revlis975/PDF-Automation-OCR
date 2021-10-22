import cv2

class cropGrid():
    def __init__(self) -> None:
        pass

    def crop(self, imgPath, no):
        image = cv2.imread(imgPath)
        original_image = image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 200)
        contours, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
        largest_item = sorted_contours[0]

        # cv2.waitKey(0)

        minx = 10000
        maxx = 0
        miny = 10000
        maxy = 0

        for i, c in enumerate(largest_item):

            if c[0][0] < minx:
                minx = c[0][0]
            elif c[0][0] > maxx:
                maxx = c[0][0]

            if c[0][1] < miny:
                miny = c[0][1]
            elif c[0][1] > maxy:
                maxy = c[0][1]

        x = minx
        w = maxx - minx
        y = miny
        h = maxy - miny
        crop_img = original_image[y:y + h, x:x + w]

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 1))
        border = cv2.copyMakeBorder(crop_img, 2, 2, 2, 2, cv2.BORDER_CONSTANT, value=[255, 255])
        resizing = cv2.resize(border, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        dilation = cv2.dilate(resizing, kernel, iterations=1)
        erosion = cv2.erode(dilation, kernel, iterations=2)

        cv2.imwrite('CroppedGrids/000{}.jpg'.format(no), erosion)