from gerenciadorPassword import db


# criação da classe usuário conectada com o banco de dados mysql
class tb_user(db.Model):
    cod_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_user = db.Column(db.String(50), nullable=False)
    password_user = db.Column(db.String(50), nullable=False)
    status_user = db.Column(db.Integer, nullable=False)
    login_user = db.Column(db.String(50), nullable=False)
    cod_usertype = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

# criação da classe tipousuário conectada com o banco de dados mysql
class tb_usertype(db.Model):
    cod_usertype = db.Column(db.Integer, primary_key=True, autoincrement=True)
    desc_usertype = db.Column(db.String(50), nullable=False)
    status_usertype = db.Column(db.Integer, nullable=False)

# criação da classe beneficios conectada com o banco de dados mysql
#class tb_beneficios(db.Model):
#    cod_beneficio = db.Column(db.Integer, primary_key=True, autoincrement=True)
#    desc_beneficio = db.Column(db.String(50), nullable=False)
#    status_beneficio = db.Column(db.Integer, nullable=False)
#
#    def __repr__(self):
#        return '<Name %r>' % self.name        

# criação da classe area conectada com o banco de dados mysql
#class tb_areas(db.Model):
#    cod_area = db.Column(db.Integer, primary_key=True, autoincrement=True)
#    desc_area = db.Column(db.String(50), nullable=False)
#    status_area = db.Column(db.Integer, nullable=False)

#    def __repr__(self):
#        return '<Name %r>' % self.name   

# criação da classe tipo lancamento conectada com o banco de dados mysql
#class tb_tipolancamento(db.Model):
#    cod_tipolancamento = db.Column(db.Integer, primary_key=True, autoincrement=True)
#    desc_tipolancamento = db.Column(db.String(50), nullable=False)
#    status_tipolancamento = db.Column(db.Integer, nullable=False)
#    sigla_tipolancamento = db.Column(db.String(50), nullable=False)

#    def __repr__(self):
#        return '<Name %r>' % self.name

# criação da classe beneficio usuario conectada com o banco de dados mysql
#class tb_beneficiousuario(db.Model):
#    cod_beneficiousuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
#    cod_usuario = db.Column(db.Integer, nullable=False)
#    cod_beneficio = db.Column(db.Integer, nullable=False)

# criação da classe periodoconectada com o banco de dados mysql    
#class tb_periodos(db.Model):
#    cod_periodo = db.Column(db.Integer, primary_key=True, autoincrement=True)
#    desc_periodo = db.Column(db.String(50), nullable=False)
#    status_periodo = db.Column(db.Integer, nullable=False)
#    inicio_periodo = db.Column(db.DateTime, nullable=False)
#    final_periodo = db.Column(db.DateTime, nullable=False)

#    def __repr__(self):
#        return '<Name %r>' % self.name     

# criação da classe periodoconectada com o banco de dados mysql    
#class tb_periodofuncionario(db.Model):
#    cod_periodoFuncionario = db.Column(db.Integer, primary_key=True, autoincrement=True)
#    cod_usuario = db.Column(db.Integer, nullable=False)
#    cod_periodo = db.Column(db.Integer, nullable=False)
#    cod_tipolancamento = db.Column(db.Integer, nullable=False)
#    data_periodoFuncionario = db.Column(db.DateTime, nullable=False)

#    def __repr__(self):
#        return '<Name %r>' % self.name    
 