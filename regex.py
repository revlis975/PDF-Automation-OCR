import re

class Regex():
    def __init__(self) -> None:
        pass

    def emailPhone(self, r_easy_ocr):

        st = ""
        for i in r_easy_ocr:
            st = st + i[1] + " "

        regex_pairs = [
            [
                "Phone Number",
                r'\b[0-9]{10}\b'
            ],
            [
                "Email",
                r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\b'
            ]

        ]

        Extracted_data = []

        for [name, regex] in regex_pairs:
            Extracted_data.append(re.compile(regex).findall(st))

        return Extracted_data