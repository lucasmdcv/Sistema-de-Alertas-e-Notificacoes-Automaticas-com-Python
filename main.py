#cotação do dolar for menor que R$5.20

import requests 

# pegar a informação você quer
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dicionario = requisicao.json()
cotacao = float(requisicao_dicionario['USDBRL']['bid'])
print(cotacao)

# enviar um aviso - email
import smtplib
import email.message

def enviar_email():  
    corpo_email = f"""
    <p>Dólar está abaixo de R$5.20. Cotação atual: R${cotacao}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Dólar está hoje abaixo de R$5.20"
    msg['From'] = 'seu email  '
    msg['To'] = 'seu email'
    password = 'sua senha' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


if cotacao < 5.20:
    enviar_email(cotacao)



# deploy - heroku
