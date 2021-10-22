from imageConverter import ImageConverter
from ocrEngine import OCR
from gridItems import Grid
from regex import Regex
from addressInvoiceExtractor import Address
from excelWriter import Excel
import os
import merge_inv
import pymongo
from cropGrid import cropGrid
from counter import Counter
c=0

count = Counter()
def final():

    # converting PDFs to image
    img = ImageConverter()
    img.converter('PDFs')
    
    # applying OCR
    ocr = OCR()
    files = []
    imgPath = 'ConvertedImages'
    for filename in os.listdir(imgPath):
        files.append(os.path.join(imgPath, filename))
    
    for i, f in enumerate(files):
        print('Running on PDF {} .....'.format(i + 1))
        r_easy_ocr = ocr.engine(f)
        # Phone Number, E-mail Regex Parsing
        reg = Regex()
        Extracted_data = reg.emailPhone(r_easy_ocr)
    
        # cropping Grid Images
        crop = cropGrid()
        crop.crop(f, i + 1)
    
        # Address, Invoice Recognition
        add = Address()
        try:
            inv = add.addressInvoice(r_easy_ocr, 'Invoice Number', f)
        except:
            inv = add.addressInvoice(r_easy_ocr, 'Invoice No_', f)
        try:
            fr = add.addressInvoice(r_easy_ocr, 'From:', f)
        except:
            fr = add.addressInvoice(r_easy_ocr, 'FROM', f)
        try:
            to = add.addressInvoice(r_easy_ocr, 'To:', f)
        except:
            to = add.addressInvoice(r_easy_ocr, 'To', f)
    
        # writing in csv
        exc = Excel()
        name = 'GridCSVs/Data_Extraction0{}.xlsx'.format(i + 1)
        exc.write(Extracted_data, inv, fr, to, name)

    # Setting Cropped Grid Images
    gridPath = 'CroppedGrids'
    grids = []
    for filename in os.listdir(gridPath):
        grids.append(os.path.join(gridPath, filename))

    # Generating Grid Images
    for i, f in enumerate(grids):
        grid = Grid()
        grid.detect(f, i + 1)

    merge_inv.mergeInv()
    cr = count.count(c)
    print(cr)
