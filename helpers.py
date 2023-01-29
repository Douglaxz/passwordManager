#importações
import os
from gerenciadorPassword import app, db
from models import tb_user, tb_usertype, tb_passwordtype
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField,IntegerField, SelectField,PasswordField,DateField,EmailField


#criação via wftorm do formulario de usuarios
class FormularPesquisa(FlaskForm):
    pesquisa = StringField('Pesquisa:', [validators.DataRequired(), validators.Length(min=1, max=50)],render_kw={"placeholder": "digite sua pesquisa"} )
    salvar = SubmitField('Pesquisar')

##------------------------------------------------------------------------------------------------------------------------------
# USUÁRIO
##------------------------------------------------------------------------------------------------------------------------------

#criação via wftorm do formulario de usuarios
class FormularioUsuario(FlaskForm):
    nome = StringField('Nome:', [validators.DataRequired(), validators.Length(min=1, max=50)],render_kw={"placeholder": "digite o nome do usuário"})
    status = SelectField('Situação:', coerce=int, choices=[(0,"Ativo"),(1,"Inativo")])
    login = StringField('Login:', [validators.DataRequired(), validators.Length(min=1, max=50)],render_kw={"placeholder": "digite o login do usuário"})    
    tipousuario = SelectField('Situação:', coerce=int,  choices=[(g.cod_usertype, g.desc_usertype) for g in tb_usertype.query.order_by('desc_usertype')])
    email = EmailField('Email:', [validators.DataRequired(), validators.Length(min=1, max=50)],render_kw={"placeholder": "digite o email do usuário"})
    salvar = SubmitField('Salvar')


#criação via wftorm do formulario de usuarios
class FormularioUsuarioVisualizar(FlaskForm):
    nome = StringField('Nome:', [validators.DataRequired(), validators.Length(min=1, max=50)],render_kw={'readonly': True})
    status = SelectField('Situação:', coerce=int, choices=[(0,"Ativo"),(1,"Inativo")], render_kw={'readonly': True})
    login = StringField('Login:', [validators.DataRequired(), validators.Length(min=1, max=50)], render_kw={'readonly': True})
    tipousuario = SelectField('Tipo:', coerce=int, choices=[(g.cod_usertype, g.desc_usertype) for g in tb_usertype.query.order_by('desc_usertype')], render_kw={'readonly': True})
    email = EmailField('Email:', [validators.DataRequired(), validators.Length(min=1, max=50)], render_kw={'readonly': True})
    salvar = SubmitField('Editar')    

#criação via wftorm do formulario de usuarios
class FormularioUsuarioTrocarSenha(FlaskForm):
    senhaatual = PasswordField('Senha Atual:', [validators.DataRequired(), validators.Length(min=1, max=50)], render_kw={"placeholder": "digite a senha atual"})
    novasenha1 = PasswordField('Nova Senha:', [validators.DataRequired(), validators.Length(min=1, max=50)], render_kw={"placeholder": "digite a nova senha"})
    novasenha2 = PasswordField('Confirme Nova Senha:', [validators.DataRequired(), validators.Length(min=1, max=50)], render_kw={"placeholder": "digite novamente a senha"})
    salvar = SubmitField('Editar')  

#------------------------------------------------------------------------------------------------------------------------------
#TIPO USUÁRIO
#------------------------------------------------------------------------------------------------------------------------------

#criação via wftorm do formulario de tipo usuarios
class FormularioTipoUsuarioEdicao(FlaskForm):
    descricao = StringField('Descrição:', [validators.DataRequired(), validators.Length(min=1, max=50)], render_kw={"placeholder": "digite a descrição do tipo de usuário"})
    status = SelectField('Situação:', coerce=int, choices=[(0, 'Ativo'),(1, 'Inativo')])
    salvar = SubmitField('Salvar')    

#criação via wftorm do formulario de tipo usuarios
class FormularioTipoUsuarioVisualizar(FlaskForm):
    descricao = StringField('Descrição:', [validators.DataRequired(), validators.Length(min=1, max=50)], render_kw={'readonly': True})
    status = SelectField('Situação:', coerce=int, choices=[(0, 'Ativo'),(1, 'Inativo')], render_kw={'readonly': True})
    salvar = SubmitField('Salvar')    

#------------------------------------------------------------------------------------------------------------------------------
#TIPO SENHA
#------------------------------------------------------------------------------------------------------------------------------

#criação via wftorm do formulario de tipo usuarios
class FormularioTipoSenhaEdicao(FlaskForm):
    descricao = StringField('Descrição:', [validators.DataRequired(), validators.Length(min=1, max=50)], render_kw={"placeholder": "digite a descrição do tipo de senha"})
    status = SelectField('Situação:', coerce=int, choices=[(0, 'Ativo'),(1, 'Inativo')])
    icone = StringField('Icone:', [validators.DataRequired(), validators.Length(min=1, max=50)],render_kw={"placeholder": "digite a figura do bootstrap icon que servirá de icone"})
    salvar = SubmitField('Salvar')    

#criação via wftorm do formulario de tipo usuarios
class FormularioTipoSenhaVisualizar(FlaskForm):
    descricao = StringField('Descrição:', [validators.DataRequired(), validators.Length(min=1, max=50)], render_kw={'readonly': True})
    status = SelectField('Situação:', coerce=int, choices=[(0, 'Ativo'),(1, 'Inativo')], render_kw={'readonly': True})
    icone = StringField('Icone:', [validators.DataRequired(), validators.Length(min=1, max=50)], render_kw={'readonly': True})
    salvar = SubmitField('Salvar')   

#------------------------------------------------------------------------------------------------------------------------------
#USUARIO SENHA
#------------------------------------------------------------------------------------------------------------------------------

#criação via wftorm do formulario de tipo usuarios
class FormularioUsuarioSenhaEdicao(FlaskForm):
    usuario = StringField('Usuário:', [validators.DataRequired(), validators.Length(min=1, max=50)], render_kw={"placeholder": "digite o usuário"})
    senha = StringField('Senha:', [validators.DataRequired(), validators.Length(min=1, max=50)], render_kw={"placeholder": "digite a senha"})
    tipo = SelectField('Tipo:', coerce=int,  choices=[(g.cod_passwordtype, g.desc_passwordtype) for g in tb_passwordtype.query.order_by('desc_passwordtype')])
    salvar = SubmitField('Salvar')    

#criação via wftorm do formulario de tipo usuarios
class FormularioUsuarioSenhaVisualizar(FlaskForm):
    usuario = StringField('Usuário:', [validators.DataRequired(), validators.Length(min=1, max=50)], render_kw={'readonly': True})
    senha = StringField('Senha:', [validators.DataRequired(), validators.Length(min=1, max=50)], render_kw={'readonly': True})
    tipo = SelectField('Tipo:', coerce=int, choices=[(g.cod_passwordtype, g.desc_passwordtype) for g in tb_passwordtype.query.order_by('desc_passwordtype')], render_kw={'readonly': True})
    salvar = SubmitField('Salvar') 

#criação de senha forte
class FormularioSenhaEdicao(FlaskForm):
    caracteres = IntegerField('Quantidade de dígitos:', [validators.DataRequired()], render_kw={"placeholder": "digite quantos caracteres a senha deverá ter"})
    senha = StringField('Senha:', render_kw={'readonly': True})
    salvar = SubmitField('Salvar') 



#------------------------------------------------------------------------------------------------------------------------------
# OUTROS
#------------------------------------------------------------------------------------------------------------------------------
#classe de upload de imagem (desativada no momento)
def recupera_imagem(id):
    pass
#    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
#        if f'foto{id}' in nome_arquivo:
#            return nome_arquivo
#    return 'semfoto.png'

#classe de apagar fotos duplicadas de usuarios (desativada no momento)
def deleta_arquivos(id):
    pass
#    arquivo = recupera_imagem(id)
#    if arquivo != 'semfoto.png':
#        os.remove(os.path.join(app.config['UPLOAD_PATH'],arquivo))
