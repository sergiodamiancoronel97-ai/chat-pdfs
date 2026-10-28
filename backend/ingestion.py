from pypdf import PdfReader
def extract_pages(path):
    reader = PdfReader(path)
    pages = []
    for num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        pages.append((num, text))

    return pages      
def chunk_text(text, size=800, overlap=100):
    chunks = []
    for start in range(0, len(text), size - overlap):
        chunk = text[start:start + size]
        chunks.append(chunk)
    return chunks
if __name__ == "__main__":
    for num, text in extract_pages("samples/pdf_prueba_texto_seleccionable.pdf"):
        print(num, text[:100]) 

if __name__ == "__main__":
    chunks = chunk_text("a" * 2000)
    print(len(chunks))
    for c in chunks:
        print(len(c))

