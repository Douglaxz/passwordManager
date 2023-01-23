# importação de dependencias
from datetime import datetime
from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
import time
from datetime import date, timedelta
from gerenciadorPassword import app, db
#from models import tb_usuarios, \
#    tb_tipousuario, \
#    tb_beneficios, \
#    tb_areas, \
#    tb_tipolancamento, \
#    tb_beneficiousuario,\
#    tb_periodos,\
#    tb_periodofuncionario,\
#    resultadoBuscaPeriodo
#from helpers import recupera_imagem,deleta_arquivos, \
#    FormularioPeriodoEdicao, \
#    FormularioPeriodoVisualizar, \
#    FormularioBeneficioUsuarioVisualizacao, \
#    FormularioBeneficioUsuarioEdicao, \
#    FormularPesquisa, \
#    FormularioUsuario, \
#    FormularioUsuarioVisualizar, \
#    FormularioTipoUsuarioEdicao,\
#    FormularioTipoUsuarioVisualizar, \
#    FormularioBeneficiosEdicao, \
#    FormularioBeneficiosVisualizar, \
#    FormularioAreaEdicao,\
#    FormularioAreaVisualizar,\
#    FormularioTipoLancamentoVisualizar,\
#    FormularioTipoLancamentoEdicao,\
#    FormularioLancamentoVisualizar,\
#    FormularioLancamentoEdicao,\
#    FormularioPesquisaPeriodo
    


# rota template
@app.route('/template')
def index():
    return render_template('template.html', titulo='Bem vindos')

# rota index
#@app.route('/')
#def index():
#    #if session['usuario_logado'] == None:
#    #    return redirect(url_for('login',proxima=url_for('novoUsuario')))    
#    return render_template('index.html', titulo='Bem vindos')

# rota logout
#@app.route('/logout', methods = ['GET', 'POST'])
#def logout():
#    session['usuario_logado'] = None
#    flash('logout efetuado com sucesso')
#    return redirect(url_for('login'))

 #rota para a tela de login
@app.route('/login')
def login():
    #proxima = request.args.get('proxima')
    return render_template('login.html')

# rota para autendicar a tela de login
@app.route('/autenticar', methods = ['GET', 'POST'])
def autenticar():
    usuario = tb_usuarios.query.filter_by(login_usuario=request.form['usuario']).first()
    if usuario:
        if request.form['senha'] == usuario.senha_usuario:
            session['usuario_logado'] = usuario.login_usuario
            session['nomeusuario_logado'] = usuario.nome_usuario
            session['tipousuario_logado'] = usuario.cod_tipousuario
            flash(usuario.nome_usuario + ' Usuário logado com sucesso')
            proximaPagina = request.form['proxima']
            if proximaPagina == "None":
                proximaPagina = ''
            return redirect('/{}'.format(proximaPagina))
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
#@app.route('/usuario')
#def usuario():
#    form = FormularPesquisa()
#    page = request.args.get('page', 1, type=int)
#    usuarios = tb_usuarios.query\
#    .join(tb_areas, tb_areas.cod_area==tb_usuarios.cod_area)\
#    .join(tb_tipousuario, tb_tipousuario.cod_tipousuario==tb_usuarios.cod_tipousuario)\
#    .add_columns(tb_usuarios.login_usuario, tb_usuarios.cod_usuario, tb_usuarios.nome_usuario, tb_usuarios.status_usuario, tb_areas.desc_area, tb_tipousuario.desc_tipousuario)\
#    .order_by(tb_usuarios.nome_usuario)\
#    .paginate(page=page, per_page=5, error_out=False)
#    return render_template('usuarios.html', titulo='Usuários', usuarios=usuarios, form=form)

# rota index para mostrar pesquisa usuários
#@app.route('/usuarioPesquisa', methods=['POST',])
#def usuarioPesquisa():
#    page = request.args.get('page', 1, type=int)
#    form = FormularPesquisa()
#    usuarios = tb_usuarios.query\
#    .filter(tb_usuarios.nome_usuario.ilike(f'%{form.pesquisa.data}%'))\
#    .join(tb_areas, tb_areas.cod_area==tb_usuarios.cod_area)\
#    .join(tb_tipousuario, tb_tipousuario.cod_tipousuario==tb_usuarios.cod_tipousuario)\
#    .add_columns(tb_usuarios.login_usuario, tb_usuarios.cod_usuario, tb_usuarios.nome_usuario, tb_usuarios.status_usuario, tb_areas.desc_area, tb_tipousuario.desc_tipousuario)\
#    .order_by(tb_usuarios.nome_usuario)\
#    .paginate(page=page, per_page=5, error_out=False)
#    return render_template('usuarios.html', titulo='Usuários' , usuarios=usuarios, form=form)

# rota para criar novo formulário usuário 
#@app.route('/novoUsuario')
#def novoUsuario():
#    if session['usuario_logado'] == None:
#        return redirect(url_for('login',proxima=url_for('novoUsuario')))
#    form = FormularioUsuario()
#    return render_template('novoUsuario.html', titulo='Novo Usuário', form=form)

# rota para visualizar usuário 
#@app.route('/visualizarUsuario/<int:id>')
#def visualizarUsuario(id):
#    if session['usuario_logado'] == None:
#        return redirect(url_for('login',proxima=url_for('visualizarUsuario')))
#    usuario = tb_usuarios.query.filter_by(cod_usuario=id).first()
#    form = FormularioUsuarioVisualizar()
#    form.nome.data = usuario.nome_usuario
#    form.senha.data = usuario.senha_usuario
#    form.status.data = usuario.status_usuario
#    form.login.data = usuario.login_usuario
#    form.tipousuario.data = usuario.cod_tipousuario
#    form.area.data = usuario.cod_area
#    form1 = FormularioBeneficioUsuarioVisualizacao()
#    beneficiosusuario = tb_beneficiousuario.query.filter_by(cod_usuario=id)\
#        .join(tb_beneficios, tb_beneficios.cod_beneficio==tb_beneficiousuario.cod_beneficio)\
#        .add_columns(tb_beneficios.desc_beneficio,tb_beneficiousuario.cod_beneficiousuario)
 #   return render_template('visualizarUsuario.html', titulo='Visualizar Usuário', id=id, form=form, form1=form1, beneficiosusuario=beneficiosusuario)   

# rota para editar formulário usuário 
#@app.route('/editarUsuario/<int:id>')
#def editarUsuario(id):
#    if session['usuario_logado'] == None:
#        return redirect(url_for('login',proxima=url_for('visualizarUsuario')))
#    usuario = tb_usuarios.query.filter_by(cod_usuario=id).first()
#    form = FormularioUsuario()
#    form.nome.data = usuario.nome_usuario
#    form.senha.data = usuario.senha_usuario
#    form.status.data = usuario.status_usuario
#    form.login.data = usuario.login_usuario
#    form.tipousuario.data = usuario.cod_tipousuario
#    form.area.data = usuario.cod_area
#    return render_template('editarUsuario.html', titulo='Editar Usuário', id=id, form=form)    
       
# rota para criar usuário no banco de dados
#@app.route('/criar', methods=['POST',])
#def criar():
#    form = FormularioUsuario(request.form)
#    if not form.validate_on_submit():
#        return redirect(url_for('novo'))
#    nome  = form.nome.data
#    senha = form.senha.data
#    status = form.status.data
#    login = form.login.data
#    tipousuario = form.tipousuario.data
#    area = form.area.data
#    usuario = tb_usuarios.query.filter_by(nome_usuario=nome).first()
#    if usuario:
#        flash ('Usuário já existe')
#        return redirect(url_for('index')) 
#    novoUsuario = tb_usuarios(nome_usuario=nome, senha_usuario=senha, status_usuario=status, login_usuario=login, cod_tipousuario=tipousuario, cod_area=area)
#    db.session.add(novoUsuario)
#    db.session.commit()

    #arquivo = request.files['arquivo']
    #uploads_path = app.config['UPLOAD_PATH']
    #timestamp = time.time
    #deleta_arquivos(usuario.cod_usuario)
    #arquivo.save(f'{uploads_path}/foto{usuario.cod_usuario}-{timestamp}.jpg')

#    return redirect(url_for('usuario'))

# rota para atualizar usuário no banco de dados
#@app.route('/atualizarUsuario', methods=['POST',])
#def atualizarUsuario():
#    form = FormularioUsuario(request.form)
#    if form.validate_on_submit():
#        id = request.form['id']
#        usuario = tb_usuarios.query.filter_by(cod_usuario=request.form['id']).first()
#        usuario.nome_usuario = form.nome.data
#        usuario.senha_usuario = form.senha.data
#        usuario.status_usuario = form.status.data
#        usuario.login_usuario = form.login.data
#        usuario.cod_tipousuario = form.tipousuario.data
#        usuario.cod_area = form.area.data
#        db.session.add(usuario)
#        db.session.commit()
#    return redirect(url_for('visualizarUsuario', id=id))

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
#@app.route('/tipousuario')
#def tipousuario():
#    page = request.args.get('page', 1, type=int)
#    form = FormularPesquisa()    
#    tiposusuario = tb_tipousuario.query.order_by(tb_tipousuario.cod_tipousuario)\
#    .paginate(page=page, per_page=5, error_out=False)
#    return render_template('tipousuarios.html', titulo='Tipo Usuários', tiposusuario=tiposusuario, form=form)

# rota index para mostrar pesquisa dos tipo usuários
#@app.route('/tipousuarioPesquisa', methods=['POST',])
#def tipousuarioPesquisa():
#    page = request.args.get('page', 1, type=int)
#    form = FormularPesquisa()
#    tiposusuario = tb_tipousuario.query.order_by(tb_tipousuario.desc_tipousuario)\
#    .filter(tb_tipousuario.desc_tipousuario.ilike(f'%{form.pesquisa.data}%'))\
#    .paginate(page=page, per_page=5, error_out=False)
#    return render_template('tipousuarios.html', titulo='Tipo Usuários' , tiposusuario=tiposusuario, form=form)    

# rota para criar novo formulário usuário 
#@app.route('/novoTipoUsuario')
#def novoTipoUsuario():
#    if session['usuario_logado'] == None:
#        return redirect(url_for('login',proxima=url_for('novoTipoUsuario')))
#    form = FormularioTipoUsuarioEdicao()
#    return render_template('novoTipoUsuario.html', titulo='Novo Tipo Usuário', form=form)

# rota para criar tipo usuário no banco de dados
#@app.route('/criarTipoUsuario', methods=['POST',])
#def criarTipoUsuario():
#    form = FormularioTipoUsuarioEdicao(request.form)
#    if not form.validate_on_submit():
#        return redirect(url_for('criarTipoUsuario'))
#    desc  = form.descricao.data
#    status = form.status.data
#    tipousuario = tb_tipousuario.query.filter_by(desc_tipousuario=desc).first()
#    if tipousuario:
#        flash ('Tipo Usuário já existe')
#        return redirect(url_for('tipousuario')) 
#    novoTipoUsuario = tb_tipousuario(desc_tipousuario=desc, status_tipousuario=status)
#    db.session.add(novoTipoUsuario)
#    db.session.commit()
#    return redirect(url_for('tipousuario'))

# rota para visualizar tipo usuário 
#@app.route('/visualizarTipoUsuario/<int:id>')
#def visualizarTipoUsuario(id):
#    if session['usuario_logado'] == None:
#        return redirect(url_for('login',proxima=url_for('visualizarTipoUsuario')))
#    tipousuario = tb_tipousuario.query.filter_by(cod_tipousuario=id).first()
#    form = FormularioTipoUsuarioVisualizar()
#    form.descricao.data = tipousuario.desc_tipousuario
#    form.status.data = tipousuario.status_tipousuario
#    return render_template('visualizarTipoUsuario.html', titulo='Visualizar Tipo Usuário', id=id, form=form)   

# rota para editar formulário tipo usuário 
#@app.route('/editarTipoUsuario/<int:id>')
#def editarTipoUsuario(id):
#    if session['usuario_logado'] == None:
#        return redirect(url_for('login',proxima=url_for('visualizarTipoUsuario')))
#    tipousuario = tb_tipousuario.query.filter_by(cod_tipousuario=id).first()
#    form = FormularioTipoUsuarioEdicao()
#    form.descricao.data = tipousuario.desc_tipousuario
#    form.status.data = tipousuario.status_tipousuario
#    return render_template('editarTipoUsuario.html', titulo='Editar Tipo Usuário', id=id, form=form)   

# rota para atualizar usuário no banco de dados
#@app.route('/atualizarTipoUsuario', methods=['POST',])
#def atualizarTipoUsuario():
#    form = FormularioTipoUsuarioEdicao(request.form)
#    if form.validate_on_submit():
#        id = request.form['id']
#        tipousuario = tb_tipousuario.query.filter_by(cod_tipousuario=request.form['id']).first()
#        tipousuario.desc_tipousuario = form.descricao.data
#        tipousuario.status_tipousuario = form.status.data
#        db.session.add(tipousuario)
#        db.session.commit()
#    return redirect(url_for('visualizarTipoUsuario', id=id))    

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
