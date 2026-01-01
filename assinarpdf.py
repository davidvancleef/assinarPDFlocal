import sys
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO
import os

def adicionar_imagem_pdf(
    nome_pdf,
    imagem,
    x,
    y,
    largura_img,
    altura_img,
    pagina=0
):
    reader = PdfReader(nome_pdf)
    writer = PdfWriter()

    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=A4)
    c.drawImage(imagem, x, y, width=largura_img, height=altura_img, mask='auto')
    c.save()

    packet.seek(0)
    overlay_pdf = PdfReader(packet)

    for i, page in enumerate(reader.pages):
        if i == pagina:
            page.merge_page(overlay_pdf.pages[0])
        writer.add_page(page)

    nome_saida = f"{os.path.basename(nome_pdf)}"

    with open(nome_saida, "wb") as f:
        writer.write(f)

    print(f"✔ PDF gerado: {nome_saida}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Uso:")
        print("  python assinarpdf.py <pdf> <x> <y> [pagina] [largura] [altura]")
        print("Exemplo:")
        print("  python assinarpdf.py contrato.pdf 350 120")
        sys.exit(1)

    pdf = sys.argv[1]
    x = float(sys.argv[2])
    y = float(sys.argv[3])

    pagina = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    largura = float(sys.argv[5]) if len(sys.argv) > 5 else 200
    altura = float(sys.argv[6]) if len(sys.argv) > 6 else 100

    adicionar_imagem_pdf(
        nome_pdf=pdf,
        imagem="assinatura.png",
        x=x,
        y=y,
        largura_img=largura,
        altura_img=altura,
        pagina=pagina
    )
