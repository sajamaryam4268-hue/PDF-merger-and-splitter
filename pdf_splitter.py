from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("sample.pdf")

for page_num in range(len(reader.pages)):
    writer = PdfWriter()
    writer.add_page(reader.pages[page_num])

    output_file = f"page_{page_num + 1}.pdf"

    with open(output_file, "wb") as output:
        writer.write(output)

print("PDF split successfully!")
