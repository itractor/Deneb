# This is a sample Python script.
from pdfminer.high_level import extract_text
from io import StringIO
from pdfminer.high_level import extract_text_to_fp
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def scan():
    for page_layout in extract_pages("report.pdf"):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                print(element.get_text())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scan()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
