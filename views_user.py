from jogoteca import app
from helpers import FormularioUser
from flask import redirect,render_template, request,session, flash, url_for
from models import Usuarios
from flask_bcrypt import check_password_hash

@app.route('/login')
def login():
    form = FormularioUser()
    proxima = request.args.get('proxima')
    return render_template('/login.html', proxima = proxima, form=form)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    form = FormularioUser(request.form)
    usuario = Usuarios.query.filter_by(nickname = form.nickname.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario and senha:
        session['usuario_logado'] = usuario.nickname
        flash(usuario.nickname.capitalize() + ' logado com sucesso !')
        proxima_pagina= request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Usuário não logado')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso !')
    return redirect(url_for('index'))
