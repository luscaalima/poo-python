import smtplib
import email.message
from twilio.rest import Client



class Pessoa:
    # Construtor 
    def __init__(self, nome, idade, email,telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
    def metodo1(self):
        # RETORNA UMA STRING( CADEIA DE CARACTERES)
        return "EXECUTA O MÉTODO 1 DA CLASSE PESSOA"

    # def sendSMS(self,sms:str):
    #      # Your Account SID from twilio.com/console
    #     account_sid = "AC4e10f85f5bca58d38e8ef2a20b2b8d15"
    #     # Your Auth Token from twilio.com/console
    #     auth_token  = "720bf2f4a0d874c4976998a9ce2bbd9e"
    #     client = Client(account_sid, auth_token)
    #     message = client.messages.create(
    #     to=self.telefone, 
    #     from_="+18149925691",
    #     body=sms)
    #     print("message.sid ->",message.sid)  
    #     return f'{sms} enviado'


# Herança
# A classes filha (Funcionario) só está repassando os  dados de nome,idade e email para a classe Pai(Pessoa) através do super()
class Funcionario(Pessoa):
    def __init__(self, nome, idade, email,telefone, idFuncionario):
        if idFuncionario == 'sas':
         self.idFuncionario = 'idFuncionario'
        else :
            self.idFuncionario ="lucas " 
        super().__init__(nome, idade, email,telefone)

    # POLIMORFISMO SOBREESCREVENDO UM MÉTODO
    def metodo1(self):
        # RETORNA UMA STRING( CADEIA DE CARACTERES)
        return "EXECUTA O MÉTODO 1 DA CLASSE FUNCIONARIO"

    #   def sendEmail(self,people:Pessoa):
    #       return f'enviar email para{people.email}'

    # def send_email(self, people: Pessoa):
    #     corpo_email = """
    #         <img src="imagem.jpg">
    #      """

    #     msg = email.message.Message()
    #     msg["Subject"] = "Assunto"
    #     msg["From"] = "luscaalima81@gmail.com"
    #     msg["To"] = people.email
    #     password = "fgulupzxbpnqembd"
    #     msg.add_header("Content-Type", "text/html")
    #     msg.set_payload(corpo_email)

    #     s = smtplib.SMTP("smtp.gmail.com: 587")
    #     s.starttls()
    #     # Login Credentials for sending the mail
    #     s.login(msg["From"], password)
    #     s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
    #     return f"Email enviado para {people.email}"
