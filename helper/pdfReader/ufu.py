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
        first = True;
        for page_num in range(len(pdf_reader.pages)):
            pageNumber = pageNumber + 1
            if (pageNumber in (1, 2, 18, 19, 39,40)):
                continue
            
            print("Processando página " + str(pageNumber))
            # Obter o texto da página
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            code = page_text.encode('utf-8')
            utf8_text = code.decode('utf-8')
            utf8_text = utf8_text.replace("QUES TÃO", "QUESTÃO")
            utf8_text = utf8_text.replace("QUESTÃ O", "QUESTÃO")
            utf8_text = utf8_text.replace("QUESTA~O", "QUESTÃO")
            utf8_text = utf8_text.replace("QUESTÃO", "QUESTÃO")
            utf8_text = utf8_text.replace("QUEST ÃO", "QUESTÃO")

            # Procurar por questões
            questoes = [q for q in utf8_text.split("QUESTÃO ") if q.strip()]
            for i, questao_texto in enumerate(questoes, start=1):

                if(first or len(questao_texto) < 150):
                    first = False
                    continue

                if("Processo Seletivo UFU" in questao_texto):
                    continue

                # Separar o número da questão e o texto
                num_questao, texto_questao = questao_texto.split('\n', maxsplit=1)
                texto_questao = funcoes.TrataCaracteresEspeciais(texto_questao=texto_questao)

                num_questao = num_questao.replace(' ', '')
                print("Processando questão " + num_questao)

                num_questao = num_questao.strip()

                respostas_texto = texto_questao[texto_questao.rfind('A) '):]
                texto_questao = texto_questao[:texto_questao.rfind('A) ')]
                texto_questao = funcoes.TrataReferencias(texto_questao=texto_questao)
                
                texto_questao = "<b>Questão " + num_questao + "</b><br><br>" + texto_questao
                
                texto_questao = texto_questao.replace("TEXTO I", "<b>TEXTO I</b><br><br>").replace("TEXTO II", "<b>TEXTO II</b><br><br>").replace("TEXTO III", "<b>TEXTO III</b><br><br>")
                questao_objeto = {
                    "questao": texto_questao,
                    "materia": "",
                    "numeroquestao": num_questao,
                    "respostas": [],
                    "anexos": []
                }
                
                respostas_texto = respostas_texto.replace(". \n", ".\n")
                pattern = re.compile(r'[ABCD]\)')
                respostas = [part.strip() for part in re.split(pattern, respostas_texto) if part.strip()]
                # Separar as respostas
                questao_objeto["respostas"] = respostas

                # Extrair imagens
                doc = fitz.open(pdf_path)
                imagens = doc[page_num].get_images()

                for img_index, img_info in enumerate(imagens):
                    xref = img_info[0]
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    base64_data = base64.b64encode(image_bytes).decode('utf-8')
                    questao_objeto["anexos"].append({"imagem": f"<imagem_{img_index + 1}>", "base64": base64_data})

                # Imprimir o objeto
                funcoes.save_question_info(num_questao, questao_objeto, 'C:/provas/saida/')

        print("Finished")

if __name__ == "__main__":
    # Substitua 'caminho_para_seu_arquivo.pdf' pelo caminho do seu arquivo PDF
    caminho_do_pdf = 'C:/provas/vestibular_ufu_2023.pdf'
    extrair_informacoes(caminho_do_pdf)