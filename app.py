# Bibliotecas necessárias
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/{{ NOME_DO_BANCO }}'

# Iniciando SQLALCHEMY
db = SQLAlchemy(app)

# Classe para criação da tabela no banco de dados
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))

    # Função para retornar um json
    def to_json(self):
        return {"id": self.id, "nome": self.nome, "email": self.email}

# db.create_all() --> Cria a tabela no banco de dados

# Selecionar todos usuários
@app.route('/usuarios', methods=["GET"])
def selecionar_users():
    usuarios_obj = Usuario.query.all()
    usuarios_json = [usuario.to_json() for usuario in usuarios_obj]

    return set_response(200, 'Usuarios', usuarios_json, 'OK')

# Selecionar um único usuário
@app.route('/usuario/<id>', methods=['GET'])
def seleciona_user(id):
    usuario_obj = Usuario.query.filter_by(id=id).first()
    usuario_json = usuario_obj.to_json()

    return set_response(200, 'usuario', usuario_json, 'OK')

# Cadastrar um novo usuário
@app.route('/usuario', methods=['POST'])
def cadastrar_user():
    body = request.get_json()

    # Validar os parâmestros que vieram na requisição
    try:
        usuario = Usuario(nome=body['nome'], email=body['email'])
        db.session.add(usuario)
        db.session.commit()

        return set_response(201, "usuario", usuario.to_json(), "cadastrado com sucesso!")
    except Exception as e:
        print(e)
        return set_response(400, 'usuario', {}, 'Erro ao cadastrar!')

# Atualizar um usuário
@app.route('/usuario/<id>', methods=['PUT'])
def atualizar_user(id):
    # Pegar usuário
    usuario_obj = Usuario.query.filter_by(id=id).first()
    # Pegar modificações
    body = request.get_json()

    try:
        if 'nome' in body:
            usuario_obj.nome = body['nome']
        if 'email' in body:
            usuario_obj.email = body['email']
        
        db.session.add(usuario_obj)
        db.session.commit()

        return set_response(200, 'usuario', usuario_obj.to_json(), 'Atualizado com sucesso!')
    except Exception as e:
        print(f'Erro: {e}')
        
        return set_response(400, 'usuario', {}, 'Erro ao atualizar!')

# Deletar um usuário
@app.route('/usuario/<id>', methods=['DELETE'])
def deletar_user(id):

    # Pegar usuario
    usuario_obj = Usuario.query.filter_by(id=id).first()

    # excluir usuário
    try:
        db.session.delete(usuario_obj)
        db.session.commit()

        return set_response(200, 'usuario', usuario_obj.to_json(), 'usuario deletado com sucesso!')
    
    except Exception as e:
        print(f'Erro: {e}')

        return set_response(400, 'usuario', {}, 'Erro ao deletar usuario.')

# Função para gerar um response formatado como json para a API
def set_response(status, nome_conteudo, conteudo, menssagen=False):
    body = {}
    body[nome_conteudo] = conteudo

    if menssagen:
        body['message'] = menssagen
    
    return Response(json.dumps(body), status=status, mimetype='application/json')

# Execultar o aplicativo
if __name__ == '__main__':
    app.run(debug=True)
