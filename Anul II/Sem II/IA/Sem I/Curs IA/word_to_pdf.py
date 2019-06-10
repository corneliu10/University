import sys
import os
import comtypes.client
import re
from PyPDF2 import PdfFileMerger

def merge_files(dir, out_file):
    os.chdir(dir)
    files = os.listdir('.')

    files_sorted = sorted(files, key=lambda file: int(re.search(r'\d+', file[:-(len(file) - file.find('.'))]).group()))
    merger = PdfFileMerger()

    for pdf in files_sorted:
        if pdf.split('.')[-1] == 'pdf':
            merger.append(open(pdf, 'rb'))

    with open(out_file, 'wb') as fout:
        merger.write(fout)

def word_to_pdf(in_file, out_file):
    wdFormatPDF = 17

    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()

def convert_files(in_folder, out_folder):
    for file in os.listdir(in_folder):
        in_file = os.path.join(in_folder, file)
        out_file = os.path.join(out_folder, file + ".pdf")

        word_to_pdf(in_file, out_file)

def convert_and_merge(in_folder, out_folder, out_file = 'result.pdf'):
    convert_files(in_folder, out_folder)
    merge_files(in_folder, out_file)

in_folder = os.path.abspath(sys.argv[1])
out_folder = os.path.abspath(sys.argv[2])

convert_and_merge(in_folder, out_folder)