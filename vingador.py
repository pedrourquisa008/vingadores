class Vingador:
    def __init__(self, nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca):
        self.nome_heroi = nome_heroi
        self.nome_real = nome_real
        self.categoria = categoria
        self.poderes = poderes
        self.poder_principal = poder_principal
        self.fraquezas = fraquezas
        self.nivel_forca = nivel_forca
        self.tornozeleira_aplicada = False
        self.chip_gps_aplicado = False

    def aplicar_tornozeleira(self):
        self.tornozeleira_aplicada = True
        print(f"Tornozeleira aplicada em {self.nome_heroi}.")
        
    def aplicar_chip_gps(self):
        self.chip_gps_aplicado = True
        print(f"Chip GPS aplicado em {self.nome_heroi}.")
    
    def convocar(self):
        print(f"{self.nome_heroi} foi convocado!")
    
    def prender(self):
        print(f"{self.nome_heroi} foi preso!")

    def listar_poderes(self):
        return ", ".join(self.poderes)

    def __str__(self):
        return f"{self.nome_heroi} ({self.nome_real}) - {self.categoria} - Força: {self.nivel_forca}"
