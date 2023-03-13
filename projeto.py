import pyttsx3
import time
import math

def saudacao(hora):

    madrugada = ['00', '01', '02', '03', '04', '05']
    while hora in madrugada:
        return 'uma boa madrugada!'
    manha = ['06', '07', '08', '09', '10', '11', '12']
    while hora in manha:
        return 'um bom dia!'
    tarde = ['13', '14', '15', '16', '17', '18']
    while hora in tarde:
        return 'uma boa tarde!'
    noite = ['19', '20', '21', '22', '23']
    while hora in noite:
        return 'uma boa noite!'


def programa(n1, n2, n3, n4, n5):
    print(f' Nome: {n1}\n Idade: {n2} ano(s)\n Salário: R${n3}\n Gênero: {n4}\n Estado Civil: {n5}.')


def is_number(numero):
    return numero.replace('.', '', 1).isdigit()

engine = pyttsx3.init()
print('Olá, esse programa tem o intuito de armazenar os códigos utilizados e aprendidos pelo DEV Ariel durante seus estudos no conteúdo de Python.')
engine.say('Olá, esse programa tem o intuito de armazenar os códigos utilizados e aprendidos pelo DEV Ariel durante seus estudos no conteúdo de Python.')
engine.runAndWait()

nome = input("Digite seu nome: ")
while len(nome) < 3 or not nome.isalpha():
    print("Nome digitado incorretamente, por favor repita o processo. ")
    nome = input("Digite seu nome: ")

idade = input("Digite sua idade: ")
while not idade in range(10, 150) and not idade.isnumeric():
    print("Digite uma idade válida!")
    idade = input("Digite sua idade: ")

wage = False
while wage == False:

    salario = input("Digite seu salário: R$")
    test = is_number(salario)

    if test == False:
        print('A resposta não foi reconhecida como um número.')
        wage = False

    else:
        wage = True
        salario = float(salario)

        if salario <= 0:
            print('Esse valor não corresponde a pergunta.')
            wage = False

        else:
            wage = True

genero = input("Digite seu gênero [F] Feminino / [M] Masculino / [O] Outro: ").upper()
lista = ['F', 'M', 'O']
while genero not in lista:
    print("Gênero inexistente!")
    genero = input("Digite seu gênero [F] Feminino / [M] Masculino / [O] Outro: ").upper()

match genero:
    case 'F':
        genero = 'Feminino'
    case 'M':
        genero = 'Masculino'
    case 'O':
        outro = False
        while outro == False:
            personalizado = input('Qual o gênero você se identifica: ')
            if personalizado.isalpha() == False:
                outro = False
                print('Sua resposta não é válida.')
            else:
                outro = True
                genero = personalizado

estado_civil = input(
    " Das seguintes opções: \n S (Solteiro) \n C (Casado) \n V (Viúvo) \n D (Divorciado) \n Qual o seu estado civil: ").upper()
while estado_civil not in "SCVD":
    print("Estado civil digitado incorretamente, por favor digite somente uma das siglas válidas! (S, C, V ou D)")
    estado_civil = input(
        " Das seguintes opções: \n S (Solteiro) \n C (Casado) \n V (Viúvo) \n D (Divorciado) \n Qual o seu estado civil: ").upper()
match estado_civil:
    case 'S':
        estado_civil = 'Solteiro(a)'
    case 'C':
        estado_civil = 'Casado(a)'
    case 'V':
        estado_civil = 'Viúvo(a)'
    case 'D':
        estado_civil = 'Divorciado(a)'

programa(nome, idade, salario, genero, estado_civil)

idade = int(idade)
if idade < 18:
    print('Você não tem idade suficiente para prosseguir no programa.')
    engine = pyttsx3.init()
    hora_atual = time.strftime('%H')
    engine.say(f'{nome}Você não tem idade para prosseguir neste programa, obrigado pela escolha e tenha' + saudacao(hora_atual))
    engine.runAndWait()
    exit()
else:
    engine = pyttsx3.init()
    print('Crie uma senha que contenha apenas números. Vale lembrar que deve possuir no mínimo 4 dígitos.')
    engine.say('Crie uma senha que contenha apenas números. Vale lembrar que deve possuir no mínimo 4 dígitos.')
    engine.runAndWait()
    senha = False
    while senha == False:
        senha_do_usuario = input('Defina uma senha com números: ')
        if senha_do_usuario.isnumeric() == False:
            print('Apenas números na senha.')
        elif len(senha_do_usuario) <= 3 or len(senha_do_usuario) > 12:
            print('A senha deve conter no mínimo 4 dígitos, e no máximo 12.')
        else:
            senha1 = set(senha_do_usuario)
            if len(senha1) == 1:
                print('Sua senha é linear.')
            else:
                senha = True
                engine = pyttsx3.init()
                print(f'{nome}, seja bem vindo(a).')
                engine.say(f'{nome}, seja bem vindo.')
                engine.runAndWait()
                acertou = False
                while acertou == False:
                    print('''O que você deseja fazer?
                                      [1] Descobrir se tomei multa.
                                      [2] Jogo do chute.
                                      [3] Descobrir fatorial.
                                      [4] Valor hora de trabalho.
                                      [5] Teste o programa, qual número é maior?
                                      [6] Descubra sua média escolar.
                                      [7] Calculadora científica.
                                      [8] Converta escalas termométricas.
                                      [9] O seu salário em valor líquido.
                                      [10] Quanto cobrará o imposto de renda (2022).
                                      [11] Gere um CPF válido.
                                      [12] Descubra se o CPF é válido ou não.
                                      [13] Descubra se o CNPJ é válido ou não.
                                      [14] Encurte a URL do seu site.
    
                                      Digite "Perfil" para gerenciar nome e senha.
    
                                      Digite "Sair" para encerrar o programa.''')
                    engine = pyttsx3.init()
                    engine.say(f'{nome}, digite um dos respectivos números para executar uma ação no programa.')
                    engine.runAndWait()
                    opcao = str(input('Sua opção: ').upper())
                    if opcao == str('1'):
                        acertou = True
                    elif opcao == str('2'):
                        acertou = True
                    elif opcao == str('3'):
                        acertou = True
                    elif opcao == str('4'):
                        acertou = True
                    elif opcao == str('5'):
                        acertou = True
                    elif opcao == str('6'):
                        acertou = True
                    elif opcao == str('7'):
                        acertou = True
                    elif opcao == str('8'):
                        acertou = True
                    elif opcao == str('9'):
                        acertou = True
                    elif opcao == str('10'):
                        acertou = True
                    elif opcao == str('11'):
                        acertou = True
                    elif opcao == str('12'):
                        acertou = True
                    elif opcao == str('13'):
                        acertou = True
                    elif opcao == str('14'):
                        acertou = True
                    elif opcao == str('SAIR'):
                        acertou = True
                    elif opcao == str('PERFIL'):
                        acertou = True
                    if opcao == str('1'):
                        veloc = False
                        while veloc == False:
                            velocidade = input('Digite a velocidade do seu veículo: ')
                            if velocidade.isnumeric() == False:
                                print('Digite apenas números.')
                            else:
                                veloc = True
                                veloc_m = False
                                while veloc_m == False:
                                    velocidade_maxima = input('Digite a velocidade máxima da pista: ')
                                    if velocidade_maxima.isnumeric() == False:
                                        print('Digite apenas números.')
                                    else:
                                        veloc_m = True
                                        velocidade = int(velocidade)
                                        velocidade_maxima = int(velocidade_maxima)
                                        if velocidade <= velocidade_maxima:
                                            print('Você não levou multa.')
                                            acertou = False
                                        elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
                                            print('Você tomou uma multa leve.')
                                            acertou = False
                                        elif velocidade > velocidade_maxima + 10 and velocidade <= velocidade_maxima + 20:
                                            print('Você tomou uma multa grave.')
                                            acertou = False
                                        elif velocidade > velocidade_maxima + 20:
                                            print('Você tomou uma multa gravíssima.')
                                            acertou = False
                    if opcao == str('2'):
                        import random

                        valor_aleatorio = random.randint(1, 100)
                        print('O programa escolheu um número entre 1 e 100, tente adivinhá-lo.')
                        certado = False
                        while certado == False:
                            numero_do_jogador = input('Digite um número de 1 a 100: ')
                            if numero_do_jogador.isnumeric() == False:
                                print('Essa caractere não é válida.')
                            else:
                                certado = True
                                numero_do_jogador = int(numero_do_jogador)
                                if numero_do_jogador > 100 or numero_do_jogador < 1:
                                    print('Apenas números entre 1 e 100.')
                                    certado = False
                                else:
                                    certado = True
                                    if numero_do_jogador > valor_aleatorio:
                                        print('O chute é maior que o valor gerado, tente novamente.')
                                        certado = False
                                    elif numero_do_jogador < valor_aleatorio:
                                        print('O chute é menor que o valor gerado, tente novamente.')
                                        certado = False
                                    elif numero_do_jogador == valor_aleatorio:
                                        certado = True
                                        print('Parabéns, você acertou o chute.')
                                        acertou = False
                    if opcao == str('3'):
                        from math import factorial

                        fator = False
                        while fator == False:
                            numero = input('Digite o número que você quer descobrir o fatorial: ')
                            if numero.isnumeric() == False:
                                print('Apenas números naturais inteiros.')
                            else:
                                numero = int(numero)
                                print('O fatorial do número escolhido é:', factorial(numero))
                                fator = True
                                acertou = False
                    if opcao == str('4'):
                        salario_mensal = salario
                        print(f'Para esse calculo será usado o salário que você definiu no início: {salario}')
                        hr = False
                        while hr == False:
                            horas_trabalhadas_por_mes = input(
                                'Digite a quantidade de horas trabalhadas no mês: ')
                            if horas_trabalhadas_por_mes.isnumeric() == False:
                                print('Caractere inválida.')
                            else:
                                hr = True
                                salario_mensal = int(salario_mensal)
                                horas_trabalhadas_por_mes = int(horas_trabalhadas_por_mes)
                                valor_hora = salario_mensal / horas_trabalhadas_por_mes
                                print('Você recebe por hora, em torno de: R${}'.format(
                                    valor_hora))
                                acertou = False
                    if opcao == str('5'):
                        print('Válido apenas para números inteiros.')
                        maior = False
                        while maior == False:
                            primeiro_valor = input('Digite o primeiro valor: ')
                            if primeiro_valor.isnumeric() == False:
                                print('Caractere inválida.')
                            else:
                                maior = True
                                segundo = False
                                while segundo == False:
                                    segundo_valor = input('Digite o segundo valor: ')
                                    if segundo_valor.isnumeric() == False:
                                        print('Caractere inválida.')
                                    else:
                                        segundo = True
                                        primeiro_valor = int(primeiro_valor)
                                        segundo_valor = int(segundo_valor)
                                        if primeiro_valor > segundo_valor:
                                            print(
                                                'O primeiro valor é maior. ({})'.format(primeiro_valor))
                                            acertou = False
                                        elif primeiro_valor == segundo_valor:
                                            print('Os valores são iguais.')
                                            acertou = False
                                        else:
                                            print('O segundo valor é maior. ({})'.format(segundo_valor))
                                            acertou = False
                    if opcao == str('6'):
                        pn = float(input('Digite a nota do primeiro bimestre: '))
                        sn = float(input('Digite a nota do segundo bimestre: '))
                        tn = float(input('Digite a nota do terceiro bimestre: '))
                        qn = float(input('Digite a nota do quarto bimestre: '))
                        mn = 0
                        mn = pn + sn + tn + qn
                        r = mn / 4
                        print('Sua média escolar foi de:', r)
                        acertou = False
                    if opcao == str('7'):
                        def is_number(numero):
                            return numero.replace('.', '', 1).isdigit()

                        def calculadora(num1, num2, operador):
                            match operador:
                                case "+":
                                    return num1 + num2
                                case "-":
                                    return num1 - num2
                                case "*":
                                    return num1 * num2
                                case "/":
                                    return num1 / num2
                                case "^":
                                    return num1 ** num2
                                case "RAIZ":
                                    print('Só é tirada a raiz do primeiro número inserido.')
                                    return math.sqrt(num1)
                                case "TAN":
                                    print('A tangente só é tirada do primeiro número inserido.')
                                    return math.tan(num1)
                                case "COS":
                                    print('O cosseno só é tirado do primeiro número inserido.')
                                    return math.cos(num1)
                                case "SIN":
                                    print('O seno só é tirado do primeiro número inserido.')
                                    return math.sin(num1)

                        calc = False
                        while calc == False:
                            num1 = input('Digite o primeiro número: ')
                            if is_number(num1) == False:
                                calc = False
                                print('Número inválido.')
                            else:
                                calc = True
                                operator = False
                                while operator == False:
                                    operador = input(
                                        "Digite o operador (+, -, *, /, ^, raiz, tan, cos ou sin): ").upper()
                                    calcular = ['+', '-', '*', '/', '^', 'RAIZ', 'TAN', 'COS', 'SIN']
                                    if operador not in calcular:
                                        print('Operador inválido.')
                                        operator = False
                                    else:
                                        operator = True
                                        calc2 = False
                                        while calc2 == False:
                                            num2 = input('Digite o segundo número: ')
                                            if is_number(num2) == False:
                                                calc2 = False
                                                print('Número inválido.')
                                            else:
                                                calc = True
                                                calc2 = True
                                                num1 = float(num1)
                                                num2 = float(num2)
                                                resultado = calculadora(num1, num2, operador)
                                                print(resultado)
                                                continuar = False
                                                while continuar == False:
                                                    print(
                                                        'Escolha a opção desejada. \n 1. Continuar calculando a partir do resultado anterior. \n 2. Reiniciar o cálculo com novos números. \n 3. Encerrar o programa.')
                                                    c = input('Sua opção: ')
                                                    if c == '1':
                                                        continuar = True
                                                        num1 = resultado
                                                        operator = False
                                                    elif c == '2':
                                                        continuar = True
                                                        print('Reiniciando o programa...')
                                                        calc = False
                                                    elif c == '3':
                                                        print('Saindo...')
                                                        continuar = True
                                                        acertou = False
                                                    else:
                                                        print('Resposta não identificada.')
                                                        continuar = False
                    if opcao == str('8'):
                        print('''O que você deseja transformar?
                                           [1] Fahrenheit em Celsius
                                           [2] Fahrenheit em Kelvins
                                           [3] Celsius em Fahrenheit
                                           [4] Celsius em Kelvins
                                           [5] Kelvins em Fahrenheit
                                           [6] Kelvins em Celsius''')
                        opcao = int(input('Sua opção: '))
                        if opcao == 1:
                            fec = float(input('Digite a quantidade de Fahrenheit: '))
                            fec_t = fec - 32
                            fec_f = fec_t / 1.8
                            print('Convertendo para Celsius, fica:', fec_f)
                            acertou = False
                        if opcao == 2:
                            fek = float(input('Digite a quantidade de Fahrenheit: '))
                            fek_t = fek + 459.57
                            fek_f = fek_t * 5 / 9
                            print('Convertendo para Kelvins, fica:', fek_f)
                            acertou = False
                        if opcao == 3:
                            cef = float(input('Digite a quantidade de Celsius: '))
                            cef_t = cef * 1.8
                            cef_f = cef_t + 32
                            print('Convertendo para Fahrenheit, fica:', cef_f)
                            acertou = False
                        if opcao == 4:
                            cek = float(input('Digite a quantidade de Celsius: '))
                            cek_f = cek + 273.15
                            print('Convertendo para Kelvins, fica:', cek_f)
                            acertou = False
                        if opcao == 5:
                            kef = float(input('Digite a quantidade de Kelvins: '))
                            kef_t = kef - 273.15
                            kef_f = kef_t * 1.8 + 32
                            print('Convertendo para Fahrenheit, fica:', kef_f)
                            acertou = False
                        if opcao == 6:
                            kec = float(input('Digite a quantidade de Kelvins:'))
                            kec_f = kec - 273.15
                            print('Convertendo para Celsius, fica:', kec_f)
                            acertou = False
                    if opcao == str('9'):
                        valor_hora = float(input('Digite quanto ganha por hora no referido mês: '))
                        horas_trabalhadas = float(
                            input('Digite a quantidade de horas trabalhadas no mês: '))
                        salario_mensal = valor_hora * horas_trabalhadas
                        print('Salario bruto: R$', salario_mensal)
                        ir = salario_mensal - (salario_mensal * 0.11)
                        print('Descontando o imposto de renda(11%): R$', ir, '(', salario_mensal * 0.11,
                              ')')
                        inss = ir - (ir * 0.08)
                        print('Descontando o INSS(8%): R$', inss, '(', ir * 0.08, ')')
                        sindicato = inss - (inss * 0.05)
                        print('Descontando o Sindicato(5%): R$', sindicato, '(', inss * 0.05, ')')
                        salario_liquido = sindicato
                        print('Salário líquido é igual a: R$', salario_liquido)
                        acertou = False
                    if opcao == str('10'):
                        salario_mensal = float(input('Digite o valor bruto do seu salário mensal: R$ '))
                        if salario_mensal <= 1903.98:
                            print('Não houve valor descontado no seu salário: R$', salario_mensal)
                            acertou = False
                        if salario_mensal >= 1903.99 and salario_mensal <= 2826.65:
                            desconto_1 = (salario_mensal * 0.075) - 142.80
                            desconto_1f = salario_mensal - desconto_1
                            print('O seu salário após o imposto de renda(7,5%): R${:.2f}'.format(
                                desconto_1f))
                            print('desconto de: R${:.2f}'.format(desconto_1))
                            acertou = False

                        if salario_mensal >= 2826.66 and salario_mensal <= 3751.05:
                            desconto_2 = (salario_mensal * 0.15) - 354.80
                            desconto_2f = salario_mensal - desconto_2
                            print('O seu salário após o imposto de renda(15%): R${:.2f}'.format(
                                desconto_2f))
                            print('desconto de: R${:.2f}'.format(desconto_2))
                            acertou = False

                        if salario_mensal >= 3751.06 and salario_mensal <= 4664.68:
                            desconto_3 = (salario_mensal * 0.225) - 636.13
                            desconto_3f = salario_mensal - desconto_3
                            print('O seu salário após o imposto de renda(22.5%): R${:.2f}'.format(
                                desconto_3f))
                            print('desconto de: R${:.2f}'.format(desconto_3))
                            acertou = False

                        if salario_mensal > 4664.68:
                            desconto_4 = (salario_mensal * 0.275) - 869.36
                            desconto_4f = salario_mensal - desconto_4
                            print('O seu salário após o imposto de renda(27.5%): R${:.2f}'.format(
                                desconto_4f))
                            print('desconto de: R${:.2f}'.format(desconto_4))
                            acertou = False

                    if opcao == str('11'):
                        from random import randint

                        numeros = str(randint(100000000, 999999999))
                        cpf = numeros

                        t1 = int(cpf[0]) * 10
                        t2 = int(cpf[1]) * 9
                        t3 = int(cpf[2]) * 8
                        t4 = int(cpf[3]) * 7
                        t5 = int(cpf[4]) * 6
                        t6 = int(cpf[5]) * 5
                        t7 = int(cpf[6]) * 4
                        t8 = int(cpf[7]) * 3
                        t9 = int(cpf[8]) * 2

                        r1 = t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8 + t9

                        r1_f = 11 - (r1 % 11)
                        if r1_f > 9:
                            t10 = 0
                        else:
                            t10 = r1_f

                        u1 = int(cpf[0]) * 11
                        u2 = int(cpf[1]) * 10
                        u3 = int(cpf[2]) * 9
                        u4 = int(cpf[3]) * 8
                        u5 = int(cpf[4]) * 7
                        u6 = int(cpf[5]) * 6
                        u7 = int(cpf[6]) * 5
                        u8 = int(cpf[7]) * 4
                        u9 = int(cpf[8]) * 3
                        u10 = t10 * 2

                        r2 = u1 + u2 + u3 + u4 + u5 + u6 + u7 + u8 + u9 + u10

                        r2_f = 11 - (r2 % 11)

                        u11 = r2_f

                        tamanho_cpf = len(cpf)
                        contador = 0
                        novo_cpf = ''
                        while contador < tamanho_cpf:
                            numero = cpf[contador]
                            if len(novo_cpf) == 9:
                                break
                            else:
                                novo_cpf += cpf[contador]
                                contador += 1

                        new_cpf = novo_cpf + str(t10) + str(u11)
                        new_cpf2 = list(new_cpf)
                        new_cpf2.insert(3, '.')
                        new_cpf2.insert(7, '.')
                        new_cpf2.insert(11, '-')
                        new_cpf3 = ''.join(new_cpf2)
                        print('O novo CPF gerado é: {}'.format(new_cpf3))

                        if new_cpf3[10] == '1':
                            print(
                                'Esse CPF foi emitido de um desses locais: Distrito Federal, Goias, Mato Grosso ou Tocantins.')
                        elif new_cpf3[10] == '2':
                            print(
                                'Esse CPF foi emitido de um desses locais: Acre, Amazonas, Amapá, Pará, Rondônia ou Roraima.')
                        elif new_cpf3[10] == '3':
                            print('Esse CPF foi emitido de um desses locais: Ceará, Maranhão e Piauí.')
                        elif new_cpf3[10] == '4':
                            print(
                                'Esse CPF foi emitido de um desses locais: Pernambuco, Rio Grande do Norte, Paraíba ou Alagoas.')
                        elif new_cpf3[10] == '5':
                            print('Esse CPF foi emitido de um desses locais: Bahia ou Sergipe.')
                        elif new_cpf3[10] == '6':
                            print('Esse CPF foi emitido do estado de Minas Gerais.')
                        elif new_cpf3[10] == '7':
                            print(
                                'Esse CPF foi emitido de um desses locais: Rio de Janeiro ou Espírito Santo.')
                        elif new_cpf3[10] == '8':
                            print('Esse CPF foi emitido do estado de São Paulo.')
                        elif new_cpf3[10] == '9':
                            print('Esse CPF foi emitido de um desses locais: Paraná ou Santa Catarina.')
                        elif new_cpf3[10] == '0':
                            print('Esse CPF foi emitido do estado do Rio Grande do Sul.')
                        acertou = False
                    if opcao == str('12'):
                        teste1 = False
                        while teste1 == False:
                            cpf = input('Digite o seu CPF: ')
                            if cpf.isnumeric() == False:
                                print('Apenas números no CPF.')
                            else:
                                teste1 = True
                                if len(cpf) < 11 or len(cpf) > 12:
                                    print('Esse CPF não possui a quantidade de números corretos.')
                                    teste1 = False
                                else:
                                    teste1 = True
                                    t1 = int(cpf[0]) * 10
                                    t2 = int(cpf[1]) * 9
                                    t3 = int(cpf[2]) * 8
                                    t4 = int(cpf[3]) * 7
                                    t5 = int(cpf[4]) * 6
                                    t6 = int(cpf[5]) * 5
                                    t7 = int(cpf[6]) * 4
                                    t8 = int(cpf[7]) * 3
                                    t9 = int(cpf[8]) * 2

                                    r1 = t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8 + t9

                                    r1_f = 11 - (r1 % 11)
                                    if r1_f > 9:
                                        t10 = 0
                                    else:
                                        t10 = r1_f

                                    u1 = int(cpf[0]) * 11
                                    u2 = int(cpf[1]) * 10
                                    u3 = int(cpf[2]) * 9
                                    u4 = int(cpf[3]) * 8
                                    u5 = int(cpf[4]) * 7
                                    u6 = int(cpf[5]) * 6
                                    u7 = int(cpf[6]) * 5
                                    u8 = int(cpf[7]) * 4
                                    u9 = int(cpf[8]) * 3
                                    u10 = t10 * 2

                                    r2 = u1 + u2 + u3 + u4 + u5 + u6 + u7 + u8 + u9 + u10

                                    r2_f = 11 - (r2 % 11)

                                    u11 = r2_f

                                    cpf2 = list(cpf)
                                    cpf2.insert(3, '.')
                                    cpf2.insert(7, '.')
                                    cpf2.insert(11, '-')
                                    cpf3 = ''.join(cpf2)

                                    tamanho_cpf = len(cpf3)
                                    contador = 0
                                    novo_cpf = ''
                                    while contador < tamanho_cpf:
                                        numero = cpf3[contador]
                                        if len(novo_cpf) == 12:
                                            break
                                        else:
                                            novo_cpf += cpf3[contador]
                                            contador += 1

                                    new_cpf = novo_cpf + str(t10) + str(u11)

                                    if new_cpf == cpf3:
                                        print('O CPF {}, é válido.'.format(new_cpf))
                                    else:
                                        print('O CPF {}, não é válido.'.format(cpf3))
                                        print('O CPF válido seria: {}'.format(new_cpf))
                                    acertou = False

                    if opcao == str('13'):
                        teste2 = False
                        while teste2 == False:
                            cnpj = input('Digite o seu CNPJ: ')
                            if cnpj.isnumeric() == False:
                                print('Apenas números no CNPJ.')
                            else:
                                teste2 = True
                                if len(cnpj) > 14 or len(cnpj) < 14:
                                    print('Esse CNPJ não possui a quantidade de números corretos.')
                                    teste2 = False
                                else:

                                    c1 = int(cnpj[0]) * 5
                                    c2 = int(cnpj[1]) * 4
                                    c3 = int(cnpj[2]) * 3
                                    c4 = int(cnpj[3]) * 2
                                    c5 = int(cnpj[4]) * 9
                                    c6 = int(cnpj[5]) * 8
                                    c7 = int(cnpj[6]) * 7
                                    c8 = int(cnpj[7]) * 6
                                    c9 = int(cnpj[8]) * 5
                                    c10 = int(cnpj[9]) * 4
                                    c11 = int(cnpj[10]) * 3
                                    c12 = int(cnpj[11]) * 2

                                    results = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10 + c11 + c12

                                    c13_f = 11 - (results % 11)
                                    if c13_f > 9:
                                        m13 = 0
                                    else:
                                        m13 = c13_f

                                    e1 = int(cnpj[0]) * 6
                                    e2 = int(cnpj[1]) * 5
                                    e3 = int(cnpj[2]) * 4
                                    e4 = int(cnpj[3]) * 3
                                    e5 = int(cnpj[4]) * 2
                                    e6 = int(cnpj[5]) * 9
                                    e7 = int(cnpj[6]) * 8
                                    e8 = int(cnpj[7]) * 7
                                    e9 = int(cnpj[8]) * 6
                                    e10 = int(cnpj[9]) * 5
                                    e11 = int(cnpj[10]) * 4
                                    e12 = int(cnpj[11]) * 3
                                    e13 = m13 * 2

                                    results2 = e1 + e2 + e3 + e4 + e5 + e6 + e7 + e8 + e9 + e10 + e11 + e12 + e13

                                    e14_f = 11 - (results2 % 11)

                                    if e14_f > 9:
                                        m14 = 0
                                    else:
                                        m14 = e14_f

                                    cnpj2 = list(cnpj)
                                    cnpj2.insert(2, '.')
                                    cnpj2.insert(6, '.')
                                    cnpj2.insert(10, '/')
                                    cnpj2.insert(15, '-')
                                    cnpj3 = ''.join(cnpj2)

                                    tamanho_cnpj = len(cnpj3)
                                    contador = 0
                                    novo_cnpj = ''
                                    while contador < tamanho_cnpj:
                                        numero = cnpj3[contador]
                                        if len(novo_cnpj) == 16:
                                            break
                                        else:
                                            novo_cnpj += cnpj3[contador]
                                            contador += 1

                                    new_cnpj = novo_cnpj + str(m13) + str(m14)

                                    if new_cnpj == cnpj3:
                                        print(f'O CNPJ {new_cnpj}, é válido.')
                                    else:
                                        print(f'O CNPJ {cnpj3}, não é válido.')
                                        print(f'O CNPJ válido seria: {new_cnpj}')
                                    acertou = False
                    if opcao == str('14'):
                        import random


                        def aleatorio():
                            part1 = ''
                            while len(part1) < 1:
                                novo = chr(random.randint(ord('a'), ord('z')))
                                part1 += novo

                            part2 = ''
                            while len(part2) < 2:
                                novo2 = chr(random.randint(ord('0'), ord('9')))
                                part2 += novo2

                            part3 = ''
                            while len(part3) < 5:
                                novo3 = chr(random.randint(ord('a'), ord('z')))
                                part3 += novo3

                            link = 'https://arielurl.com/'
                            resultado = link + part1 + part2 + part3
                            return resultado


                        def personalize(dominio):
                            link = 'https://arielurl.com/'
                            soma = link + dominio
                            return soma


                        encurt1 = False
                        while encurt1 == False:
                            escreva = input('Digite o domínio do seu site: ')
                            if 'https://' and '.com' not in escreva:
                                print('O link não possui as credenciais necessárias. (ex: https://example.com)')
                                encurt1 = False
                            else:100000
                                encurt2 = False
                                while encurt2 == False:
                                    opcao = input('Qual opção você deseja? \n'
                                                  '[1] Encurtador aleatório\n'
                                                  '[2] Encurtador personalizado\n'
                                                  ''
                                                  'Opção: ')

                                    if opcao == str('1'):
                                        encurt1 = True
                                        encurt2 = True
                                        print(f'O link gerado aleatoriamente pelo encurtador foi: {aleatorio()}')
                                        acertou = False

                                    elif opcao == str('2'):
                                        encurt1 = True
                                        encurt2 = True
                                        personalizado = input('Digite o dominio personalizado: ')
                                        tudo = personalize(personalizado)
                                        print(f'O link personalizado gerado é: {tudo}')
                                        acertou = False

                    if opcao == str('PERFIL'):
                        print('Antes de prosseguir, precisamos verificar se essa conta lhe pertence.')
                        testando = input('Digite sua senha:')
                        if testando != senha_do_usuario:
                            print('Senha incorreta.')
                            acertou = False
                        else:
                            acertou = True
                            print('Bem vindo ao painel do usuário.')
                            print(f'O nome escolhido pelo usuário foi: {nome}')
                            print(f'A senha escolhida pelo usuário foi: {senha_do_usuario}')
                            perfil = False
                            while perfil == False:
                                print(
                                    '[1] Para alterar o nome.\n[2] Para alterar a senha.\n"Voltar" para retornar ao menu.')
                                opcao2 = input('Sua opção: ').upper()
                                if opcao2 == str('1'):
                                    nn = False
                                    while nn == False:
                                        nome = input('Digite o novo nome: ')
                                        if nome.isalpha() == False:
                                            print('Apenas letras no nome.')
                                        else:
                                            nn = True
                                            print(f'Nome alterado para {nome} com sucesso.')
                                            perfil = True
                                            acertou = False
                                if opcao2 == str('2'):
                                    ns = False
                                    while ns == False:
                                        senha_do_usuario = input('Defina uma senha com números: ')
                                        if senha_do_usuario.isnumeric() == False:
                                            print('Apenas números na senha.')
                                        elif len(senha_do_usuario) <= 3 or len(senha_do_usuario) > 12:
                                            print(
                                                'A senha deve conter no mínimo 4 dígitos, e no máximo 12.')
                                        else:
                                            senha1 = set(senha_do_usuario)
                                            if len(senha1) == 1:
                                                print('Sua senha é linear.')
                                            else:
                                                ns = True
                                                print('A senha foi alterada com sucesso.')
                                                perfil = True
                                                acertou = False
                                if opcao2 == str('VOLTAR'):
                                    print('Não houve alteração em seus dados.')
                                    perfil = True
                                    acertou = False
                    if opcao == str('SAIR'):
                        engine = pyttsx3.init()
                        hora_atual = time.strftime('%H')
                        print(f'Obrigado pela preferência {nome}, volte sempre e tenha ' + saudacao(hora_atual))
                        engine.say(f'Obrigado pela preferência {nome}, volte sempre e tenha ' + saudacao(hora_atual))
                        engine.runAndWait()
                        acertou = True
