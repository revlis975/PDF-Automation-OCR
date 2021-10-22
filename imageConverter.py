from pdf2image import convert_from_path
import os
import fitz

class ImageConverter():
    def __init__(self) -> None:
        pass

    def converter(self, pdfPath):

        files = []
        for filename in os.listdir(pdfPath):
            files.append(os.path.join(pdfPath, filename))

        # for i, f in enumerate(files):
        #     images = convert_from_path(f)
        #     resized = cv2.resize(images, (720,1080))
        #     for image in resized:
        #         image.save('ConvertedImages/000{}.jpg'.format(i+1), 'JPEG')

        for i, f in enumerate(files):
            doc = fitz.open(f)
            page = doc.loadPage(0)  # number of page
            pix = page.getPixmap(matrix=fitz.Matrix(150/72,150/72))
            output = "ConvertedImages/000{}.jpg".format(i + 1)
            pix.writePNG(output)
