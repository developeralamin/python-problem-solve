from PyPDF2 import PdfMerger

AllPdf = ['Final_Exam.pdf','Web_Tech.pdf']

MerGer = PdfMerger()

for NewPdf in AllPdf:
    MerGer.append(NewPdf)

MerGer.write("alamin.pdf")
MerGer.close()