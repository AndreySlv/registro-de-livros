from time import sleep

# Mensagem de boas-vindas
print("╔════════════════════════════════════════════╗")
print("║         📚 BEM-VINDO AO SISTEMA 📚         ║")
print("║                                            ║")
print("║   Este é o sistema de registro de livros   ║")
print("║   da nossa biblioteca. Você pode acessar   ║")
print("║    informações detalhadas sobre nossos     ║")
print("║ títulos disponíveis e gerenciar registros. ║")
print("║                                            ║")
print("║         Vamos iniciar sua jornada!         ║")
print("╚════════════════════════════════════════════╝")
sleep(2)

banco_de_dados = [
    {"Título": "O Senhor dos Anéis", "Autor(a)": "J.R.R. Tolkien", "Editor(a)": "HarperCollins", "Ano da publicação": 1954, "Número de páginas": 1216, "Gênero": "Fantasia", "Valor": 120.0},
    {"Título": "1984", "Autor(a)": "George Orwell", "Editor(a)": "Companhia das Letras", "Ano da publicação": 1949, "Número de páginas": 328, "Gênero": "Distopia", "Valor": 40.0}
]

def menu ():
    opções = ["1.Novo livro ", "2.Livros ", "3.Pesquisar ", "4. Sair"]

    print()
    print("╔══════════════════════════╗")
    print(f"║          MENU            ║")
    print("╠══════════════════════════╣")
    for opção in opções:
        print(f" {opção}")
    print("╚══════════════════════════╝")

def submenu2 ():
    subopções2 = ["1.Imprimir tudo", "2.Imprimir trecho","3.Voltar"]
    print()
    print("╔══════════════════════════╗")
    print(f"║          MENU            ║")
    print("╠══════════════════════════╣")
    for opção in subopções2:
        print(f" {opção}")
    print("╚══════════════════════════╝")

def submenu3 ():
    subopções3 = ["1.Pesquisa geral", "2.Pesquisa especifica","3.Voltar"]
    print()
    print("╔══════════════════════════╗")
    print(f"║          MENU            ║")
    print("╠══════════════════════════╣")
    for opção in subopções3:
        print(f" {opção}")
    print("╚══════════════════════════╝")   

def adicionar_livro ():
        livro = {}

        livro['Título'] = input("Título: ")
        livro['Autor(a)'] = input("Autor(a): ")
        livro['Editor(a)'] = input("Editor(a): ")
        livro['Ano da publicação'] = int(input("Ano da publicação: "))
        livro['Número de páginas'] = int(input("Número de páginas: "))
        livro['Gênero'] = input("Gênero: ")
        livro['Valor'] = float(input("Valor (R$): "))

        banco_de_dados.append(livro)

def mostrar_registro(inicio,fim):

#consegui o objetivo de fazer apenas uma função para mostrar os registros tanto ao todo quanto em trecho 
    if inicio == 0:
        fim = len(banco_de_dados)
        tamanho = range(fim)
    else:
        tamanho = (inicio-1,fim-1)
 
    for i in tamanho:
        print()
        print("╔══════════════════════════╗")
        print(f"Livro {i+1}".center(25))
        print(f"Título: {banco_de_dados[i]['Título']}")
        print(f"Autor(a): {banco_de_dados[i]['Autor(a)']}")
        print(f"Editor(a): {banco_de_dados[i]['Editor(a)']}")
        print(f"Data de publicação: {banco_de_dados[i]['Ano da publicação']}")
        print(f"Número de páginas: {banco_de_dados[i]['Número de páginas']}")
        print(f"Gênero: {banco_de_dados[i]['Gênero']}")
        print(f"Valor: R${banco_de_dados[i]['Valor']:.2f}")

def pesquisa_geral(pesquisa):
    for i in range(len(banco_de_dados)):
        if (pesquisa.lower() in banco_de_dados[i]["Título"].lower() or
            pesquisa.lower() in banco_de_dados[i]["Autor(a)"].lower() or
            pesquisa.lower() in banco_de_dados[i]["Editor(a)"].lower() or
            pesquisa.lower() in banco_de_dados[i]["Gênero"].lower() or
            pesquisa in str(banco_de_dados[i]["Ano da publicação"]) or
            pesquisa in str(banco_de_dados[i]["Número de páginas"]) or
            pesquisa in str(banco_de_dados[i]["Valor"])):
            
            print()
            print("╔══════════════════════════╗")
            print(f"Livro {i+1}".center(25))
            print(f"Título: {banco_de_dados[i]['Título']}")
            print(f"Autor(a): {banco_de_dados[i]['Autor(a)']}")
            print(f"Editor(a): {banco_de_dados[i]['Editor(a)']}")
            print(f"Data de publicação: {banco_de_dados[i]['Ano da publicação']}")
            print(f"Número de páginas: {banco_de_dados[i]['Número de páginas']}")
            print(f"Gênero: {banco_de_dados[i]['Gênero']}")
            print(f"Valor: R${banco_de_dados[i]['Valor']:.2f}")

def pesquisa_especifica(area,pesquisa):
    if area == 1:
        for i in range(len(banco_de_dados)):
            if (pesquisa.lower() in banco_de_dados[i]["Título"].lower()):
                print(banco_de_dados[i])
    elif area == 2:
        for i in range(len(banco_de_dados)):       
            if (pesquisa.lower() in banco_de_dados[i]["Autor(a)"].lower()):
                print(banco_de_dados[i])
    elif area == 3:
        for i in range(len(banco_de_dados)):
            if (pesquisa.lower() in banco_de_dados[i]["Editor(a)"].lower()):
                print(banco_de_dados[i])
    elif area == 4:
        for i in range(len(banco_de_dados)):
            if pesquisa in str(banco_de_dados[i]["Ano da publicação"]):
                print(banco_de_dados[i])
    elif area == 5:
        for i in range(len(banco_de_dados)):
            if pesquisa in str(banco_de_dados[i]["Número de páginas"]):
                print(banco_de_dados[i])
    elif area == 6:
        for i in range(len(banco_de_dados)):
            if (pesquisa.lower() in banco_de_dados[i]["Gênero"].lower()):
                print(banco_de_dados[i])
    elif area == 7:
        for i in range(len(banco_de_dados)):
            if (pesquisa in str(banco_de_dados[i]["Valor"])):
                print(banco_de_dados[i])
    else:
        print("Valor inexiste!")

while True:
    menu()
    escolha_menu = int(input("Selecione uma opção:"))
  
    if escolha_menu == 1: 
        if len(banco_de_dados) >= 51:
            print("Número máximo de registros atigido")
        else:
            adicionar_livro()
            while True:
                continuar = int(input("Deseja adicionar outro registro? Sim(1) Não(2): "))
                if continuar == 1: 
                    adicionar_livro()
                elif continuar == 2:
                    break
                else:    
                    print("Valor inexistente")
                    continue

    elif escolha_menu == 2:
# nesse submenu eu fiz um while true dentro do outro while true principal para simular melhor um sistema de registro real
        while True:
            submenu2()
            escolha_menu2 = int(input("Selecione uma opção: "))
            if escolha_menu2 == 1:

                mostrar_registro(0,0)
                continue

            if escolha_menu2 == 2:
                trecho_inico = int(input("Informe de onde deve começar seu trecho: "))
                trecho_fim = int(input("Informe de onde deve terminar seu trecho: "))

                mostrar_registro(trecho_inico,trecho_fim)
                continue
            elif escolha_menu2 == 3:
                break
            else:
                print("Valor inexistente")
                continue

    elif escolha_menu == 3:
        while True:
            submenu3()
            escolha_menu3 = int(input("Selecione uma opção: "))

            if escolha_menu3 == 1:
                pesquisa = input("Digite o termo para pesquisa geral: ")
                pesquisa_geral(pesquisa)
            elif escolha_menu3 == 2:
                print("1 = Título, 2 = Autor(a), 3 = Editor(a), 4 = Ano da publicação, 5 = Número de páginas, 6 = Gênero, 7 = Valor")
                area = int(input("Informe qual area especifica deseja pesquisar o termo: "))
                pesquisa = (input("Digite o termo para pesquisa: "))
                pesquisa_especifica(area,pesquisa)
            elif escolha_menu3 == 3:
                break
            else:
                print("Valor inexistente")
                continue

    elif escolha_menu == 4:
        sair2 = int(input("Tem certeza que deseja sair? Todos os registros serão apagados permanentemente. Sim(1) Não(2): "))
        if sair2 == 2:
            continue
        if sair2 == 1:
            print("Volte Sempre!")
            break
        else:
            print("Valor inexistente")
            continue