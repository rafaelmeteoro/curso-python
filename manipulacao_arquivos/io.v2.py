#!/usr/local/bin/python3
try:
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        print('Nome: {} \t Idade: {}'.format(*registro.strip().split(',')))
finally:
    arquivo.close()
