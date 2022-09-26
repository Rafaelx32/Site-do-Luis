# Ao abrir o GitPod, execute:
# pip install -r requirements.txt

# Trabalho Final da Disciplina:
# Implementar o delete DONE!
# Implementar o update (rota para mostrar os dados no form e outra para salvar os dados) DONE!
# Salvar os dados, conforme forem sendo manipulados, em um arquivo CSV. DONE!

from flask import Flask, render_template, request
from uuid import uuid4
import pandas as pd
import csv


app = Flask(__name__)


# le o itens.csv e joga para o index.html
@app.route('/')
def index():
    with open('compras.csv', 'rt') as file_in:
        compras = csv.DictReader(file_in)
        return render_template('index.html', compras=compras)


#sei la como funciona (não modificar)
@app.route('/create')
def create():
    return render_template('create.html')


#salva as variaveis do forms em uma nova row no arquivo .csv
@app.route('/save', methods=['POST'])
def save():

    #puxa as variaveis do forms 
    nome = request.form['nome']         
    data = request.form['data'] 
    preco = request.form['preco']

    entrada= []
    entrada.append([uuid4(), nome, data, preco]) #trocar para pandas dataset dps aaaaaaaaaaaaaaa

    #adiciona *append* uma nova row no .csv
    with open('compras.csv', 'a') as file_out:
        escritor = csv.writer(file_out)
        escritor.writerows(entrada)
   
    #redireciona para "/" 
    with open('compras.csv', 'rt') as file_in:
        compras = csv.DictReader(file_in)
        return render_template('index.html', compras=compras)


#deleta rows de acordo com o Id
@app.route('/delete/<id>')
def delete(id):

    # abre o arquivo .csv pelo pandas
    data = pd.read_csv("compras.csv") 
    #seta o index valeu para a columm 'Id'
    data = data.set_index("Id") 

    #dropa toda row que tiver a mesma variavel "id" na columm index
    data.drop(id, axis='index', inplace=True) 
    
    #salva o novo dataset
    data.to_csv('compras.csv')  

    # função que le o arquivo e envia a variavel para o html OBS: provavelmente existe alguma outra forma mais simples e eficiente de fazer isso, porem esta funcionando ent deia quieto 
    with open('compras.csv', 'rt') as file_in:
        compras = csv.DictReader(file_in)
        return render_template('index.html', compras=compras)
    

#pega as variaveis da row que o usuario quer modificar e coloca dentro dos forms
@app.route('/update/<id>/<nome>/<data>/<preco>')
def update(id,nome,data,preco):#obtem as var pela url 
    lista = [id,nome,data,preco]#transforma em lista para facilitar
    return render_template('update.html', lista=lista) #e joga para o update.html


#salva os forms que foram modificados do /update/
@app.route('/saveup', methods=['POST'])
def saveup():

    #obtem as novas variaveis
    id = request.form['id'] # o id esta ocultado na pagina
    nome = request.form['nome']         
    dat = request.form['data'] 
    preco = request.form['preco']

    #abre o dataframe do .csv
    data = pd.read_csv("compras.csv")

    #cria um novo dataframe apartir das novas variaveis
    new_df = pd.DataFrame({'Id': [id],'Nome': [nome],'Data': [dat],'Preco': [preco]})

    #seta os index's para a coluna 'Id'
    #n sei se isso é necessario mas na minha mente faz sentido 
    data = data.set_index("Id")
    new_df = new_df.set_index("Id")

    #atualiza os dados do data frame antigo com o novo
    data.update(new_df)

    #salva o arquivo
    data.to_csv('compras.csv')

    #redireciona para "/"
    with open('compras.csv', 'rt') as file_in:
        compras = csv.DictReader(file_in)
        return render_template('index.html', compras=compras)

app.run(debug=True)

# CLIENTE -- SERVIDOR
# Navegador -- AWS (Flask)

# Client -> REQUEST (Mensagem HTTP) -> Server 
# Server -> RESPONSE (Mensagem HTTP) -> CLIENTE

# HTTP (HyperText Transfer Protocol)
# HTML (HyperText Markup Language)

# Mensagem HTTP: 
# Header
# Body
# METHOD (GET, POST), Métodos suportados pelos navegadores.
# GET -> DADOS PELA URL
# POST -> OCULTO OS DADOS (NÃO MOSTRA NA URL)

# METHOD (API = GET, POST, PUT, DELETE, PATCH, OPTIONS)

# API REST
# POST   (C)REATE
# GET    (R)EAD
# PUT    (U)PDATE
# PATCH  (U)PDATE PARCIAL
# DELETE (D)ELETE


