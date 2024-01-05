import PyPDF2
import funcoes
import re

def extrair_informacoes(pdf_path):
    # Abrir o arquivo PDF
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        utf8_text = ""
        pageNumber = 0
        num_questao = 1
        allText = ''
        for page_num in range(len(pdf_reader.pages)):
            pageNumber = pageNumber + 1
            if (pageNumber in (1, 2, 15, 16)):
                continue
            
            print("Processando página " + str(pageNumber))
            # Obter o texto da página
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            code = page_text.encode('utf-8')
            utf8_text = code.decode('utf-8')
            utf8_text = utf8_text.strip()

            if(pageNumber == 3):
                utf8_text = utf8_text[utf8_text.rfind("mesmos”."):]

            allText += utf8_text
        allText = funcoes.trataCaractereres(allText)
        allText = allText.replace('.  ', '.\n')

        my_list = list(range(1, 71))

        for num_questao in my_list:
            numeroquestao = funcoes.getNumeroProva(num_questao, True)
            numeroquestaoNext = funcoes.getNumeroProva(num_questao+1, True)
            indexStart = allText.find(numeroquestao + '  ')
            indexEnd = allText.find(numeroquestaoNext + '  ')

            if(indexStart < 0):
                print('Questão ' + str(num_questao) + ' não encontrado')
                continue
            if(indexEnd < 0):
                texto_questao = allText[indexStart:]
            else:
                texto_questao = allText[indexStart:indexEnd]
                allText = allText[indexEnd:]

            print("Processando questão " + str(numeroquestao))

            respostas_texto = texto_questao[texto_questao.rfind('A) '):]
            texto_questao = texto_questao[:texto_questao.rfind('A) ')]
            texto_questao = funcoes.TrataReferencias(texto_questao=texto_questao)
            
            texto_questao = "<b>Questão " + str(numeroquestao) + "</b><br><br>" + texto_questao
            
            texto_questao = texto_questao.replace("TEXTO I", "<b>TEXTO I</b><br><br>").replace("TEXTO II", "<b>TEXTO II</b><br><br>").replace("TEXTO III", "<b>TEXTO III</b><br><br>")
            questao_objeto = {
                "questao": texto_questao,
                "materia": "",
                "numeroquestao": numeroquestao,
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
    caminho_do_pdf = 'C:/provas/advogado_tipo_01.pdf'
    extrair_informacoes(caminho_do_pdf)