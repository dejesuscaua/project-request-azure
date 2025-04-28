import logging
import azure.functions as func
from reportlab.pdfgen import canvas
from io import BytesIO

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Requisição HTTP recebida para geração de PDF.')

    # Inicializa um buffer de bytes para armazenar o PDF em memória
    pdf_buffer = BytesIO()
    pdf = canvas.Canvas(pdf_buffer)

    # Escreve o conteúdo no PDF
    pdf.drawString(100, 750, "Olá! Este é um PDF gerado por uma Azure Function.")
    pdf.showPage()
    pdf.save()

    # Retorna o ponteiro para o início do buffer
    pdf_buffer.seek(0)

    # Retorna o PDF como resposta HTTP
    return func.HttpResponse(
        pdf_buffer.read(),
        mimetype="application/pdf",
        headers={
            "Content-Disposition": "attachment; filename=meu_pdf_gerado.pdf"
        }
    )
