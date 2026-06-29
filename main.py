import time
from crud import create_product, read_product, read_all_products, update, delete

for i in range(0, 3):
        print('Iniciando o Sistema')
        time.sleep(1)

while True:
    print("Oque você quer fazer ?: ")
    print("-----------------------------------")
    print("[1] Cadastrar Produto")
    print("[2] Ver um Produto")
    print("[3] Ver todos os produtos")
    print("[4] Atualizar um produto")
    print("[5] Deletar um Produto")
    print("[6] Sair do Sistema")
    print("-----------------------------------")
    
    choice = int(input("Escolha: "))
    if choice == 1:
        nome = str(input("Qual o nome do produto ?: "))
        preco = float(input("Qual o preço do produto ?: "))
        create_product(nome,preco)
    elif choice == 2:
        num = int(input("Qual é o ID do produto ?: "))
        read_product(num)
    elif choice == 3:
        read_all_products()
    elif choice == 4:
        num = int(input("Qual é o ID do produto ?: "))
        nome = str(input("Qual o nome do produto ?: "))
        preco = float(input("Qual o preço do produto ?: "))
        update(num, nome, preco)
    elif choice == 5:
        num = int(input("Qual é o ID do produto ?: "))
        delete(num)
    elif choice == 6:
        break
    else:
        print("Opção incorreta")

