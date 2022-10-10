import datetime
from PyPDF4 import PdfFileMerger
from pathlib import Path
import matplotlib.pyplot as plt
from utils.dataframe_utils import get_dataframe_from_file

class Pdf:

    def __init__(self, records: list[str], place_to_save: str):
        self.records = records

        self.place_to_save = place_to_save + f"pdfs/{self.__create_pdf_name()}.pdf"

    def create_pdf(self):
        for record in self.records:
            pdfs = []
            images = []
            txts = []
            name = record.split('.')
            extension = name[-1]
            if extension == 'pdf':
                pdfs.append(record)
            elif extension == 'jpg':
                images.append(record)
            elif extension == 'txt' or 'xy':
                txts.append(record)
            else:
                continue
            if len(pdfs) > 0:
                self.__merge_pdfs(pdfs)
            if len(txts) > 0:
                self.__txt_to_pdf(txts)

    def __merge_pdfs(self, pdfs: list[str]):
        try:
            pdf_merger = PdfFileMerger()
            i = 1
            for p in pdfs:
                print(p)
                pdf_merger.append(p)
                # with Path(self.place_to_save).open(mode="wb") as output_file:
                #     pdf_merger.write(output_file)
                #
            pdf_merger.write(self.place_to_save)
            pdf_merger.close()

        except NameError:
            print(NameError)

    def __txt_to_pdf(self, txts: list[str], skip_before: int = 0, skip_after: int = 0, sep: str = ' '):
        try:
            for name in txts:
                df = get_dataframe_from_file(name)
                df.plot()
                plt.savefig(f"/tmp/name_{name}.pdf", format="pdf", bbox_inches="tight")
            pdf_merger = PdfFileMerger()
            for name in txts:
                pdf_merger.append(f"/tmp/name_{name}.pdf")
            name = self.__create_pdf_name()
            with Path(self.place_to_save).open(mode="wb") as output_file:
                pdf_merger.write(output_file)
        except NameError:
            print(NameError)

    @staticmethod
    def __create_pdf_name():
        time = datetime.datetime.now()
        string_time = str(time).replace(' ', '_').replace('.', '_').replace(':', '_')
        name = 'pdf_' + string_time
        return name
