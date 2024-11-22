class SistemaCadastro:
    def __init__(self):
        self.vingadores = []

    def cadastrar_vingador(self, vingador):
        self.vingadores.append(vingador)
        print(f"{vingador.nome_heroi} foi cadastrado com sucesso.")

    def listar_vingadores(self):
        if not self.vingadores:
            print("Nenhum vingador cadastrado.")
        for vingador in self.vingadores:
            print(vingador)

    def listar_detalhes_vingador(self, nome_heroi):
        vingador = next((v for v in self.vingadores if v.nome_heroi == nome_heroi), None)
        if vingador:
            print(f"Detalhes de {vingador.nome_heroi}:")
            print(f"Nome real: {vingador.nome_real}")
            print(f"Categoria: {vingador.categoria}")
            print(f"Poderes: {vingador.listar_poderes()}")
            print(f"Poder principal: {vingador.poder_principal}")
            print(f"Fraquezas: {', '.join(vingador.fraquezas)}")
            print(f"Nível de força: {vingador.nivel_forca}")
        else:
            print(f"Vingador {nome_heroi} não encontrado.")
