# 📄 Azure Function - Gerador de PDF via Requisição HTTP
Este projeto é uma Azure Function simples que:

- Recebe uma requisição HTTP,

- Gera um arquivo PDF dinamicamente,

- Retorna o PDF como download para o usuário.

- A função foi pensada para ser utilizada no Consumption Plan do Azure, aproveitando a escalabilidade automática e o custo baixo.

## 🚀 Tecnologias Utilizadas
Azure Functions Python: Documentação Oficial

- ReportLab: Documentação Oficial (biblioteca para gerar PDFs)

- Python 3.10+: Documentação Oficial

## 📦 Como Funciona
Quando uma requisição HTTP é recebida, a função:

- Cria um PDF diretamente na memória usando BytesIO e a biblioteca ReportLab.

- Escreve uma mensagem personalizada no PDF.

- Retorna o PDF gerado como resposta HTTP, permitindo que o usuário faça o download diretamente no navegador.
