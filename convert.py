import sys
import os
import subprocess

def install_and_import(package):
    try:
        import fitz
    except ImportError:
        print("Instalando biblioteca para converter PDF em Imagem...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "PyMuPDF"])
        import fitz
    return fitz

fitz = install_and_import('fitz')

folder = r"d:\Antigravity\Quis Historias da Bibliapara colorir"

# Mapeamento do arquivo em disco (PDF atual) -> Nome da Imagem (PNG) a ser gerada
pdf_to_img_map = {
    "Colorindo Stitch.png.pdf": "Colorindo com Stitch.png",
    "Colorindo com Ursinho Pooh.png.pdf": "Colorindo com Ursinho Pooh.png",
    "Colorindo versiculos da Bíblia.png.pdf": "Colorindo versiculos da Bíblia.png",
    "Histórias Bíblicas Antigo Testamento.png.pdf": "Histórias Bíblicas Antigo Testamento.png",
    "Histórias Bíblicas Novo Testamento.png.pdf": "Histórias Bíblicas Novo Testamento.png",
    "MEU CADERNO DE ALFABETIZAÇÃO - GRUPO MATERIAIS PEDAGÓGICOS.png.pdf": "MEU CADERNO DE ALFABETIZAÇÃO - GRUPO MATERIAIS PEDAGÓGICOS.png"
}

for pdf_file, img_name in pdf_to_img_map.items():
    pdf_path = os.path.join(folder, pdf_file)
    if os.path.exists(pdf_path):
        print(f"Extraindo capa de: {pdf_file}")
        doc = fitz.open(pdf_path)
        page = doc.load_page(0)  # primeira página
        pix = page.get_pixmap(dpi=150) # qualidade boa para web
        
        out_path = os.path.join(folder, img_name)
        pix.save(out_path)
        print(f"Salvo como: {img_name}")
        doc.close()
        
        # Renomeia o PDF de volta para o normal (tira o .png)
        correct_pdf_name = pdf_file.replace(".png.pdf", ".pdf")
        correct_pdf_path = os.path.join(folder, correct_pdf_name)
        os.rename(pdf_path, correct_pdf_path)
    else:
        print(f"Arquivo não encontrado: {pdf_file}")

print("Conversão finalizada!")
