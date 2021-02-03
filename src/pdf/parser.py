from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
from settings import TECH_HEIGHT_THRESH, TECH_WIDTH_THRESH, HEADER_THRESH, FOOTER_THRESH


def extract_information(pdf_file_path):

    print(f"[INFO] Parsing {pdf_file_path}...")

    pdf_info = {}
    categories = []
    tech_ret = False
    for page_layout in extract_pages(pdf_file_path):
        page_height = page_layout.height
        page_width = page_layout.width
        sorted_page_layout = sorted(page_layout._objs, key=lambda k: k.y1, reverse=True)
        for element in sorted_page_layout:
            if isinstance(element, LTTextContainer):
                element_text = element.get_text().replace("\n", "")
                element_y = element.y1
                element_x = element.x1
                if element_y > HEADER_THRESH * page_height or element_y < FOOTER_THRESH * page_height:
                    continue
                if element_text == "Technologies" and element_y > TECH_HEIGHT_THRESH * page_height and \
                        element_x < TECH_WIDTH_THRESH * page_width:
                    tech_ret = True
                    continue
                if not tech_ret and element_y < (TECH_HEIGHT_THRESH - 0.05) * page_height:
                    break
                if tech_ret:
                    element_font = element._objs[0]._objs[0].fontname
                    if "Bold" in element_font:
                        categories.append(element_text)
                        pdf_info[categories[-1]] = []
                        continue
                    pdf_info[categories[-1]].append(element_text)

    return pdf_info


if __name__ == '__main__':
    extract_information(pdf_file_path="")
