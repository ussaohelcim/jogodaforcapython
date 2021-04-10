# Feito por Michelzinho
"""
Elabore um JOGO de FORCA:
Crie uma lista de palavras e sorteie uma randomicamente uma a cada execução. Pesquise como usar números aleatórios (randômicos)
O programa mostra a forca com os espaços correspondentes às letras da palavra escolhida:
Ex: PERNAMBUCO
+-----------|
|	        O
|     	 /  |  \
|    	   /\
|
+-----------------
|                       
|

    P  _ _ N_ _ _ _ _ O							 

O usuário digita a letra, e se ela fizer parte da palavra sorteada, ela será colocada na posição certa.
A cada tentativa uma parte do boneco será desenhada.
O usuário terá 6 tentativas para acertar a palavra, antes de ser enforcado.
Use a sua criatividade.
"""

def GameOver():# printa um game over
    print('Parabens, voce perdeu')

def NovoJogo():# seta os numeros de erros e acertos em 0 quando iniciar um novo jogo
    SetNumeroErros(0)
    SetNumeroAcertos(0)

def Jogando():# função que informa que o jogo ainda esta rodando
    if(jogorodando): return True
    else: return False

def DesenhaForca(erros):# função que desenha a forca de acordo com o numero de letras erradas
    if(erros == 0): corpo = ['','','','','','']
    if(erros == 1): corpo = ['O','','','','','']
    if(erros == 2): corpo = ['O',' ','|','','','']
    if(erros == 3): corpo = ['O','/','|','','','']
    if(erros == 4): corpo = ['O','/','|','\\','','']
    if(erros == 5): corpo = ['O','/','|','\\','/','']
    if(erros == 6): 
        corpo = ['O','/','|','\\','/','\\']
        GameOver()

    return """
+-----------|
|           {}
|     	 {}  {}  {}
|    	   {} {}
|
+-----------------
|                       
|
""".format(corpo[0],corpo[1],corpo[2],corpo[3],corpo[4],corpo[5])

def GetNumerosErros():# função que retorna o numero de erros
    return quantidadeErros

def SetNumeroErros(num):#função para setar o numero de erros
    global quantidadeErros
    quantidadeErros = num

def SetNumeroAcertos(num):# função para setar o numero de acertos
    global quantidadeAcertos
    quantidadeAcertos = num

def GetNumeroAcertos():# função que retorna o numero de acertos
    return quantidadeAcertos

def Venceu():# printa que o jogador ganhou
    print('Infelizmente voce ganhou.')

def ChecaLetraEdesenha(letra):# função para checar se tem a letra 
    nErros = GetNumerosErros()
    nAcertos = GetNumeroAcertos()
    if(letra in palavra):
        if(palavra.count(letra) > 1):
            nAcertos += palavra.count(letra)
            temp = palavra
            x = palavra.count(letra)
            cont = palavra.count(letra)
            while cont > 0:
                saida[temp.find(letra)+temp.find(letra)] = letra
                temp = temp.replace(letra,'#',1)
                cont -=1
                
            print('acertou', x, 'letras')
        else:
            print('acertou')
            nAcertos += 1
            saida[palavra.find(letra)+palavra.find(letra)] = letra

    else:
        nErros +=1 
        Errou()
        #print('errou')

    global letrasEscondidas
    letrasEscondidas = ''.join(saida)
    SetNumeroErros(nErros)
    SetNumeroAcertos(nAcertos)

def Errou():
    print('errou')


import random #importar a biblioteca de numeros randomicos

palavras = ['abobora','elefante','indio','ornitorinco','uva passa'] # lista com as palavras
random.seed()
numero = random.randrange(0,len(palavras)) # numero randomico
quantidadeErros = 0
quantidadeAcertos = 0
jogorodando = True
palavra = palavras[numero]

saida = []
for i in palavra:
        saida += '_ ' 
letrasEscondidas = ''.join(saida) # uma string que mostra as letras como escondidas

print()
print('################################################################')
print()
print('Bem vindo ao jogo da forca, irei sortear uma palavra e voce deve descobrir qual é.')
print()
print('################################################################')


while True:
    NovoJogo()
    print(DesenhaForca(quantidadeErros))
    print('descubra esta palavra> ',letrasEscondidas)
    while Jogando():
        if(GetNumerosErros()>5): 
            GameOver()
            break
        if(GetNumeroAcertos()==len(palavra)):
            Venceu()
            break
        print('digite uma letra: ')
        letra = input('')
        ChecaLetraEdesenha(letra)
        print()
        print(DesenhaForca(quantidadeErros))
        #print(letrasEscondidas)
        print()
        print(letrasEscondidas)
    r = input('quer jogar novamente? S/N: ')
    if r in 'Nn':
        break
print('fechando programa.')