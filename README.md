# wapp-bulk-send
Script para automatizar o envio de mensagens pelo WhatsApp.

# Requisitos

### Selenium
`C:\> py -m pip install selenium`

### Edge Browser
[Download](https://www.microsoft.com/pt-br/edge)

### Edge Webdriver
Fazer o [Download](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) de acordo com a versão do Edge instalada na máquina.

# Utilização

* **Definir uma lista com os nomes dos contatos e/ou grupos**

```python
contatos = ['Wagner','Arthur','Ex-CSM']
```

* **Definir a mensagem**

```python
mensagem = 'Testando um bot...'
```

* **Instanciar a classe `EdgeWhatsApp` com o caminho para o Webdriver**

```python
whatsapp = EdgeWhatsApp(r'C:\edgedriver_win64\msedgedriver.exe')
```

* **Enviar as mensagens**

```python
for contato in contatos:
   whatsapp.send_msg(contato, mensagem)
```
