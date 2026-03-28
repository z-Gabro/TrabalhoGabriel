import subprocess

while True:
    print ('SELECIONE QUAL PROJETRO DESEJA EXECUTAR:')
    print ('1 - N sei o nome')
    print ('2 - Buscas')
    print ('3 - Ordenação')
    print ('0 - Sair')
    escolha = input('Insira sua escolha: ')

    match escolha:
        case '1':
            print('o animal do matheus n commito ainda')
        case '2':
            subprocess.run(["python", "projeto3-ordenacao\main.py"])

