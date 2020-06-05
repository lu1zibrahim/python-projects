#!/usr/bin/python  #Permite o Python ser executado como "Standalone", sem precisar digitar o python...
# -*- coding: utf-8 -*- # utilizado para usar a codificação utf-8 (Permite acentos entre outros caracteres)

import pickle #importa o pickle para utilizar ao salvar e abrir arquivos
import os #importa as funcoes do sistema
import time #importa as funcoes de tempo


arq = 'bancodevotos.dat' # criando uma variável para evitar reescrever o arquivo binário

try: #aqui é para tentar abrir o arquivo, para pegar dados já salvos
    pkl_file = open(arq,'rb')
    db = pickle.load(pkl_file)
except: # caso o arquivo não existe, será criado
    arquivo = open(arq, 'wb')
    for i in range(1):
        pickle.dump(i, arquivo)
    db = {}
    pickle.dump(db,arquivo)
    arquivo.close()
# criada variável para evitar ficar reescrevendo
mylist = ["Verificar um Canditado","Cadastrar um Candidato","Verificar os votos","Adicionar votos","Listar todos candidatos","Sair do Sistema"]
votosopcoes = ["Listar por Candidato","Listar por Região"]
myopcoes = ["Adicionar votos","Voltar para o Menu"]
mydata = ["Código do Candidato","Nome do Candidato","Cargo do Candidato","Região do Candidato","Número de Votos","Sair do Sistema"]



def read_candidato(nome): #Criar uma função para mostrar um candidato especifico.
    try:
        a = open(nome, 'rb')
    except:
        print('Erro ao ler o arquivo')
    else:
        head_caller(mylist[0])
        qual_candidato = cod_valido('Qual código do candidato ? ')
        if not existe_registro(qualcodigo):
            print('Não existe nenhum candidato com este código, favor digite outro')
            read_candidato(arq)
        else:
            pkl_file = open(arq,'rb')
            db2 = pickle.load(pkl_file)
            print(f"O Candidato de código:{qual_candidato} é o {db2[qual_candidato]['nome']} que possui o cargo: {db2[qual_candidato]['cargo']}, da regiao: {db2[qual_candidato]['regiao']} e no momento tem {db2[qual_candidato]['num_votos']} voto(s).")
    finally:
        a.close()
        time.sleep(2)
        __main__()

def existe_registro(codigo): # criada uma função para verificar se o código já existe no arquivo
    duplicated = False
    pkl_file = open(arq,'rb')
    db = pickle.load(pkl_file)
    try:
        if codigo in db.keys():
            duplicated = True
    except AttributeError:
        return duplicated

    return duplicated	

def gravar_candidato(): # criada uma função para gravar um candidato no arquivo através do código
	
    candidato = {}
    codigo = cod_valido('Digite o código do candidato: ')

    if existe_registro(codigo): # verificr se já existe o candidato
        print('Já existe um candidato cadastrado com este código, digite outro')
        gravar_candidato()
    else:
        head_caller('Novo Cadastro')
        candidato['cod_candidato'] = codigo
        candidato['nome'] = str(input('Digite o nome candidato: '))
        candidato['cargo'] = str(input('Cargo do Candidato: '))
        candidato['regiao'] = str(input('Qual a região do Candidato? '))
        candidato['num_votos'] = cod_valido('Quantos votos o candidato tem? ')

        db[codigo] = candidato

        output = open(arq,'wb')
        pickle.dump(db,output)
        output.close()

        __main__()


def verificar_votos(): # criada uma função para verificar o número de votos
    head_caller('Votos por candidato ou região?') # verificar se quer ver os votos por candidato ou por região
    print('\n1 - Candidato')
    print('\n2 - Região\n')
    qualvoto = cod_valido('\nPor favor selecione uma opção válida:\n') 
    try:
        pkl_file = open(arq,'rb')
        db2 = pickle.load(pkl_file)
        if qualvoto == 1:       # caso seja por candidato apenas mostrar o candidato e o número de votos
            for i in db2.keys():
                print(f"O candidato {db2[i]['nome']} tem {db2[i]['num_votos']} votos")
            pkl_file.close()
            print(linha())
        elif qualvoto == 2: # caso seja por região, somar os votos de regiões iguais e depois mostrar no console.
            dbregiao = {}
            for i in db2.keys():
                if db2[i]['regiao'] in dbregiao.keys():
                    my_key = db2[i]['regiao']
                    my_new_value = db2[i]['num_votos']
                    my_old_value = dbregiao[my_key]
                    new_value = my_old_value + my_new_value
                    dbregiao[my_key] = new_value
                else:
                    my_key = db2[i]['regiao']
                    my_value = db2[i]['num_votos']
                    dbregiao[my_key] = my_value
            for key,value in dbregiao.items():
                print(f"A Regiao {key} tem {value} votos")
            pkl_file.close()
            print(linha())
        else:
            print('Favor digitar um código válido')
            verificar_votos()
    except:
        print('Nenhum candidato encontrado, favor adicionar candidatos para continuar')
        __main__()


    time.sleep(2)

    __main__()

def adicionar_votos(): # adicionar votos a um candidato através do código
    qualcodigo = cod_valido('\nPor favor selecione o código do candidato que deseja adicionar votos\n')
    if not existe_registro(qualcodigo):
        print('Não existe nenhum candidato com este código, favor digite outro')
        adicionar_votos()
    else:
        head_caller('Adicionar votos')
        pkl_file = open(arq,'rb')
        db2 = pickle.load(pkl_file)
        quantidade_votos = cod_valido(f"\nQuantos votos adicionar para o candidato: {db2[qualcodigo]['nome']} ")
        my_old_value = db2[qualcodigo]['num_votos']
        my_new_value = my_old_value + quantidade_votos
        db2[qualcodigo]['num_votos'] = my_new_value
        output = open(arq,'wb')
        pickle.dump(db2,output)
        output.close()
        print("Votos Adicionados")
    __main__()

def linha(tam=42): # apenas uma função para ajudar na visualização
    return '-' * tam


def head_caller(mytext): #função para ajudar na visualização.
    print(linha())
    print(mytext.center(42))
    print(linha())

def __main__(): #função principal no qual mostra as opções e pede um retorno
    head_caller('Opções de Cadastro')
    counter = 1
    for item in mylist:
        print(f'{counter} - {item}')
        counter +=1
    print(linha())
    resposta = cod_valido('\nPor favor selecione uma opção válida:\n')
    return resposta_menu(resposta)

def listar_candidatos():
    pkl_file = open(arq,'rb')
    db2 = pickle.load(pkl_file)
    for i in db2.keys():
        print(f"O candidato {db2[i]['nome']} tem {db2[i]['num_votos']} votos, é da região: {db2[i]['regiao']} e cargo: {db2[i]['cargo']}")

def resposta_menu(rsp): #função criada para direcionar qual função executar conforme desejo do usuário.
    if rsp == 1:
        read_candidato(arq)
    elif rsp == 2:
        gravar_candidato()
    elif rsp == 3:
        verificar_votos()
    elif rsp == 4:
        adicionar_votos()
    elif rsp == 5:
        listar_candidatos()
    elif rsp == 6:
        head_caller('Foi bom ve-lo até a proxima')
        os.system('exit()')
    else:
        os.system('cls')
        print('Por favor digite apenas números válidos')
        return __main__()

def cod_valido(resp): #função criada para verificar se o usuário digitou números
    while True:
        try:
            n = int(input(resp))
        except (ValueError, TypeError):
            print('\n Erro: por favor, digitar apenas números\n')
            continue
        else:
            return n

__main__()
