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
            if (pageNumber in (1, 28)):
                continue
            
            print("Processando página " + str(pageNumber))
            # Obter o texto da página
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            code = page_text.encode('utf-8')
            utf8_text += code.decode('utf-8')
        
        utf8_text = utf8_text.replace('Concurso Vestibular F UVEST 2023 – PROVA K', '')
        utf8_text = utf8_text.replace('Concurso Vestibular FUVEST 2023 – PROVA K', '')

        # Procurar por questões
        pattern = re.compile(r'\n\s*([0-9]{2})\s*\n')
        questoes = [q for q in re.split(pattern, utf8_text) if q.strip()]

        num_questao = ""
        questaoComImagem = 0
        for i, questao_texto in enumerate(questoes, start=0):

            if(i%2 == 0):
                num_questao = questao_texto
                continue
            else:
                texto_questao = questao_texto

            print("Processando questão " + num_questao)

            num_questao = num_questao.strip()

            # Separar o número da questão e o texto
            texto_questao = funcoes.trataCaractereres(texto_questao)
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
            pattern = re.compile(r'[ABCDE]\)')
            respostas = [part.strip() for part in re.split(pattern, respostas_texto) if part.strip()]
            # Separar as respostas
            questao_objeto["respostas"] = respostas

            # Extrair imagens
            #doc = fitz.open(pdf_path)
            #imagens = doc[page_num].get_images()

            # if(funcoes.ContemImage(texto_questao)):
            #     for img_index, img_info in enumerate(imagens):
            #         if(img_index == questaoComImagem):
            #             xref = img_info[0]
            #             base_image = doc.extract_image(xref)
            #             image_bytes = base_image["image"]
            #             base64_data = base64.b64encode(image_bytes).decode('utf-8')
            #             questao_objeto["anexos"].append({"imagem": f'<img src="#" alt="Anexo" id="divAnexo{img_index}"/>', "base64": 'data:image/png;base64,' + base64_data})
            #             questaoComImagem+=1
            #             break

            # Imprimir o objeto
            funcoes.save_question_info(num_questao, questao_objeto, 'C:/provas/saida/')

        print("Finished")

if __name__ == "__main__":
    # Substitua 'caminho_para_seu_arquivo.pdf' pelo caminho do seu arquivo PDF
    caminho_do_pdf = 'C:/provas/fuvest2023_primeira_fase_prova_K.pdf'
    extrair_informacoes(caminho_do_pdf)