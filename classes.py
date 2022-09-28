import smtplib
import email.message


class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def metodo1(self):
        # RETORNA UMA STRING( CADEIA DE CARACTERES)
        return "EXECUTA O MÉTODO 1 DA CLASSE PESSOA"


# Herança
# A classes filha (Funcionario) só está repassando os  dados de nome,idade e email para a classe Pai(Pessoa) através do super()
class Funcionario(Pessoa):
    def __init__(self, nome, idade, email, idFuncionario):
        self.idFuncionario = idFuncionario
        super().__init__(nome, idade, email)

    # POLIMORFISMO SOBREESCREVENDO UM MÉTODO
    def metodo1(self):
        # RETORNA UMA STRING( CADEIA DE CARACTERES)
        return "EXECUTA O MÉTODO 1 DA CLASSE FUNCIONARIO"

    #   def sendEmail(self,people:Pessoa):
    #       return f'enviar email para{people.email}'

    # def send_email(self, people: Pessoa):
        corpo_email = """
            <img src="imagem.jpg">
        """

        msg = email.message.Message()
        msg["Subject"] = "Assunto"
        msg["From"] = "luscaalima81@gmail.com"
        msg["To"] = people.email
        password = "fgulupzxbpnqembd"
        msg.add_header("Content-Type", "text/html")
        msg.set_payload(corpo_email)

        s = smtplib.SMTP("smtp.gmail.com: 587")
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg["From"], password)
        s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
        return f"Email enviado para {people.email}"
