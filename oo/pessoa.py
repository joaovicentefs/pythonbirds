class Pessoa:
    def __init__(self, *filhos, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    gregorio = Pessoa(nome='Gregório', idade=3)
    joao = Pessoa(gregorio, nome='João', idade=36)
    print(Pessoa.cumprimentar(joao))
    print(id(joao))
    print(joao.cumprimentar())
    print(joao.nome)
    print(gregorio.idade)
    for filho in joao.filhos:
        print(filho.nome)
    joao.sobrenome = 'Farias'
    del joao.filhos
    print(joao.__dict__)
    print(gregorio.__dict__)