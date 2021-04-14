# Referências:
#    https://www.tutorialspoint.com/whatsapp-using-python
#    https://stackoverflow.com/questions/47148872/webdrivers-executable-may-have-wrong-permissions-please-see-https-sites-goo 

from EdgeWhatsApp import EdgeWhatsApp

def main():
   print('wapp-bulk-send...')
   
   whatsapp = EdgeWhatsApp(r'C:\Users\Ilton\Source\Repos\wapp-bulk-send\edgedriver_win64\msedgedriver.exe')

   mensagem = 'Ignora essa mensagem, to testando um bot aqui rapidão...'

   whatsapp.send_msg('Grupinho da Baixada 🎩', mensagem)
   whatsapp.send_msg('Amanda Martins', mensagem)
   
   del whatsapp

if __name__ == "__main__":
   main()