#Seed e de onde vem os numeros/letras 'aleatorios' do codigo
# onde a biblioteca secrets faz uns cauculos com numeros de
# desempenho da sua maquina Ex : "o uso de memoria ram"
#e faz uns caulos para fazer sua senh, tipo os calculos 
#que tem no numero do seu pdf
import secrets
#variáveis
clas = secrets.SystemRandom #fontes de alta qualidade
numro = secrets.choice('sequencia(range) etc..')#escolhe um numero aleatorio da sequencia
#secrets.randbits("k")       #retorna um vcalor inteiro transformado em bits 
#aqui e onde a gente vai poder usar as funções 
# da biblioteca, mas não vamos trabalhar com isso
#TOKENS
# funçã apenas da biblioteca e que é usada na criação das senhas
#secrets.token_bytes(["numero de bytes"])    #transcreve o numero para o tanto de bytes
#secrets.token_hex(["bytes em 2 hexagonais"])     #de numero inteiro para bytes para 2 hexgonais
#secrets.token_urlsafe(["urls"])    #muito forte para urls


#codigo

print("Progama simples de senhas fortes da equipe Qr")
print("Nossa equipe preparou 3 tipos de senhas exclusivamente pra vocé ")
print("1:Senha em Bytes - segura (impossivel de rastrear). ")
print("2:Senha em Hexadecima - impossivel acesso 100x mais forte que a de bytes.")
print("3:Senha em Url - não recomendada para senhas e sim em endereços de sites.")

numero = int(input("Que tipo de senha vocé quer rei/rainha: "))
qnt_senhas = int(input("quantas senhas voce quer chefe/chefa : "))
qnt_digitos = int(input("quantas digitos voce quer patrão/patroa: "))

#Funções

def bytes(a):
    global senha_bytes
    senha_bytes = secrets.token_bytes(a)
    print(senha_bytes)

def hexadecimal(b):
    global senha_hexadecimal
    senha_hexadecimal = secrets.token_hex(b)
    print(senha_hexadecimal)

def urls(c):
    global senha_urls
    senha_urls = secrets.token_hex(c)
    print(senha_urls)

#Condicionais

if numero == 1:
    for i in range (0,qnt_senhas):
        bytes(qnt_digitos)

elif numero == 2:
    for i in range (0,qnt_senhas):
        hexadecimal(qnt_digitos)

elif numero == 3:
    for i in range (0,qnt_senhas):
        urls(qnt_digitos)