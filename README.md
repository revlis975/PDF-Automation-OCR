# PDF-Automation-OCR
A website powered by an OCR engine that extracts data like address, email, data grids and so on, and presents it in a downloadable excel file

## Instructions to install and run

1. Download the zip file and unzip it at a suitable location 

2. Dependency installation
  - Install poppler and put it in the system variables path. Steps for that [here](https://stackoverflow.com/questions/18381713/how-to-install-poppler-on-windows).
  - Intsall tesseract and put it in the system variables path. Steps are [here](https://stackoverflow.com/questions/46140485/tesseract-installation-in-windows#fromHistory).
  - Install python and put it in the path as well.
  
3. Create a virtual environment

  - Open the file location on command prompt and install virtual env using `pip install virtualenv` if you don't have it pre-installed
  - Create the virtual environment using `virtualenv env`
  - Activate it with `.\env\Scripts\activate`
  - Now install all required modules with one command `pip install fastapi[all] pytesseract easyOCR pdf2image fitz PyMuPDF xlsxwriter pymongo`
  
4. Run the app using `uvicorn server:app --reload` and visit the url that uvicorn shows it's running on.

## What a successful run looks like

<img src="https://github.com/revlis975/PDF-Automation-OCR/blob/master/working.gif" alt="A successful run looks like this" width="750" height="400">
