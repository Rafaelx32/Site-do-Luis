import csv

clientes = [
  ['Id', 'Nome', 'Data', 'Preco' ],
  ['1', 'carro', '22/06/2020','13252332'],
  ['2', 'busss', '22/06/2022','2'],
  ['3', 'moto', '20/06/2020','303'],
]

print(clientes[1][1])


with open('clientes.csv', 'wt') as file_out:
  escritor = csv.writer(file_out)
  escritor.writerows(clientes)
  
  