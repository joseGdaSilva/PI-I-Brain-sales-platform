from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    def __str__(self):
        return self.nome + f" (Id: {self.id})"

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_disponivel = models.IntegerField()
    def __str__(self):
        return self.nome + f" (Id: {self.id})"

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_pedido = models.DateField()
    total_pedido = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"(Id: {self.id}) Pedido de {self.cliente.nome} {self.data_pedido.day:02d}/{self.data_pedido.month:02d}/{self.data_pedido.year} (R$ {self.total_pedido})"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total_item = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"(Id: {self.id}) (Id pedido: {self.pedido.id}) - {self.quantidade}x {self.produto.nome}"

class GestaoEstoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade_entrada = models.IntegerField()
    quantidade_saida = models.IntegerField()
    data_movimentacao = models.DateField()
    def __str__(self):
        return f"Movimento de {self.produto.nome} em {self.data_movimentacao.day:02d}/{self.data_movimentacao.month:02d}/{self.data_movimentacao.year}"
