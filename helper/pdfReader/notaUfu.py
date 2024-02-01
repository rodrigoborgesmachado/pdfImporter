import PyPDF2
import funcoes
import re

def extrair_informacoes(pdf_path):
    # Abrir o arquivo PDF
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        utf8_text = ""
        pageNumber = 0
        materias = ['\nRedação', '\nCiências da\nNatureza e suas\nTecnologias', '\nCiências Humanas\ne suas\nTecnologias', '\nLinguagens,\nCódigos e suas\nTecnologias', '\nMatemática e suas\nTecnologias']
        notas = []
        for page_num in range(len(pdf_reader.pages)):
            pageNumber = pageNumber + 1
            if (pageNumber == 1):
                continue
            else: 
                if (pageNumber >= 96):
                    continue
            
            print("Processando página " + str(pageNumber))
            # Obter o texto da página
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            code = page_text.encode('utf-8')
            utf8_text = code.decode('utf-8')
            utf8_text = utf8_text.strip()
            
            indexStart = utf8_text.find('34 3239-4893\n') + len('34 3239-4893\n')
            curso = utf8_text[indexStart:]
            indexEnd = curso.find('\n')
            curso = curso[:indexEnd]

            indexStart = utf8_text.find('Grau:\n') + len('Grau:\n')
            indexEnd = utf8_text.find('Turno:\n')
            turno = utf8_text[indexStart:indexEnd]

            for materia in materias:
                indexStart = utf8_text.find(materia) + len(materia)
                indexEnd = indexStart + 5
                peso = utf8_text[indexStart:indexEnd]

                nota = {
                    "curso": funcoes.trataCaractereres(curso).strip(),
                    "turno": funcoes.trataCaractereres(turno).strip(),
                    "materia": funcoes.trataCaractereres(materia).strip(),
                    "peso": funcoes.trataCaractereres(peso).strip()
                }
                notas.append(nota)

        funcoes.save_file('C:/Users/rodri/OneDrive/Área de Trabalho/SISU/termos adesão ufu/saida/', 'out.json', notas)
        print("Finished")

# Substitua 'caminho_para_seu_arquivo.pdf' pelo caminho do seu arquivo PDF
caminho_do_pdf = 'C:/Users/rodri/OneDrive/Área de Trabalho/SISU/termos adesão ufu/Termo de Adesão 1ª edição de 2024.pdf'
extrair_informacoes(caminho_do_pdf)