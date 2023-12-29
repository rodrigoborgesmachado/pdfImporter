import PyPDF2
import fitz
import base64
import os
import json
import funcoes
import re

def extrair_informacoes(pdf_path):
    # Abrir o arquivo PDF
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        utf8_text = ""
        pageNumber = 0
        first = True
        for page_num in range(len(pdf_reader.pages)):
            pageNumber = pageNumber + 1
            if (pageNumber in (1, 19, 20)):
                continue
            
            print("Processando página " + str(pageNumber))
            # Obter o texto da página
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            code = page_text.encode('utf-8')
            utf8_text = code.decode('utf-8')
            utf8_text = utf8_text.replace("pcimarkpci MDAwMDowMDAwOjAwMDA6MDAwMDowMDAwOmZmZmY6Yzg5Njo0ZjFh:VHVlLCAyMCBTZXAgMjAyMiAwODo0ODo1MiAtMDMwMA==\nwww.pciconcursos.com.br\n637_BASE _NS_ 7/3/2022 12:22:55  \nExecução: Fundatec  \nNÍVEL SUPERIOR  LÍNGUA PORTUGUESA", "")
            utf8_text = utf8_text.replace("pcimarkpci MDAwMDowMDAwOjAwMDA6MDAwMDowMDAwOmZmZmY6Yzg5Njo0ZjFh:VHVlLCAyMCBTZXAgMjAyMiAwODo0ODo1MiAtMDMwMA==\nwww.pciconcursos.com.br\n637_BASE _NS_ 7/3/2022 12:22:55  \nExecução: Fundatec  \nNÍVEL SUPERIOR  ", "")

            # Procurar por questões
            questoes = [q for q in utf8_text.split("QUESTÃO ") if q.strip()]
            for i, questao_texto in enumerate(questoes, start=1):

                questao_texto = questao_texto.replace("2 1", "21")
                questao_texto = questao_texto.replace("2 2", "22")
                questao_texto = questao_texto.replace("2 3", "23")
                questao_texto = questao_texto.replace("2 4", "24")
                questao_texto = questao_texto.replace("2 5", "25")
                num_questao, texto_questao = questao_texto.split(maxsplit=1)
                # Separar o número da questão e o texto
                texto_questao = funcoes.TrataCaracteresEspeciais(texto_questao=texto_questao)

                print("Processando questão " + str(num_questao))

                respostas_texto = texto_questao[texto_questao.rfind('A) '):]
                texto_questao = texto_questao[:texto_questao.rfind('A) ')]
                texto_questao = funcoes.TrataReferencias(texto_questao=texto_questao)
                
                texto_questao = "<b>Questão " + str(num_questao) + "</b><br><br>" + texto_questao
                
                texto_questao = texto_questao.replace("TEXTO I", "<b>TEXTO I</b><br><br>").replace("TEXTO II", "<b>TEXTO II</b><br><br>").replace("TEXTO III", "<b>TEXTO III</b><br><br>")
                questao_objeto = {
                    "questao": texto_questao,
                    "materia": "",
                    "numeroquestao": num_questao,
                    "respostas": [],
                    "anexos": []
                }
                
                respostas_texto = respostas_texto.replace(". \n", ".\n")
                pattern = re.compile(r'[ABCDE]\)')
                respostas = [part.strip() for part in re.split(pattern, respostas_texto) if part.strip()]
                # Separar as respostas
                questao_objeto["respostas"] = respostas

                # Imprimir o objeto
                funcoes.save_question_info(num_questao, questao_objeto, 'C:/provas/saida/')

        print("Finished")

if __name__ == "__main__":
    # Substitua 'caminho_para_seu_arquivo.pdf' pelo caminho do seu arquivo PDF
    caminho_do_pdf = 'C:/provas/Analista Ambiental - Biologia - SPGGRS_prova.pdf'
    extrair_informacoes(caminho_do_pdf)