# importação de dependencias
from datetime import datetime
from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
import time
from datetime import date, timedelta
from gerenciadorPassword import app, db
from models import tb_user,\
     tb_usertype
#    tb_beneficios, \
#    tb_areas, \
#    tb_tipolancamento, \
#    tb_beneficiousuario,\
#    tb_periodos,\
#    tb_periodofuncionario,\
#    resultadoBuscaPeriodo
from helpers import \
    FormularPesquisa, \
    FormularioUsuario, \
    FormularioUsuarioVisualizar, \
    FormularioTipoUsuarioEdicao,\
    FormularioTipoUsuarioVisualizar    


# rota index
@app.route('/')
def index():
    #if session['usuario_logado'] == None:
    #    return redirect(url_for('login',proxima=url_for('novoUsuario')))    
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
    #proxima = request.args.get('proxima')
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
            session['tipousuario_logado'] = 1
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
    form = FormularPesquisa()
    page = request.args.get('page', 1, type=int)
    usuarios = tb_user.query\
    .join(tb_usertype, tb_usertype.cod_usertype==tb_user.cod_usertype)\
    .add_columns(tb_user.login_user, tb_user.cod_user, tb_user.name_user, tb_user.status_user, tb_usertype.desc_usertype)\
    .order_by(tb_user.name_user)\
    .paginate(page=page, per_page=5, error_out=False)
    return render_template('usuarios.html', titulo='Usuários', usuarios=usuarios, form=form)

# rota index para mostrar pesquisa usuários
@app.route('/usuarioPesquisa', methods=['POST',])
def usuarioPesquisa():
    page = request.args.get('page', 1, type=int)
    form = FormularPesquisa()
    usuarios = tb_user.query\
    .filter(tb_user.name_user.ilike(f'%{form.pesquisa.data}%'))\
    .join(tb_usertype, tb_usertype.cod_usertype==tb_user.cod_usertype)\
    .add_columns(tb_user.login_user, tb_user.cod_user, tb_user.name_user, tb_user.status_user, tb_usertype.desc_usertype)\
    .order_by(tb_user.name_user)\
    .paginate(page=page, per_page=5, error_out=False)
    return render_template('usuarios.html', titulo='Usuários' , usuarios=usuarios, form=form)

# rota para criar novo formulário usuário 
@app.route('/novoUsuario')
def novoUsuario():
    if session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('novoUsuario')))
    form = FormularioUsuario()
    return render_template('novoUsuario.html', titulo='Novo Usuário', form=form)

# rota para visualizar usuário 
@app.route('/visualizarUsuario/<int:id>')
def visualizarUsuario(id):
    if session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('visualizarUsuario')))
    usuario = tb_user.query.filter_by(cod_user=id).first()
    form = FormularioUsuarioVisualizar()
    form.nome.data = usuario.name_user
    form.status.data = usuario.status_user
    form.login.data = usuario.login_user
    form.tipousuario.data = usuario.cod_usertype
    return render_template('visualizarUsuario.html', titulo='Visualizar Usuário', id=id, form=form)   

# rota para editar formulário usuário 
@app.route('/editarUsuario/<int:id>')
def editarUsuario(id):
    if session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('visualizarUsuario')))
    usuario = tb_user.query.filter_by(cod_user=id).first()
    form = FormularioUsuario()
    form.nome.data = usuario.name_user
    form.status.data = usuario.status_user
    form.login.data = usuario.login_user
    form.tipousuario.data = usuario.cod_usertype
    return render_template('editarUsuario.html', titulo='Editar Usuário', id=id, form=form)    
       
# rota para criar usuário no banco de dados
@app.route('/criarUsuario', methods=['POST',])
def criarUsuario():
    form = FormularioUsuario(request.form)
    if not form.validate_on_submit():
        return redirect(url_for('novo'))
    nome  = form.nome.data
    status = form.status.data
    login = form.login.data
    tipousuario = form.tipousuario.data
    usuario = tb_user.query.filter_by(name_user=nome).first()
    if usuario:
        flash ('Usuário já existe')
        return redirect(url_for('index')) 
    novoUsuario = tb_user(nome_user=nome, status_user=status, login_user=login, cod_usertype=tipousuario)
    db.session.add(novoUsuario)
    db.session.commit()

    #arquivo = request.files['arquivo']
    #uploads_path = app.config['UPLOAD_PATH']
    #timestamp = time.time
    #deleta_arquivos(usuario.cod_usuario)
    #arquivo.save(f'{uploads_path}/foto{usuario.cod_usuario}-{timestamp}.jpg')

#    return redirect(url_for('usuario'))

# rota para atualizar usuário no banco de dados
@app.route('/atualizarUsuario', methods=['POST',])
def atualizarUsuario():
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
    page = request.args.get('page', 1, type=int)
    form = FormularPesquisa()    
    tiposusuario = tb_usertype.query.order_by(tb_usertype.desc_usertype)\
    .paginate(page=page, per_page=5, error_out=False)
    return render_template('tipousuarios.html', titulo='Tipo Usuário', tiposusuario=tiposusuario, form=form)

# rota index para mostrar pesquisa dos tipo usuários
@app.route('/tipousuarioPesquisa', methods=['POST',])
def tipousuarioPesquisa():
    page = request.args.get('page', 1, type=int)
    form = FormularPesquisa()
    tiposusuario = tb_usertype.query.order_by(tb_usertype.desc_usertype)\
    .filter(tb_usertype.desc_usertype.ilike(f'%{form.pesquisa.data}%'))\
    .paginate(page=page, per_page=5, error_out=False)
    return render_template('tipousuarios.html', titulo='Tipo Usuário' , tiposusuario=tiposusuario, form=form)    

# rota para criar novo formulário usuário 
@app.route('/novoTipoUsuario')
def novoTipoUsuario():
    if session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('novoTipoUsuario')))
    form = FormularioTipoUsuarioEdicao()
    return render_template('novoTipoUsuario.html', titulo='Novo Tipo Usuário', form=form)

# rota para criar tipo usuário no banco de dados
@app.route('/criarTipoUsuario', methods=['POST',])
def criarTipoUsuario():
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
    if session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('visualizarTipoUsuario')))
    tipousuario = tb_usertype.query.filter_by(cod_usertype=id).first()
    form = FormularioTipoUsuarioVisualizar()
    form.descricao.data = tipousuario.desc_usertype
    form.status.data = tipousuario.status_usertype
    return render_template('visualizarTipoUsuario.html', titulo='Visualizar Tipo Usuário', id=id, form=form)   

# rota para editar formulário tipo usuário 
@app.route('/editarTipoUsuario/<int:id>')
def editarTipoUsuario(id):
    if session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('visualizarTipoUsuario')))
    tipousuario = tb_usertype.query.filter_by(cod_usertype=id).first()
    form = FormularioTipoUsuarioEdicao()
    form.descricao.data = tipousuario.desc_usertype
    form.status.data = tipousuario.status_usertype
    return render_template('editarTipoUsuario.html', titulo='Editar Tipo Usuário', id=id, form=form)   

# rota para atualizar usuário no banco de dados
@app.route('/atualizarTipoUsuario', methods=['POST',])
def atualizarTipoUsuario():
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
#BENEFICIOS
#---------------------------------------------------------------------------------------------------------------------------------
# rota index para mostrar os beneficios
#@app.route('/beneficio')
#def beneficio():
#    page = request.args.get('page', 1, type=int)
#    form = FormularPesquisa()    
#    beneficios = tb_beneficios.query.order_by(tb_beneficios.desc_beneficio)\
#    .paginate(page=page, per_page=5, error_out=False)
#    return render_template('beneficios.html', titulo='Beneficios', beneficios=beneficios, form=form)

# rota index para pesquisar os beneficios
#@app.route('/beneficioPesquisa', methods=['POST',])
#def beneficioPesquisa():
#    page = request.args.get('page', 1, type=int)
#    form = FormularPesquisa()
#    lista = tb_beneficios.query.order_by(tb_beneficios.desc_beneficio)\
#    .filter(tb_beneficios.desc_beneficio.ilike(f'%{form.pesquisa.data}%'))\
#    .paginate(page=page, per_page=5, error_out=False)
#    return render_template('beneficios.html', titulo='Benefícios' , lista=lista, form=form)
