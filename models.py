from gerenciadorPassword import db

# criação da classe usuário conectada com o banco de dados mysql
class tb_user(db.Model):
    cod_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_user = db.Column(db.String(50), nullable=False)
    password_user = db.Column(db.String(50), nullable=False)
    status_user = db.Column(db.Integer, nullable=False)
    login_user = db.Column(db.String(50), nullable=False)
    cod_usertype = db.Column(db.Integer, nullable=False)
    email_user = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

# criação da classe tipousuário conectada com o banco de dados mysql
class tb_usertype(db.Model):
    cod_usertype = db.Column(db.Integer, primary_key=True, autoincrement=True)
    desc_usertype = db.Column(db.String(50), nullable=False)
    status_usertype = db.Column(db.Integer, nullable=False)

# criação da classe tipo de senha conectada com o banco de dados mysql
class tb_passwordtype(db.Model):
    cod_passwordtype = db.Column(db.Integer, primary_key=True, autoincrement=True)
    desc_passwordtype = db.Column(db.String(50), nullable=False)
    status_passwordtype = db.Column(db.Integer, nullable=False)
    icon_passwordtype = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name        

# criação da classe area conectada com o banco de dados mysql
class tb_userpassword(db.Model):
    cod_userpassword = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cod_passwordtype = db.Column(db.Integer, nullable=False)
    username_userpassword = db.Column(db.String(50), nullable=False)
    password_userpassword = db.Column(db.String(50), nullable=False)
    date_userpassword = db.Column(db.DateTime, nullable=False)
    cod_user = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name   

