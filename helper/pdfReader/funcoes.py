def TrataCaracteresEspeciais(texto_questao):
    texto_questao = texto_questao.replace("𝑝", "<i>p</i>")
    texto_questao = texto_questao.replace("𝑥", "<i>x</i>")
    texto_questao = texto_questao.replace("𝑞", "<i>q</i>")
    texto_questao = texto_questao.replace("𝑔", "<i>g</i>")
    texto_questao = texto_questao.replace("𝑦", "<i>y</i>")
    texto_questao = texto_questao.replace("", "<i>•</i>")
    texto_questao = texto_questao.replace("→", "&#8594;")
    texto_questao = texto_questao.replace("⇄", "&#8644;")

    return texto_questao

def TrataReferencias(texto_questao):
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

    if("disponível em:" in texto_questao):
        indexAt = texto_questao.index("disponível em:")
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
        indexEnd = texto_questao.index("disponível em:")
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

    if("(Adaptado)" in texto_questao):
        indexAt = texto_questao.index("(Adaptado)")
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
        indexEnd = texto_questao.index("(Adaptado)")
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

    if("(Fragmento)" in texto_questao):
        indexAt = texto_questao.index("(Fragmento)")
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
        indexEnd = texto_questao.index("(Fragmento)")
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

    if("Acesso em" in texto_questao):
        indexAt = texto_questao.index("Acesso em")
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
        indexEnd = texto_questao.index("Acesso em")
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

    if("p." in texto_questao):
        indexAt = texto_questao.index("p.")
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
        indexEnd = texto_questao.index("p.")
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