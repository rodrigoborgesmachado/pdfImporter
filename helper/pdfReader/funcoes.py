import os
import json

def TrataCaracteresEspeciais(texto_questao):
    texto_questao = texto_questao.replace("𝑝", "<i>p</i>")
    texto_questao = texto_questao.replace("𝑥", "<i>x</i>")
    texto_questao = texto_questao.replace("𝑞", "<i>q</i>")
    texto_questao = texto_questao.replace("𝑔", "<i>g</i>")
    texto_questao = texto_questao.replace("𝑦", "<i>y</i>")
    texto_questao = texto_questao.replace("", "<i>•</i>")
    texto_questao = texto_questao.replace("→", "&#8594;")
    texto_questao = texto_questao.replace("⇄", "&#8644;")
    texto_questao = texto_questao.replace(" .\n", ".<br>")
    texto_questao = texto_questao.replace(".\n", ".<br>")
    texto_questao = texto_questao.replace("(  )", "<br>(  ) ")
    texto_questao = texto_questao.replace("\t", " ")
    texto_questao = texto_questao.replace("\n", " ")
    texto_questao = texto_questao.replace("<http", "http")
    texto_questao = texto_questao.replace(".html>", ".html")
    texto_questao = texto_questao.replace(".uk>", ".uk")
    texto_questao = texto_questao.replace(".com>", ".com")
    texto_questao = texto_questao.replace(".htm>", ".htm")
    texto_questao = texto_questao.replace(".gov>", ".gov")
    texto_questao = texto_questao.replace("< http", "http")
    texto_questao = texto_questao.replace(".html >", ".html")
    texto_questao = texto_questao.replace(".uk >", ".uk")
    texto_questao = texto_questao.replace(".com >", ".com")
    texto_questao = texto_questao.replace(".htm >", ".htm")
    texto_questao = texto_questao.replace(".gov >", ".gov")
    texto_questao = texto_questao.replace("   ", "<br><br>")
    texto_questao = texto_questao.replace("(A)", "A)")
    texto_questao = texto_questao.replace("(B)", "B)")
    texto_questao = texto_questao.replace("(C)", "C)")
    texto_questao = texto_questao.replace("(D)", "D)")
    texto_questao = texto_questao.replace("(E)", "E)")
    texto_questao = texto_questao.replace("( A)", "A)")
    texto_questao = texto_questao.replace("( B)", "B)")
    texto_questao = texto_questao.replace("( C)", "C)")
    texto_questao = texto_questao.replace("( D)", "D)")
    texto_questao = texto_questao.replace("( E)", "E)")
    texto_questao = texto_questao.replace("( A )", "A)")
    texto_questao = texto_questao.replace("( B )", "B)")
    texto_questao = texto_questao.replace("( C )", "C)")
    texto_questao = texto_questao.replace("( D )", "D)")
    texto_questao = texto_questao.replace("( E )", "E)")
    texto_questao = texto_questao.replace("(A )", "A)")
    texto_questao = texto_questao.replace("(B )", "B)")
    texto_questao = texto_questao.replace("(C )", "C)")
    texto_questao = texto_questao.replace("(D )", "D)")
    texto_questao = texto_questao.replace("(E )", "E)")

    return texto_questao

def TrataReferencias(texto_questao):
    listaPalavras = ["Disponível em", "disponível em", "(adaptado)", "(Adaptado)", "(Fragmento)", "(fragmento)", "Acesso em", "acesso em", "p.", "P."]

    for palavra in listaPalavras:
        if(palavra in texto_questao):
            indexAt = texto_questao.index(palavra)
            found = False
            text = ''
            while(texto_questao[indexAt] != '<' and not found):
                if(texto_questao[indexAt] == '>' or found):
                    found = True
                    text+= texto_questao[indexAt]
                indexAt-=1
                if(indexAt <= 0):
                    break
            indexAt+=2
            indexEnd = texto_questao.index(palavra)
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

    return texto_questao

def ContemImage(texto_questao):
    contem = False
    contem |= "A figura" in texto_questao
    contem |= "A imagem" in texto_questao
    contem |= "a figura" in texto_questao
    contem |= "a imagem" in texto_questao
    contem |= "A pintura" in texto_questao
    contem |= "a pintura" in texto_questao
    contem |= "O diagrama" in texto_questao
    contem |= "o diagrama" in texto_questao
    
    return contem

def save_question_info(question_number, question_data, output_directory):
    # Create a directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Create a filename for the question
    filename = os.path.join(output_directory, f"question_{question_number}.json")

    # Save the question data to a JSON file
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(question_data, json_file, indent=2, ensure_ascii=False)

def save_gabarito_info(test, question_data, output_directory):
    # Create a directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Create a filename for the question
    filename = os.path.join(output_directory, f"gabarito_{test}.json")

    # Save the question data to a JSON file
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(question_data, json_file, indent=2, ensure_ascii=False)
