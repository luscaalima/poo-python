
class Escritor :
    def __init__(self, nome):
        #atributo privado não consigo acessar fora da classe sem um getter
        self.__nome = nome
        self.ferramenta = None
        
    #getter
    @property
    def nome(self):
     return self.__nome
    
    @property
    def ferramenta(self):
     return self.__ferramenta 
 
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        
        self.__ferramenta = ferramenta
 
 
class Caneta:
    def __init__(self, marca):
        self.__marca = marca
    
    #getter
    @property
    def marca(self):
     return self.__marca    
    
    def escrever(self):
        print("Caneta escrevendo...")
 
class MaquinaEscrever:
  def escrever(self):
        print("Maquina  escrevendo...")
       
class CarrinhoDeCompras:        
   
    def __init__(self):
        self.produtos=[]
        
    def inserir_produto(self,produto):  
        self.produtos.append(produto)   
    
    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome,produto.valor)    
     
    def soma_total(self):
        total = 0
        for produto in self.produtos:
           total += produto.valor
           
        return total   
        
class Produto: 
  
  def __init__(self,nome,valor):
      self.nome=nome
      self.valor=valor 


class Cliente:
    def __init__(self,nome,idade):   
        self.nome = nome
        self.idade = idade
        self.enderecos = []
        
    def insere_enderecos(self,cidade,estado):        
        self.enderecos.append(Endereco(cidade,estado))
    
    def lista_enderecos(self):
        for endereco in self.enderecos:
            print( endereco.cidade,endereco.estado     )    
             
class Endereco:   
    
    def __init__(self,cidade,estado): 
        self.cidade = cidade
        self.estado = estado          