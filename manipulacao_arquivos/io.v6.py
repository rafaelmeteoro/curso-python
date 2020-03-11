#!/usr/local/bin/python3
with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {} \t Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('Arquivo já foi fechado!')
