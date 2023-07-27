class Epp:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade


class GerenciadorEpp:
    def __init__(self):
        self.estoque = []

    def adicionar_epp(self, nome, quantidade):
        novo_epp = Epp(nome, quantidade)
        self.estoque.append(novo_epp)
        print(f"{quantidade} unidades de {nome} foram adicionadas ao estoque.")

    def listar_epps(self):
        if not self.estoque:
            print("O estoque está vazio.")
        else:
            print("EPPs disponíveis no estoque:")
            for epp in self.estoque:
                print(f"{epp.nome}: {epp.quantidade} unidades")

    def remover_epp(self, nome, quantidade):
        for epp in self.estoque:
            if epp.nome == nome:
                if epp.quantidade >= quantidade:
                    epp.quantidade -= quantidade
                    print(f"{quantidade} unidades de {nome} foram removidas do estoque.")
                else:
                    print(f"Não é possível remover {quantidade} unidades de {nome}. "
                          f"A quantidade disponível é {epp.quantidade}.")
                return
        print(f"O EPP {nome} não está disponível no estoque.")


def main():
    gerenciador = GerenciadorEpp()

    while True:
        print("\n===== Gerenciamento de EPPs =====")
        print("1. Adicionar EPP")
        print("2. Listar EPPs")
        print("3. Remover EPP")
        print("4. Sair")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            nome = input("Digite o nome do EPP: ")
            quantidade = int(input("Digite a quantidade a ser adicionada: "))
            gerenciador.adicionar_epp(nome, quantidade)

        elif opcao == "2":
            gerenciador.listar_epps()

        elif opcao == "3":
            nome = input("Digite o nome do EPP a ser removido: ")
            quantidade = int(input("Digite a quantidade a ser removida: "))
            gerenciador.remover_epp(nome, quantidade)

        elif opcao == "4":
            print("Saindo do gerenciador de EPP. Até logo!")
            break

        else:
            print("Opção inválida. Por favor, digite um número de 1 a 4.")


if __name__ == "__main__":
    main()
