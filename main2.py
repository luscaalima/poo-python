from relacionamento_classes import * 

# Associação :  Uma classe não depende da outra.
# escritor = Escritor("Lucas")
# caneta = Caneta("BIC")
# escritor.ferramenta = caneta
# escritor.ferramenta.escrever()
# maquina = MaquinaEscrever()
# print(caneta.marca)


#Agregação Uma classe depende da outra.
# carrinho = CarrinhoDeCompras()
# p1 = Produto("CAMISETA",50)
# p2 = Produto("IPHONE",10000)
# p3 = Produto("CANECA",15)
# carrinho.inserir_produto(p1)
# carrinho.inserir_produto(p2)
# carrinho.inserir_produto(p3)
# carrinho.lista_produto()
# print(carrinho.soma_total())


#Composição

cliente = Cliente("Lucas",32)
cliente.insere_enderecos("Belo Horizonte","MG")

cliente2 = Cliente("Maria",22)
cliente2.insere_enderecos("Salvador","BA")
cliente2.insere_enderecos("Rio de Janeiro","RJ")

cliente.lista_enderecos()