def adicionarContato(agenda, numContato, nomeContato, emailContato):
    contato = {"contato":nomeContato, "numero":numContato, "favorito":False, "email":emailContato}
    agenda.append(contato)
    print(f"O contato de {nomeContato} foi salvo com sucesso !!")
    return

def verContatos(agenda):
    print("\n ... Agenda ... ")
    if not agenda:
        print("A agenda está vazia !")
        return
    
    for indice, contato in enumerate(agenda, start=1):
        status = "★" if contato["favorito"] else ""
        nomeContato = contato["contato"]
        numContato = contato["numero"]
        emailContato = contato["email"]
        print(f"{status} {indice}: Nome: {nomeContato}  Número:{numContato}  Email: {emailContato} ")

def editarContato(agenda,chave,indice, novoNome,novoNumContato,novoEmailContato):
    indiceAjustado = int(indice)-1
    if indiceAjustado >= 0 and indiceAjustado < len(agenda):
        if chave == "1":
            agenda[indiceAjustado]["contato"] = novoNome
        elif chave == "2":
            agenda[indiceAjustado]["numero"] = novoNumContato
        elif chave == "3":
            agenda[indiceAjustado]["email"] = novoEmailContato
    print(f"O contato número {indice} foi editado com sucesso !")
    return

def deletarContato(agenda, indice):
    indiceAjustado = int(indice)-1
    agenda.pop(indiceAjustado)
    print("O contato foi excluido com sucesso!")
    return

def favoritarContato(agenda, indice):
    indiceAjustado = int(indice)-1
    if agenda[indiceAjustado]["favorito"] == False:
        agenda[indiceAjustado]["favorito"] = True
    elif agenda[indiceAjustado]["favorito"] == True:
        agenda[indiceAjustado]["favorito"] = False
    print("O contato foi favoritado com sucesso!")
    return

def verContatosFavoritos(agenda):
    print("\n ... Lista Favoritos ... ")
    if not agenda:
        print("A agenda está vazia")
    
    for indice, contato in enumerate(agenda, start=1):
        status = "★" if contato["favorito"] else ""
        if contato["favorito"] == True:
            print(f"{status} {indice}: Nome: {nomeContato}  Número:{numContato}  Email: {emailContato} ")
    return

agenda =  []

while True:
    print("\n ... Sua Agenda ... \n")
    print("1. Adicionar um novo contato")
    print("2. Ver agenda de contatos")
    print("3. Editar um contato existente")
    print("4. Deletar contato existente")
    print("5. Favorita e desfavoritar um contato")
    print("6. Ver Lista de favoritos")
    print("7. Sair da Agenda")

    escolha = input("\nEscolha uma opção: ")

    if escolha == "1":
        numContato = input("\nQual o número do novo contato? ")
        nomeContato = input("Qual o nome do novo contato? ")
        emailContato = input("Qual o email do contato?")
        adicionarContato(agenda,numContato,nomeContato, emailContato)

    elif escolha == "2":
        verContatos(agenda)

    elif escolha == "3":
        verContatos(agenda)
        indice = input("Qual o contato que será editado? ")
        chave = input("Qual informação será editada? \n 1 - Para nome \n 2- Para número \n 3- Para email \n")
        
        if chave == "1":
            novoNome = input("Qual será o novo nome do contato? ")
            novoNumContato = agenda[int(indice)-1]["numero"]
            novoEmailContato = agenda[int(indice)-1]["email"]
            editarContato(agenda,chave,indice,novoNome, novoNumContato, novoEmailContato)
        
        elif chave == "2":
            novoNome = agenda[int(indice)-1]["contato"]
            novoNumContato = input("Qual é o novo número do contato? ")
            novoEmailContato = agenda[int(indice)-1]["email"]
            editarContato(agenda,chave,indice,novoNome, novoNumContato, novoEmailContato)
        
        elif chave == "3":
            novoNome = agenda[int(indice)-1]["contato"]
            novoNumContato = agenda[int(indice)-1]["numero"]
            novoEmailContato = input("Qual é o novo email do contato? ")
            editarContato(agenda,chave,indice,novoNome, novoNumContato, novoEmailContato)

    elif escolha == "4":
        verContatos(agenda)
        indice = input("Qual o contato que será excluido? ")
        deletarContato(agenda, indice)

    elif escolha == "5":
        verContatos(agenda)
        indice = input("Qual o contato que será Favoritado? ")
        favoritarContato(agenda, indice)
    
    elif escolha == "6":
        verContatosFavoritos(agenda)

    elif escolha == "7":
        break
print("Agenda encerrada !!")