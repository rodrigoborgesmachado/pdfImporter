import PyPDF2
import fitz
import base64
import os
import json

def save_question_info(question_number, question_data, output_directory):
    # Create a directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Create a filename for the question
    filename = os.path.join(output_directory, f"question_{question_number}.json")

    # Save the question data to a JSON file
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(question_data, json_file, indent=2, ensure_ascii=False)

def extrair_informacoes(pdf_path):
    # Abrir o arquivo PDF
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        utf8_text = ""
        pageNumber = 0
        first = True;
        materia = "";
        for page_num in range(len(pdf_reader.pages)):
            pageNumber = pageNumber + 1
            if (pageNumber == 1):
                continue
            print("Processando página " + str(pageNumber))

            # Obter o texto da página
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            code = page_text.encode('utf-8')
            utf8_text = code.decode('utf-8')

            # Procurar por questões
            questoes = [q for q in utf8_text.split("QUESTÃO ") if q.strip()]
            for i, questao_texto in enumerate(questoes, start=1):

                if(first):
                    if(" -" in questao_texto):
                        materia=questao_texto[questao_texto.index(" –"):questao_texto.index("Questões de")].replace(" –", "").replace("\n", "")
                    if("Questões de " in questao_texto):
                        materia=questao_texto[questao_texto.index("CIÊNCIAS"):questao_texto.index("Questões de")].replace("\n", "")
                    first = False
                    continue
                # Separar o número da questão e o texto
                num_questao, texto_questao = questao_texto.split(maxsplit=1)
                print("Processando questão " + num_questao)

                num_questao = num_questao.strip()

                if('\nA' not in texto_questao):
                    if("Questões de" in texto_questao):
                        if(" -" in questao_texto):
                            materia=questao_texto[questao_texto.index(" –"):questao_texto.index("Questões de")].replace(" –", "").replace("\n", "")
                        if("Questões de " in questao_texto):
                            materia=questao_texto[questao_texto.index("MATEMÁTICA"):questao_texto.index("Questões de")].replace("\n", "")
                    continue

                respostas_texto = texto_questao[texto_questao.rfind('\nA '):]
                texto_questao = texto_questao[:texto_questao.rfind('\nA ')]
                texto_questao = texto_questao.replace(" .\n", ".<br>")
                texto_questao = texto_questao.replace(".\n", ".<br>")
                texto_questao = texto_questao.replace("\t", " ")
                texto_questao = texto_questao.replace("\n", " ")
                texto_questao = "<b>Questão " + num_questao + "</b><br><br>" + texto_questao

                if("Disponível em:" in texto_questao):
                    indexAt = texto_questao.index("Disponível em:")
                    found = False
                    text = ''
                    while(texto_questao[indexAt] != '<' and not found):
                        if(texto_questao[indexAt] == '>' or found):
                            found = True
                            text+= texto_questao[indexAt]
                        indexAt-=1
                        if(indexAt == 0):
                            break
                    indexAt+=2
                    indexEnd = texto_questao.index("Disponível em:")
                    found = False
                    text = ''
                    while(texto_questao[indexEnd] != '>' and not found):
                        if(texto_questao[indexEnd] == '<' or found):
                            found = True
                            text+= texto_questao[indexEnd]
                        indexEnd+=1
                        if(indexEnd == len(texto_questao)):
                            break
                    indexEnd-=1
                    
                    texto_questao = texto_questao[:indexAt] + '<sub>' + texto_questao[indexAt:indexEnd] + '</sub><br>' + texto_questao[indexEnd:]
                
                if("(adaptado)" in texto_questao):
                    indexAt = texto_questao.index("(adaptado)")
                    found = False
                    text = ''
                    while(texto_questao[indexAt] != '<' and not found):
                        if(texto_questao[indexAt] == '>' or found):
                            found = True
                            text+= texto_questao[indexAt]
                        indexAt-=1
                        if(indexAt == 0):
                            break
                    indexAt+=2
                    indexEnd = texto_questao.index("(adaptado)")
                    found = False
                    text = ''
                    while(texto_questao[indexEnd] != '>' and not found):
                        if(texto_questao[indexEnd] == '<' or found):
                            found = True
                            text+= texto_questao[indexEnd]
                        indexEnd+=1
                        if(indexEnd == len(texto_questao)):
                            break
                    indexEnd-=1
                    
                    texto_questao = texto_questao[:indexAt] + '<sub>' + texto_questao[indexAt:indexEnd] + '</sub><br>' + texto_questao[indexEnd:]
                if("(fragmento)" in texto_questao):
                    indexAt = texto_questao.index("(fragmento)")
                    found = False
                    text = ''
                    while(texto_questao[indexAt] != '<' and not found):
                        if(texto_questao[indexAt] == '>' or found):
                            found = True
                            text+= texto_questao[indexAt]
                        indexAt-=1
                        if(indexAt == 0):
                            break
                    indexAt+=2
                    indexEnd = texto_questao.index("(fragmento)")
                    found = False
                    text = ''
                    while(texto_questao[indexEnd] != '>' and not found):
                        if(texto_questao[indexEnd] == '<' or found):
                            found = True
                            text+= texto_questao[indexEnd]
                        indexEnd+=1
                        if(indexEnd == len(texto_questao)):
                            break
                    indexEnd-=1
                    
                    texto_questao = texto_questao[:indexAt] + '<sub>' + texto_questao[indexAt:indexEnd] + '</sub><br>' + texto_questao[indexEnd:]
                
                texto_questao = texto_questao.replace("TEXTO I", "<b>TEXTO I</b><br><br>").replace("TEXTO II", "<b>TEXTO II</b><br><br>").replace("TEXTO III", "<b>TEXTO III</b><br><br>")
                questao_objeto = {
                    "questao": texto_questao,
                    "materia": materia,
                    "numeroquestao": num_questao,
                    "respostas": [],
                    "anexos": []
                }
                
                respostas_texto = respostas_texto.replace(". \n", ".\n")
                # Separar as respostas
                respostas = [r.strip() for r in respostas_texto.split("\n") if r.strip()]
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
                save_question_info(num_questao, questao_objeto, 'C:/provas/saida/')

        print("Finished")

if __name__ == "__main__":
    # Substitua 'caminho_para_seu_arquivo.pdf' pelo caminho do seu arquivo PDF
    caminho_do_pdf = 'C:/provas/2023_PV_impresso_D2_CD7.pdf'
    extrair_informacoes(caminho_do_pdf)