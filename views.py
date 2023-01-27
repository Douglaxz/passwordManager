# importação de dependencias
from datetime import datetime, date
from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
import time
from datetime import date, timedelta
from gerenciadorPassword import app, db
from models import tb_user,\
    tb_usertype,\
    tb_passwordtype,\
    tb_userpassword
from helpers import \
    FormularPesquisa, \
    FormularioUsuario, \
    FormularioUsuarioVisualizar, \
    FormularioTipoUsuarioEdicao,\
    FormularioTipoUsuarioVisualizar,\
    FormularioTipoSenhaEdicao,\
    FormularioTipoSenhaVisualizar,\
    FormularioUsuarioSenhaEdicao,\
    FormularioUsuarioSenhaVisualizar
# ITENS POR PÁGINA
from config import ROWS_PER_PAGE 

# PARA O GERADOR DE SENHA SEGURA
from random import choice
import string


# rota index
@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('/')))        
    return render_template('index.html', titulo='Bem vindos')

# rota logout
@app.route('/logout', methods = ['GET', 'POST'])
def logout():
    session['usuario_logado'] = None
    flash('logout efetuado com sucesso')
    return redirect(url_for('login'))

 #rota para a tela de login
@app.route('/login')
def login():
    return render_template('login.html')

# rota para autendicar a tela de login
@app.route('/autenticar', methods = ['GET', 'POST'])
def autenticar():
    usuario = tb_user.query.filter_by(login_user=request.form['usuario']).first()
    if usuario:
        if request.form['senha'] == usuario.password_user:
            session['usuario_logado'] = usuario.login_user
            session['nomeusuario_logado'] = usuario.name_user
            session['tipousuario_logado'] = usuario.cod_usertype
            session['coduser_logado'] = usuario.cod_user
            flash(usuario.name_user + ' Usuário logado com sucesso')
            return redirect('/')
        else:
            flash('Usuário não logado com sucesso')
            return redirect(url_for('login'))
    else:
        flash('Usuário não logado com sucesso')
        return redirect(url_for('login'))


#---------------------------------------------------------------------------------------------------------------------------------
#USUARIOS
#---------------------------------------------------------------------------------------------------------------------------------

# rota index para mostrar os usuários
@app.route('/usuario')
def usuario():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('usuario')))        
    form = FormularPesquisa()
    page = request.args.get('page', 1, type=int)
    usuarios = tb_user.query\
    .join(tb_usertype, tb_usertype.cod_usertype==tb_user.cod_usertype)\
    .add_columns(tb_user.login_user, tb_user.cod_user, tb_user.name_user, tb_user.status_user, tb_usertype.desc_usertype)\
    .order_by(tb_user.name_user)\
    .paginate(page=page, per_page=ROWS_PER_PAGE, error_out=False)
    return render_template('usuarios.html', titulo='Usuários', usuarios=usuarios, form=form)

# rota index para mostrar pesquisa usuários
@app.route('/usuarioPesquisa', methods=['POST',])
def usuarioPesquisa():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('usuarioPesquisa')))        
    page = request.args.get('page', 1, type=int)
    form = FormularPesquisa()
    usuarios = tb_user.query\
    .filter(tb_user.name_user.ilike(f'%{form.pesquisa.data}%'))\
    .join(tb_usertype, tb_usertype.cod_usertype==tb_user.cod_usertype)\
    .add_columns(tb_user.login_user, tb_user.cod_user, tb_user.name_user, tb_user.status_user, tb_usertype.desc_usertype)\
    .order_by(tb_user.name_user)\
    .paginate(page=page, per_page=ROWS_PER_PAGE, error_out=False)
    return render_template('usuarios.html', titulo='Usuários' , usuarios=usuarios, form=form)

# rota para criar novo formulário usuário 
@app.route('/novoUsuario')
def novoUsuario():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('novoUsuario')))     
    if session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('novoUsuario')))
    form = FormularioUsuario()
    return render_template('novoUsuario.html', titulo='Novo Usuário', form=form)

# rota para visualizar usuário 
@app.route('/visualizarUsuario/<int:id>')
def visualizarUsuario(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('visualizarUsuario')))    
    usuario = tb_user.query.filter_by(cod_user=id).first()
    form = FormularioUsuarioVisualizar()
    form.nome.data = usuario.name_user
    form.status.data = usuario.status_user
    form.login.data = usuario.login_user
    form.tipousuario.data = usuario.cod_usertype
    form.email.data = usuario.email_user
    return render_template('visualizarUsuario.html', titulo='Visualizar Usuário', id=id, form=form)   

# rota para editar formulário usuário 
@app.route('/editarUsuario/<int:id>')
def editarUsuario(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('editarUsuario/<int:id>')))  
    usuario = tb_user.query.filter_by(cod_user=id).first()
    form = FormularioUsuario()
    form.nome.data = usuario.name_user
    form.status.data = usuario.status_user
    form.login.data = usuario.login_user
    form.tipousuario.data = usuario.cod_usertype
    form.email.data = usuario.email_user
    return render_template('editarUsuario.html', titulo='Editar Usuário', id=id, form=form)    
       
# rota para criar usuário no banco de dados
@app.route('/criarUsuario', methods=['POST',])
def criarUsuario():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('criarUsuario')))      
    form = FormularioUsuario(request.form)
    if not form.validate_on_submit():
        return redirect(url_for('novoUsuario'))
    nome  = form.nome.data
    status = form.status.data
    login = form.login.data
    tipousuario = form.tipousuario.data
    email = form.email.data
    senha = "teste@12345"
    usuario = tb_user.query.filter_by(name_user=nome).first()
    if usuario:
        flash ('Usuário já existe')
        return redirect(url_for('index')) 
    novoUsuario = tb_user(name_user=nome, status_user=status, login_user=login, cod_usertype=tipousuario, password_user=senha, email_user=email)
    db.session.add(novoUsuario)
    db.session.commit()

    #arquivo = request.files['arquivo']
    #uploads_path = app.config['UPLOAD_PATH']
    #timestamp = time.time
    #deleta_arquivos(usuario.cod_usuario)
    #arquivo.save(f'{uploads_path}/foto{usuario.cod_usuario}-{timestamp}.jpg')

    return redirect(url_for('usuario'))

# rota para atualizar usuário no banco de dados
@app.route('/atualizarUsuario', methods=['POST',])
def atualizarUsuario():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('atualizarUsuario')))          
    form = FormularioUsuario(request.form)
    if form.validate_on_submit():
        id = request.form['id']
        usuario = tb_user.query.filter_by(cod_user=request.form['id']).first()
        usuario.name_user = form.nome.data
        usuario.status_user = form.status.data
        usuario.login_user = form.login.data
        usuario.cod_uertype = form.tipousuario.data
        db.session.add(usuario)
        db.session.commit()
    return redirect(url_for('visualizarUsuario', id=id))

# rota para deletar usuário no banco de dados
#@app.route('/deletarUsuario/<int:id>')
#def deletarUsuario(id):
#    if session['usuario_logado'] == None:
#        return redirect(url_for('login'))    
#    tb_usuarios.query.filter_by(cod_usuario=id).delete()
#    db.session.commit()
#    flash('Usuario apagado com sucesso!')
#    return redirect(url_for('usuario'))    

# rota para upload de fotos de usuário no banco de dados (desativado)
#@app.route('/uploads/<nome_arquivo>')
#def imagem(nome_arquivo):
#    return send_from_directory('uploads',nome_arquivo)

#---------------------------------------------------------------------------------------------------------------------------------
#TIPO USUARIOS
#---------------------------------------------------------------------------------------------------------------------------------

# rota index para mostrar os tipo usuários
@app.route('/tipousuario')
def tipousuario():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('tipousuario')))         
    page = request.args.get('page', 1, type=int)
    form = FormularPesquisa()    
    tiposusuario = tb_usertype.query.order_by(tb_usertype.desc_usertype)\
    .paginate(page=page, per_page=ROWS_PER_PAGE , error_out=False)
    return render_template('tipousuarios.html', titulo='Tipo Usuário', tiposusuario=tiposusuario, form=form)

# rota index para mostrar pesquisa dos tipo usuários
@app.route('/tipousuarioPesquisa', methods=['POST',])
def tipousuarioPesquisa():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('tipousuarioPesquisa')))      
    page = request.args.get('page', 1, type=int)
    form = FormularPesquisa()
    tiposusuario = tb_usertype.query.order_by(tb_usertype.desc_usertype)\
    .filter(tb_usertype.desc_usertype.ilike(f'%{form.pesquisa.data}%'))\
    .paginate(page=page, per_page=ROWS_PER_PAGE, error_out=False)
    return render_template('tipousuarios.html', titulo='Tipo Usuário' , tiposusuario=tiposusuario, form=form)    

# rota para criar novo formulário usuário 
@app.route('/novoTipoUsuario')
def novoTipoUsuario():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('novoTipoUsuario'))) 
    form = FormularioTipoUsuarioEdicao()
    return render_template('novoTipoUsuario.html', titulo='Novo Tipo Usuário', form=form)

# rota para criar tipo usuário no banco de dados
@app.route('/criarTipoUsuario', methods=['POST',])
def criarTipoUsuario():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('criarTipoUsuario')))     
    form = FormularioTipoUsuarioEdicao(request.form)
    if not form.validate_on_submit():
        return redirect(url_for('criarTipoUsuario'))
    desc  = form.descricao.data
    status = form.status.data
    tipousuario = tb_usertype.query.filter_by(desc_usertype=desc).first()
    if tipousuario:
        flash ('Tipo Usuário já existe')
        return redirect(url_for('tipousuario')) 
    novoTipoUsuario = tb_usertype(desc_usertype=desc, status_usertype=status)
    db.session.add(novoTipoUsuario)
    db.session.commit()
    return redirect(url_for('tipousuario'))

# rota para visualizar tipo usuário 
@app.route('/visualizarTipoUsuario/<int:id>')
def visualizarTipoUsuario(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('visualizarTipoUsuario')))  
    tipousuario = tb_usertype.query.filter_by(cod_usertype=id).first()
    form = FormularioTipoUsuarioVisualizar()
    form.descricao.data = tipousuario.desc_usertype
    form.status.data = tipousuario.status_usertype
    return render_template('visualizarTipoUsuario.html', titulo='Visualizar Tipo Usuário', id=id, form=form)   

# rota para editar formulário tipo usuário 
@app.route('/editarTipoUsuario/<int:id>')
def editarTipoUsuario(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('editarTipoUsuario')))  
    tipousuario = tb_usertype.query.filter_by(cod_usertype=id).first()
    form = FormularioTipoUsuarioEdicao()
    form.descricao.data = tipousuario.desc_usertype
    form.status.data = tipousuario.status_usertype
    return render_template('editarTipoUsuario.html', titulo='Editar Tipo Usuário', id=id, form=form)   

# rota para atualizar usuário no banco de dados
@app.route('/atualizarTipoUsuario', methods=['POST',])
def atualizarTipoUsuario():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('atualizarTipoUsuario')))      
    form = FormularioTipoUsuarioEdicao(request.form)
    if form.validate_on_submit():
        id = request.form['id']
        tipousuario = tb_usertype.query.filter_by(cod_usertype=request.form['id']).first()
        tipousuario.desc_usertype = form.descricao.data
        tipousuario.status_usertype = form.status.data
        db.session.add(tipousuario)
        db.session.commit()
    return redirect(url_for('visualizarTipoUsuario', id=id))    

# rota para deletar usuário no banco de dados
#@app.route('/deletarTipoUsuario/<int:id>')
#def deletarTipoUsuario(id):
#    if session['usuario_logado'] == None:
#        return redirect(url_for('login'))    
#    tb_tipousuario.query.filter_by(cod_tipousuario=id).delete()
#    db.session.commit()
#    flash('Tipo Usuario apagado com sucesso!')
#    return redirect(url_for('tipousuario'))    

#---------------------------------------------------------------------------------------------------------------------------------
#TIPO DE SENHAS
#---------------------------------------------------------------------------------------------------------------------------------
# rota index para mostrar os tipos de senha
@app.route('/tiposenha')
def tiposenha():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('tiposenha')))      
    page = request.args.get('page', 1, type=int)
    form = FormularPesquisa()    
    tipossenha = tb_passwordtype.query.order_by(tb_passwordtype.desc_passwordtype)\
    .paginate(page=page, per_page=ROWS_PER_PAGE, error_out=False)
    return render_template('tiposenha.html', titulo='Tipo Senha', tipossenha=tipossenha, form=form)

# rota index para pesquisar os beneficios
@app.route('/tiposenhaPesquisa', methods=['POST',])
def tipossenhaPesquisa():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('tipossenhaPesquisa')))          
    page = request.args.get('page', 1, type=int)
    form = FormularPesquisa()
    tipossenha = tb_passwordtype.query.order_by(tb_passwordtype.desc_passwordtype)\
    .filter(tb_passwordtype.desc_passwordtype.ilike(f'%{form.pesquisa.data}%'))\
    .paginate(page=page, per_page=ROWS_PER_PAGE, error_out=False)
    return render_template('tiposenha.html', titulo='Tipo Senha' , tipossenha=tipossenha, form=form)

# rota para criar novo formulário usuário 
@app.route('/novoTipoSenha')
def novoTipoSenha():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('novoTipoSenha')))  
    form = FormularioTipoSenhaEdicao()
    return render_template('novoTipoSenha.html', titulo='Novo Tipo Senha', form=form)

# rota para criar tipo usuário no banco de dados
@app.route('/criarTipoSenha', methods=['POST',])
def criarTipoSenha():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('criarTipoSenha')))     
    form = FormularioTipoSenhaEdicao(request.form)
    if not form.validate_on_submit():
        return redirect(url_for('criarTipoSenha'))
    desc  = form.descricao.data
    status = form.status.data
    icone = form.icone.data
    tiposenha = tb_passwordtype.query.filter_by(desc_passwordtype=desc).first()
    if tiposenha:
        flash ('Tipo Senha já existe')
        return redirect(url_for('tiposenha')) 
    novoTipoSenha = tb_passwordtype(desc_passwordtype=desc, status_passwordtype=status, icon_passwordtype=icone)
    db.session.add(novoTipoSenha)
    db.session.commit()
    return redirect(url_for('tiposenha'))

# rota para visualizar tipo usuário 
@app.route('/visualizarTipoSenha/<int:id>')
def visualizarTipoSenha(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('visualizarTipoSenha')))       
    tiposenha = tb_passwordtype.query.filter_by(cod_passwordtype=id).first()
    form = FormularioTipoSenhaVisualizar()
    form.descricao.data = tiposenha.desc_passwordtype
    form.status.data = tiposenha.status_passwordtype
    form.icone.data = tiposenha.icon_passwordtype
    return render_template('visualizarTipoSenha.html', titulo='Visualizar Tipo Senha', id=id, form=form)   

# rota para editar formulário tipo usuário 
@app.route('/editarTipoSenha/<int:id>')
def editarTipoSenha(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('editarTipoSenha')))    
    tiposenha = tb_passwordtype.query.filter_by(cod_passwordtype=id).first()
    form = FormularioTipoSenhaEdicao()
    form.descricao.data = tiposenha.desc_passwordtype
    form.status.data = tiposenha.status_passwordtype
    form.icone.data = tiposenha.icon_passwordtype
    return render_template('editarTipoSenha.html', titulo='Editar Tipo Senha', id=id, form=form)   

# rota para atualizar usuário no banco de dados
@app.route('/atualizarTipoSenha', methods=['POST',])
def atualizarTipoSenha():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('atualizarTipoSenha')))        
    form = FormularioTipoSenhaEdicao(request.form)
    if form.validate_on_submit():
        id = request.form['id']
        tiposenha = tb_passwordtype.query.filter_by(cod_passwordtype=request.form['id']).first()
        tiposenha.desc_passwordtype = form.descricao.data
        tiposenha.icon_passwordtype = form.icone.data
        tiposenha.status_passwordtype = form.status.data
        db.session.add(tiposenha)
        db.session.commit()
    return redirect(url_for('visualizarTipoSenha', id=id))   

#---------------------------------------------------------------------------------------------------------------------------------
# USUARIO SENHA
#---------------------------------------------------------------------------------------------------------------------------------
# rota index para mostrar as senhas do
@app.route('/usuarioSenha')
def usuarioSenha():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('usuarioSenha')))      
    page = request.args.get('page', 1, type=int)
    form = FormularPesquisa()    
    usuariosenhas = tb_userpassword.query.order_by(tb_userpassword.date_userpassword)\
    .join(tb_passwordtype, tb_passwordtype.cod_passwordtype==tb_userpassword.cod_passwordtype)\
    .add_columns(tb_passwordtype.icon_passwordtype, tb_passwordtype.desc_passwordtype, tb_userpassword.cod_userpassword, tb_userpassword.username_userpassword)\
    .filter(tb_userpassword.cod_user==session['coduser_logado'])\
    .order_by(tb_userpassword.date_userpassword)\
    .paginate(page=page, per_page=ROWS_PER_PAGE, error_out=False)
    return render_template('usuariosenhas.html', titulo='Senha', usuariosenhas=usuariosenhas, form=form)

# rota index para pesquisar os beneficios
@app.route('/usuarioSenhaPesquisa', methods=['POST',])
def usuarioSenhaPesquisa():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('usuarioSenhaPesquisa')))    
    page = request.args.get('page', 1, type=int)
    form = FormularPesquisa()
    usuariosenhas = tb_userpassword.query\
    .join(tb_passwordtype, tb_passwordtype.cod_passwordtype==tb_userpassword.cod_passwordtype)\
    .add_columns(tb_passwordtype.icon_passwordtype, tb_passwordtype.desc_passwordtype, tb_userpassword.cod_userpassword, tb_userpassword.username_userpassword)\
    .filter(tb_userpassword.cod_user==session['coduser_logado'])\
    .filter(tb_passwordtype.desc_passwordtype.ilike(f'%{form.pesquisa.data}%'))\
    .order_by(tb_userpassword.date_userpassword)\
    .paginate(page=page, per_page=ROWS_PER_PAGE, error_out=False)
    return render_template('usuariosenhas.html', titulo='Senha' , usuariosenhas=usuariosenhas, form=form)

# rota para criar formulário de criação de senha
@app.route('/novoUsuarioSenha')
def novoUsuarioSenha():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('novoUsuarioSenha')))  
    form = FormularioUsuarioSenhaEdicao()
    return render_template('novoUsuarioSenha.html', titulo='Nova senha', form=form)


# rota para criar tipo usuário no banco de dados
@app.route('/criarUsuarioSenha', methods=['POST',])
def criarUsuarioSenha():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('criarUsuarioSenha')))      
    form = FormularioUsuarioSenhaEdicao(request.form)
    if not form.validate_on_submit():
        return redirect(url_for('criarUsuarioSenha'))
    usuario  = form.usuario.data
    senha = form.senha.data
    tipo = form.tipo.data
    data = date.today()
    userlogado = session['coduser_logado']
    novoUsuarioSenha = tb_userpassword(cod_passwordtype=tipo, username_userpassword=usuario, password_userpassword=senha, date_userpassword=data,cod_user=userlogado)
    db.session.add(novoUsuarioSenha)
    db.session.commit()
    return redirect(url_for('usuarioSenha'))

@app.route('/visualizarUsuarioSenha/<int:id>')
def visualizarUsuarioSenha(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('visualizarTipoSenha')))
    usuariosenha = tb_userpassword.query.filter_by(cod_userpassword=id).first()
    form = FormularioUsuarioSenhaVisualizar()
    form.usuario.data = usuariosenha.username_userpassword
    form.senha.data = usuariosenha.password_userpassword
    form.tipo.data = usuariosenha.cod_passwordtype
    return render_template('visualizarUsuarioSenha.html', titulo='Visualizar Senha', id=id, form=form)

# rota para editar formulário tipo usuário 
@app.route('/editarUsuarioSenha/<int:id>')
def editarUsuarioSenha(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('editarTipoSenha')))    
    usuariosenha = tb_userpassword.query.filter_by(cod_userpassword=id).first()
    form = FormularioUsuarioSenhaEdicao()
    form.usuario.data = usuariosenha.username_userpassword
    form.senha.data = usuariosenha.password_userpassword
    form.tipo.data = usuariosenha.cod_passwordtype
    return render_template('editarUsuarioSenha.html', titulo='Editar Senha', id=id, form=form)   

# rota para atualizar usuário no banco de dados
@app.route('/atualizarUsuarioSenha', methods=['POST',])
def atualizarUsuarioSenha():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('atualizarTipoSenha')))        
    form = FormularioUsuarioSenhaEdicao(request.form)
    if form.validate_on_submit():
        id = request.form['id']
        usuariosenha = tb_userpassword.query.filter_by(cod_userpassword=id).first()
        usuariosenha.username_userpassword = form.usuario.data
        usuariosenha.password_userpassword = form.senha.data
        usuariosenha.cod_passwordtype = form.tipo.data
        db.session.add(usuariosenha)
        db.session.commit()
    return redirect(url_for('visualizarUsuarioSenha', id=id))   

 #---------------------------------------------------------------------------------------------------------------------------------
# GERADOR DE SENHA SEGURA
#---------------------------------------------------------------------------------------------------------------------------------
# rota para editar formulário tipo usuário 
@app.route('/geradorSenhaSegura/<int:id>')
def geradorSenhaSegura(tamanho_da_senha):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha_segura = ''
    for i in range(tamanho_da_senha):
        senha_segura += choice(caracteres)
    print("A senha (segura) gerada é: ",senha_segura)
    return senha_segura