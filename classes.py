class Pessoa : 
    def __init__(self,nome,idade,email):
       self.nome = nome  
       self.idade = idade
       self.email = email
    
    
#Herança    
class Funcionario(Pessoa):
       def __init__(self, nome, idade,email,idFuncionario):
        self.idFuncionario = idFuncionario
        super().__init__(nome, idade,email)