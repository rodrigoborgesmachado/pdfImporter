import os
import json

def replaceAll(str, list):
    temp = str
    for i, palavra in enumerate(list):
        temp = temp.replace(palavra, "")
    return temp

def getNumeroProva(numero, useTwo = False):
    retorno = ''
    if(numero < 10 and useTwo):
        retorno = '0' + str(numero)
    else:
        retorno = str(numero)
    return retorno

def trataCaractereres(texto):
    blackList = [
	{"old":"√", "new":"&#8730;"},
    {"old":"𝑝", "new":"<i>p</i>"},
    {"old":"𝑥", "new":"<i>x</i>"},
    {"old":"𝑞", "new":"<i>q</i>"},
    {"old":"𝑔", "new":"<i>g</i>"},
    {"old":"𝑦", "new":"<i>y</i>"},
    {"old":"", "new":"<i>•</i>"},
    {"old":"∧", "new":"&and;"},
    {"old":"∨", "new":"&or;"},
    {"old":"𝑒", "new":"e"},
    {"old":"→", "new":"&#8594;"},
    {"old":"⇄", "new":"&#8644;"},
    {"old":" .\n", "new":".<br>"},
    {"old":".\n", "new":".<br>"},
    {"old":"(  )", "new":"<br>(  ) "},
    {"old":"\t", "new":" "},
    {"old":"\n", "new":" "},
    {"old":"<http", "new":"http"},
    {"old":".html>", "new":".html"},
    {"old":".uk>", "new":".uk"},
    {"old":".com>", "new":".com"},
    {"old":".htm>", "new":".htm"},
    {"old":".gov>", "new":".gov"},
    {"old":"< http", "new":"http"},
    {"old":".html >", "new":".html"},
    {"old":".uk >", "new":".uk"},
    {"old":".com >", "new":".com"},
    {"old":".htm >", "new":".htm"},
    {"old":".gov >", "new":".gov"},
    {"old":"ζ", "new":"&#950;"},
    {"old":"η", "new":"&#951;"},
    {"old":"θ", "new":"&#952;"},
    {"old":"ι", "new":"&#953;"},
    {"old":"κ", "new":"&#954;"},
    {"old":"λ", "new":"&#955;"},
    {"old":"μ", "new":"&#956;"},
    {"old":"ν", "new":"&#957;"},
    {"old":"ξ", "new":"&#958;"},
    {"old":"ο", "new":"&#959;"},
    {"old":"π", "new":"&#960;"},
    {"old":"σ", "new":"&#963;"},
    {"old":"τ", "new":"&#964;"},
    {"old":"υ", "new":"&#965;"},
    {"old":"φ", "new":"&#966;"},
    {"old":"χ", "new":"&#967;"},
    {"old":"ψ", "new":"&#968;"},
    {"old":"ω", "new":"&#969;"},
    {"old":"ϑ", "new":"&#977;"},
    {"old":"ϒ", "new":"&#978;"},
    {"old":"ϖ", "new":"&#982;"},
    {"old":"𝑛", "new":"<i>n</i>"},
    {"old":"(A)", "new":"A)"},
    {"old":"(B)", "new":"B)"},
    {"old":"(C)", "new":"C)"},
    {"old":"(D)", "new":"D)"},
    {"old":"(E)", "new":"E)"},
    {"old":"( A)", "new":"A)"},
    {"old":"( B)", "new":"B)"},
    {"old":"( C)", "new":"C)"},
    {"old":"( D)", "new":"D)"},
    {"old":"( E)", "new":"E)"},
    {"old":"( A )", "new":"A)"},
    {"old":"( B )", "new":"B)"},
    {"old":"( C )", "new":"C)"},
    {"old":"( D )", "new":"D)"},
    {"old":"( E )", "new":"E)"},
    {"old":"(A )", "new":"A)"},
    {"old":"(B )", "new":"B)"},
    {"old":"(C )", "new":"C)"},
    {"old":"(D )", "new":"D)"},
    {"old":"(E )", "new":"E)"},
    {"old":"Quan to", "new":"Quanto"},
    {"old": "\xa0", "new": ""},
    {"old": "\nConcurso Público para oInstituto Estadual do Ambiente –INEA ‐RJ FGV ‐Projetos\n\nNível Superior –Advogado  Tipo 1–Cor Branca", "new": ""},
    {"old": "pcimarkpci", "new": ""},
    {"old": "MDAwMDowMDAwOjAwMDA6MDAwMDowMDAwOmZmZmY6YjM2ODo5ZGI2", "new": ""},
    {"old": ":RnJpLCAyOSBEZWMgMjAyMyAxNzo0Mjo1NyAtMDMwMA", "new": ""},
    {"old": "MjgwNDoxZTY4OmMyMTE6YWQxMjoyMGFkOjhiMzM6MDk4YTplZTAz:", "new": ""},
    {"old": "RnJpLCAyOSBEZWMgMjAyMyAxNzo0MjozMiAtMDMwMA", "new": ""},
    {"old": "==\nwww.pciconcursos.com.br", "new": ""},
    {"old": "Concurso Público para o Instituto Estadual do Ambiente – INEA‐RJ", "new": ""},
    {"old": "FGV ‐ Projetos", "new": ""},
    {"old": "Tipo 1 – Cor Branca", "new": ""},
    {"old": "\nSECRETARIA DE ESTADO DE FAZENDA DA BAHIA - SEFAZ -BA FGV \n", "new": ""},
    {"old": "\nAgente de  Tributos Estaduais (Administração e Finanças)", "new": ""},
    {"old": "\uf020", "new": ""},
    {"old": "Tipo  Branca", "new": ""},
    {"old": "Página 2", "new": ""},
    {"old": "Página 3", "new": ""},
    {"old": "Página 4", "new": ""},
    {"old": "Página 5", "new": ""},
    {"old": "Página 6", "new": ""},
    {"old": "Página 7", "new": ""},
    {"old": "Página 8", "new": ""},
    {"old": "Página 9", "new": ""},
    {"old": "Página 10", "new": ""},
    {"old": "Página 11", "new": ""},
    {"old": "Página 12", "new": ""},
    {"old": "Página 13", "new": ""},
    {"old": "Página 14", "new": ""},
    {"old": "\n Conhecimentos Gerais", "new": ""},
    {"old": "\nLíngua Portuguesa", "new": ""},
    {"old": "\n Direito Constitucional", "new": ""},
    {"old": "       –      ", "new": ""},
    {"old": "–    ", "new": ""},
    {"old": "–  ", "new": ""},
    {"old": "Língua Portuguesa", "new": ""},
    {"old": "Conhecimentos Gerais", "new": ""},
    {"old": "Legislação Institucional", "new": ""},
    {"old": "Direito Constitucional", "new": ""},
    {"old": "Direito Civil e Processual Civil", "new": ""},
    {"old": "Direito Ambiental", "new": ""},
    {"old": "oArt.", "new": " o Art."},
    {"old": "oDecreto ", "new":"o Decreto "},
    {"old": "aafirmativa ", "new": "a afirmativa"},
    {"old": "eque ", "new": "e que"},
    {"old": "aplicando ‐lhe", "new": "aplicando‐lhe"},
    {"old": "oé", "new": "o é"},
    {"old": "oseu", "new": "o seu"},
    {"old": "odireito", "new": "o direito"},
    {"old": "Amulta", "new": "A multa"},
    {"old": "amulta", "new": "a multa"},
    {"old": "aEmpresa", "new": "a Empresa"},
    {"old": "Éoprincípio", "new": "É o princípio"},
    {"old": "aseguir", "new": "A seguir"},
    {"old": "eboa", "new": "e boa"},
    {"old": "féobjetiva", "new": "fé objetiva"},
    {"old": "aAdministração", "new": "a Administração"},
    {"old": "oadministrado", "new": "o administrado"},
    {"old": "évedado", "new": "é vedado"},
    {"old": "OJuiz", "new": "O Juiz"},
    {"old": "oJuiz", "new": "o Juiz"},
    {"old": "oproprietário", "new": "o proprietário"},
    {"old": "àexceção", "new": "à exceção"},
    {"old": "aafirmativa", "new": "a afirmativa"},
    {"old": "Aposse", "new": "A posse"},
    {"old": "aposse", "new": "a posse"},
	]

    for i, palavra in enumerate(blackList):
        palavraOld = palavra["old"]
        palavraNew = palavra["new"]
        texto = texto.replace(palavraOld, palavraNew)
    return texto

def TrataReferencias(texto_questao):
    listaPalavras = ["Disponível em", "disponível em", "(adaptado)", "(Adaptado)", "(Fragmento)", "(fragmento)", "Acesso em", "acesso em", "p.", "P.", "\uf04a Tipo 1 – Cor BRANCA", "rInstituto Brasileiro de Geografia e Estatística<br><br>FGV  Projetos<br><br>  Agente Censitário de Informática - ACI", "www.pciconcursos.com.brInstituto Brasileiro de Geografia e Estatística<br><br>FGV  Projetos<br><br>", "Instituto Brasileiro de Geografia e Estatística<br><br>FGV  Projetos<br><br>  Agente Censitário de Informática - ACI \uf04a Tipo 1 – Cor BRANCA  –", "www.pciconcursos.com.brPrefeitura do Município de Cuiabá - Secretaria Municipal de Saúde<br><br>FGV – Projetos<br><br>  Agente de Saúde - Técnico de Laboratório<br><br>Tipo 1 – Cor BRANCA", "Legislação Específica", "www.pciconcursos.com.brPrefeitura do Município de Cuiabá - Secretaria Municipal de Saúde<br><br>FGV – Projetos<br><br>  Agente de Saúde - Técnico de Laboratório<br><br>Tipo 1 – Cor BRANCA", "www.pciconcursos.com.br RnJpLCAyOSBEZWMgMjAyMyAxNzo0NDowOCAtMDMwMA== www.pciconcursos.com.br Instituto Brasileiro de Geografia e Estatística<br><br>FGV  Projetos<br><br>  Analista - Análise de Sistemas - Desenvolvimento de Aplicações - WEB Mobile   Tipo 1 – Cor BRANCA  – ", "Conhecimentos Específicos", "RnJpLCAyOSBEZWMgMjAyMyAxNzo0NDo0NyAtMDMwMA== www.pciconcursos.com.br Concurso Público FUNSAUDE-E02 2021  FGV Conhecimento<br><br> E2NS07 Analista de  Tecnologia da Informação  Ε1Τ1 Tipo 1 – Cor BRANCA  – <br><br>", "<br><br><br><br>Atualidades", "RnJpLCAyOSBEZWMgMjAyMyAxNzo0NDo0NyAtMDMwMA== www.pciconcursos.com.br Concurso Público FUNSAUDE-E02 2021  FGV Conhecimento<br><br> E2NS07 Analista de  Tecnologia da Informação  Ε1Τ1 Tipo 1 – Cor BRANCA  – <br><br>Legislação", "RnJpLCAyOSBEZWMgMjAyMyAxNzo0NDo0NyAtMDMwMA== www.pciconcursos.com.br Concurso Público FUNSAUDE-E02 2021  FGV Conhecimento<br><br> E2NS07 Analista de  Tecnologia da Informação  Ε1Τ1 Tipo 1 – Cor BRANCA  – <br><br> Conhecimento Específico", "<br><br>Atenção: nas próximas cinco questões, considere a d efinição e  as instâncias das tabelas de bancos de dados CLUBE e JOGO  exibidas a seguir.<br><br> nome<br><br>Barcelona  Boca Juniors  The Strongest<br><br> JOGO<br><br><br><br>mandante visitante golsM golsV  Barcelona Boca Juniors 1 0  Barcelona The Strongest NULL NULL  Boca Juniors Barcelona 0 0  Boca Juniors The Strongest 3 0  The Strongest Barcelona 2 0  The Strongest Boca Juniors 2 0<br><br> Cada clube deve jogar quatro vezes, duas como manda nte e duas  como visitante.<br><br>As colunas golsM  e golsV  registram o número de gols dos times  mandantes e visitantes, respectivamente, em cada jo go. Ambas  são nulas enquanto o jogo não for realizado.<br><br>", "RnJpLCAyOSBEZWMgMjAyMyAxNzo0NDo0NyAtMDMwMA== www.pciconcursos.com.br Concurso Público FUNSAUDE-E02 2021  FGV Conhecimento</sub><br><br><br> E2NS07 Analista de  Tecnologia da Informação  Ε1Τ1 Tipo 1 – Cor BRANCA  – <br><br>"]

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

def save_file(output_directory, fileName, data):
    # Create a directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Create a filename for the question
    fileName = os.path.join(output_directory, fileName)

    # Save the question data to a JSON file
    with open(fileName, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2, ensure_ascii=False)

def is_number(s):
    return s.isdigit()