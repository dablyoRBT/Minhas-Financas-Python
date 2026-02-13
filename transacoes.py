categorias = ("Alimentação", "Transporte", "Lazer", "Saúde", "Educação", "Contas", "Salário", "Outros")
class Transacao:
    tipos_validos = ["Entrada", "Saida"]
    def __init__(self, valor, tipo, categoria, data, descricao):
        if tipo.title() not in self.tipos_validos:
            raise ValueError("Tipo de transação inválido")
        self.valor = valor
        self.tipo = tipo
        self.categoria = categoria if categoria.title() in categorias else "Outros"
        self.data = data
        self.descricao = descricao

class ControlesTransacao:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def saldo_total(self):
        return sum(
            t.valor if t.tipo == "Entrada" else -t.valor
            for t in self.transacoes
        )

controle = ControlesTransacao()
t1 = Transacao(1250, "Entrada", "Salário", "12/02/2026", "Pagamento referente a Janeiro")
t2 = Transacao(100, "Saida", "Contas", "13/02/2026", "Conta de internet")
t3 = Transacao(250, "Saida", "Contas", "13/02/2026", "Conta de Luz")

controle.adicionar_transacao(t1)
controle.adicionar_transacao(t2)
controle.adicionar_transacao(t3)

print(f"Saldo restante: {controle.saldo_total()}")

