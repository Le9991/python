class Recibo:

    def __init__(self, Nome):
        self.nome = Nome
    
    def descricao(self, valor):
        self._descricao = valor
        #atributo não pode ter o mesmo nome de função 

    @property
    def valor(self):
        return(self._valor)

    @valor.setter
    def valor(self,_valor):
        self._valor = _valor

    def __str__(self):
        texto = f'Recebemos de {self.nome} a quantia de R$ {self.valor}'
        descricao =f'\nReferente {self._descricao}'
        titulo = 'Recibo'.center(len(texto), '*')
        dados = f'{titulo}\n{texto}{descricao}'
        return (dados)
        