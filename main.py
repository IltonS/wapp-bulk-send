# Referências:
#    https://www.tutorialspoint.com/whatsapp-using-python
#    https://stackoverflow.com/questions/47148872/webdrivers-executable-may-have-wrong-permissions-please-see-https-sites-goo 

from os import system
from EdgeWhatsApp import EdgeWhatsApp

def main():
   op = ''
   
   # Contatos para enviar a mensagem--------------------------------------------
   contatos = ['Wagner','Arthur','Ex-CSM']
   
   # Mensagem para enviar aos contatos------------------------------------------
   mensagem = 'Testando um bot...'

   while (op!='s') and (op!='S') and (op!='n') and (op!='N'):
      system('cls')
      print('wapp-bulk-send...\n')
      op = input('Deja enviar a mensagem:\n"' + mensagem + '"\npara ' + str(len(contatos)) + ' contatos? [S/N]: ')
   
   if (op=='s') or (op=='S'):
      print('Enviando as mensagens...')
      whatsapp = EdgeWhatsApp(r'C:\edgedriver_win64\msedgedriver.exe')
      for contato in contatos:
         whatsapp.send_msg(contato, mensagem)   
      del whatsapp
      print('Mensagens enviadas!')

   print('Tchau!')

if __name__ == "__main__":
   main()