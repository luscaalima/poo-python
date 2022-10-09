from classes import *

#Insânciando um objeto da classe UsuarioNetflix
#p1 = UsuarioNetflix('Lucas Lima',21,'luscaalima81@gmail.com','+5519988648257')
#print(p1.__dict__)
#SIMULAR O ENVIO DE UMA VERIFICAÇÃO(SMS) PARA CRIAÇÃO DE CONTA 
# p1.sendSMS('SEU CÓDIGO PARA CONFIRMAÇÃO DA CONTA  É #####')

##   ----------------------------------------------------------------
#Insânciando um objeto da classe FuncionarioNetflix(UsuarioNetflix)
# f1 = FuncionarioNetflix('NomeFuncionario',30,'email@netflix.com','38333497','idFuncionario')
# print(f1.__dict__)
#print(f1.classe)
#f1.send_email(p1)
# print('POLIMORFISMO',f1.metodo1())
#UTILIZANDO UM MÉTODO DA CLASSE PAI (UsuarioNetflix)
#print(f1.metodoQualquer())
# print('acessando um atributo da classe pai (UsuarioNetflix) ->',f1.classe)



##   ----------------------------------------------------------------
#Insânciando um objeto da classe Pessoa
#CRIANDO UMA PESSOA PASSANDO NOME E IDADE
# pessoa1= Pessoa('Lucas Lima',21)
# print('Pessoa1',pessoa1.__dict__)

#CRIANDO UMA PESSOA PASSANDO NOME E DATA DE NASCIMENTO ACESSANDO UM MÉTODO DA CLASSE
# FACTORY METODO ?
# pessoa2= Pessoa.porAnoNascimento('Joao',2000)
# print('Pessoa2 ',pessoa2.__dict__)


##   ----------------------------------GETTERS and SETTERS------------------
prod = Produto("CAMISETA",50)
prod.desconto(10)
print(prod.preco)
prod2 = Produto("COPO",15)
prod2.desconto(10)
print(prod2.preco)
### /*
prod3 = Produto("OUTRO PRODUTO","R$20")
prod3.desconto(10)
print(prod3.preco)