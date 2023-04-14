# Classe 1
class Pessoa:
    def _init_(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

# Classe 2
class Aluno(Pessoa):
    def _init_(self, nome, idade, matricula):
        super()._init_(nome, idade)
        self.matricula = matricula

    def estudar(self):
        print(f"O aluno {self.nome} está estudando.")

# Classe 3
class Professor(Pessoa):
    def _init_(self, nome, idade, disciplina):
        super()._init_(nome, idade)
        self.disciplina = disciplina

    def ensinar(self):
        print(f"O professor {self.nome} está ensinando {self.disciplina}.")

# Superclasse Abstrata
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass

    def comer(self):
        print("O animal está comendo.")

    def dormir(self):
        print("O animal está dormindo.")

# Subclasse 1
class Cachorro(Animal):
    def fazer_som(self):
        print("Au au")

    def latir(self):
        print("O cachorro está latindo.")

# Subclasse 2
class Gato(Animal):
    def fazer_som(self):
        print("Miau")

    def arranhar(self):
        print("O gato está arranhando.")

# Testando as classes
pessoa = Pessoa("João", 25)
aluno = Aluno("Maria", 20, "2022/001")
professor = Professor("Pedro", 35, "Matemática")
cachorro = Cachorro()
gato = Gato()

pessoa.apresentar()
aluno.apresentar()
aluno.estudar()
professor.apresentar()
professor.ensinar()
cachorro.fazer_som()
cachorro.latir()
gato.fazer_som()
gato.arranhar()