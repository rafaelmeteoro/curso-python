#!/usr/local/bin/python3
with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {} \t Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('Arquivo já foi fechado!')
