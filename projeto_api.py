import requests

def main():
    print('Consulta CEP')

cep_input = input('Digite o CEP para a consulta: ')

if len(cep_input) != 8:
    print('Deve conter apenas 8 dígitos para uma consulta válida')
    exit()

request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

address_data = request.json()

if 'erro' not in address_data:
    print('CEP Encontrado:')

    print('CEP: {}'.format(address_data['cep']))
    print('Logradouro: {}'.format(address_data['logradouro']))
    print('Complemento: {}'.format(address_data['complemento']))
    print('Bairro: {}'.format(address_data['bairro']))
    print('Cidade: {}'.format(address_data['localidade']))
    print('Estado: {}'.format(address_data['uf']))

else:
    print('{}: CEP Inválido.'.format(cep_input))

option = int(input('Realizar uma nova consulta ?\n1. Sim\n2. Sair\n'))

if option == 1:
    main()
else:
    print('Saindo')

if __name__ == '__main__':
    main()
