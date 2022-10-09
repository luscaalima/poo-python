import smtplib
import email.message
from twilio.rest import Client



class UsuarioNetflix:
    classe = "Super/Pai/Base"
    # Construtor 
    def __init__(self, nome, idade, email,telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

    def metodo1(self):
        # RETORNA UMA STRING( CADEIA DE CARACTERES)
        return "EXECUTA O MÉTODO 1 DA CLASSE UsuarioNetflix"
    def metodoQualquer(self):
        # RETORNA UMA STRING( CADEIA DE CARACTERES)
        return "EXIBINDO O MÉTODO QUALQUER"
    
    def sendSMS(self,sms:str):
        # Your Account SID from twilio.com/console
        account_sid = ""
        # Your Auth Token from twilio.com/console
        auth_token  = ""
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        to=self.telefone, 
        from_="+18149925691",
        body=sms)
        print("message.sid ->",message.sid)  
        return f'{sms} enviado'


# Herança
# A classes filha (FuncionarioNetflix) só está repassando os  dados de nome,idade e email para a classe Pai(UsuarioNetflix) através do super()
class FuncionarioNetflix(UsuarioNetflix):
    def __init__(self, nome, idade, email,telefone, idFuncionario):
        super().__init__(nome, idade, email,telefone)
        self.idFuncionario = idFuncionario

    # POLIMORFISMO SOBREESCREVENDO UM MÉTODO
    def metodo1(self):
        # RETORNA UMA STRING( CADEIA DE CARACTERES)
        return "EXECUTA O MÉTODO 1 DA CLASSE FUNCIONARIO"
   
    def send_email(self, user: UsuarioNetflix):
        corpo_email = """
         <div>
           <h1><b>NETFLIX</b></h1>
           CÓDIGO #### 
         </div>
         """

        msg = email.message.Message()
        msg["Subject"] = "Assunto"
        msg["From"] = "luscaalima81@gmail.com"
        msg["To"] = user.email
        password = "fgulupzxbpnqembd"
        msg.add_header("Content-Type", "text/html")
        msg.set_payload(corpo_email)
        s = smtplib.SMTP("smtp.gmail.com: 587")
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg["From"], password)
        s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
        print('email enviado');
        return f"Email enviado para {user.email}"


class Pessoa:
    #ATRIBUTO DA CLASSE
    anoAtual =2022
    
    #Construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    #MÉTODO DE  CLASSE
    def getAnoNascimento(self):
        return self.anoAtual - self.idade 
     
     
    #DECORADOR
    @classmethod    
    def porAnoNascimento(cls,nome,ano_nascimento):
        idade =cls.anoAtual-ano_nascimento
        return cls(nome,idade)
    
class Produto:
    
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
    
    def  desconto(self,percentual):    
        self.preco = self.preco - (self.preco * (percentual/100))   
    #GETTER
    @property
    def preco(self):
        return self._preco  
    
    #SETTER
    @preco.setter
    def preco(self, valor):
        if isinstance(valor,str):
         valor = float(valor.replace('R$',''))
        self._preco= valor
    