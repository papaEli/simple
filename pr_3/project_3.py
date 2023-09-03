from PyPDF2 import PdfWriter, PdfReader

pdfwriter = PdfWriter()

#Можете добавить сюда любой файл pdf для чтения
pdf_reader = PdfReader('Интересное чтиво.pdf')


for page in range(len(pdf_reader.pages)):
    pdfwriter.add_page(pdf_reader.pages[page])

# как например, для большей защищенности, можете установить библиотеку getpass, чтобы пароль не был виден никому
password = input('Введите пароль: ')
pdfwriter.encrypt(password)

with open('protected.pdf', 'wb') as file:
    pdfwriter.write(file)




