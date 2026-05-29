class GerenciadorNotas:
    def __init__(self):
        self.notas = []

    def cadastrar_nota(self, nota: float):
        """Cadastra uma nota após validar se ela é válida (entre 0 e 10)."""
        if not isinstance(nota, (int, float)):
            raise ValueError("A nota deve ser um número.")
        if nota < 0 or nota > 10:
            raise ValueError("Nota inválida! A nota deve estar entre 0 e 10.")
        self.notas.append(float(nota))

    def calcular_media(self) -> float:
        """Calcula e retorna a média das notas cadastradas com duas casas decimais."""
        if not self.notas:
            return 0.0
        return round(sum(self.notas) / len(self.notas), 2)

    def verificar_situacao(self) -> str:
        """Verifica a situação do aluno com base na média atual conforme as regras."""
        media = self.calcular_media()
        
        if media >= 7.0:
            return "Aprovado"
        elif 5.0 <= media < 7.0:
            return "Recuperação"
        else:
            return "Reprovado"
