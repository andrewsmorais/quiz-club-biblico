import sys
import os
import fitz

folder = r"d:\Antigravity\Quis Historias da Bibliapara colorir"

files_to_convert = {
    "CALIGRAFIA -.pdf": "caligrafia-1.png",
    "CALIGRAFIA -2.pdf": "caligrafia-2.png"
}

for pdf_file, img_name in files_to_convert.items():
    pdf_path = os.path.join(folder, pdf_file)
    if os.path.exists(pdf_path):
        doc = fitz.open(pdf_path)
        page = doc.load_page(0)
        pix = page.get_pixmap(dpi=150)
        
        out_path = os.path.join(folder, img_name)
        pix.save(out_path)
        print(f"Salvo como: {img_name}")
        doc.close()
    else:
        print(f"Não encontrado: {pdf_file}")
