import fitz

def pdf_to_png(pdf_path, png_path):
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)
    pix = page.get_pixmap(dpi=300)
    pix.save(png_path)
    print(f'Saved ' + png_path)

pdf_to_png('assets/images/PANORAMA+BIBLICO capa.pdf', 'assets/images/bonus-pais-capa.png')
pdf_to_png('assets/images/PANORAMA+BIBLICO.pdf', 'assets/images/bonus-pais-miolo.png')
