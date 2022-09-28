class Pessoa : 
    def __init__(self,nome,idade,email):
       self.nome = nome  
       self.idade = idade
       self.email = email
       
    def metodo1(self):
        # RETORNA UMA STRING( CADEIA DE CARACTERES)
        return 'EXECUTA O MÉTODO 1 DA CLASSE PESSOA' 
#Herança    
#A classes filha (Funcionario) só está repassando os  dados de nome,idade e email para a classe Pai(Pessoa) através do super() 
class Funcionario(Pessoa):
       def __init__(self, nome, idade,email,idFuncionario):
        self.idFuncionario = idFuncionario
        super().__init__(nome, idade,email)
       #POLIMORFISMO SOBREESCREVENDO UM MÉTODO
       def metodo1(self):
        # RETORNA UMA STRING( CADEIA DE CARACTERES)
        return 'EXECUTA O MÉTODO 1 DA CLASSE FUNCIONARIO'     