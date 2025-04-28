import logging
import azure.functions as func
from reportlab.pdfgen import canvas
from io import BytesIO

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('HTTP trigger function received a request to generate PDF.')

    # Adiciona os cabeçalhos CORS
    headers = {
        'Access-Control-Allow-Origin': '*',  # Permite qualquer origem, ajuste conforme necessário
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    }

    # Se for uma requisição OPTIONS, a Azure Function responde sem processamento
    if req.method == "OPTIONS":
        return func.HttpResponse(
            "",  # Corpo vazio para requisição OPTIONS
            status_code=200,
            headers=headers
        )

    # Criar o PDF em memória
    pdf_buffer = BytesIO()
    p = canvas.Canvas(pdf_buffer)
    p.drawString(100, 750, "Olá! Este é um PDF gerado por uma Azure Function.")
    p.showPage()
    p.save()

    pdf_buffer.seek(0)

    # Retorna o PDF gerado com os cabeçalhos CORS
    return func.HttpResponse(
        pdf_buffer.read(),
        mimetype="application/pdf",
        headers={
            "Content-Disposition": "attachment; filename=meu_pdf_gerado.pdf"
        } | headers  # Combina os cabeçalhos CORS com a resposta
    )
