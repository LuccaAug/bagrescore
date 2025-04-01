from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os

from . import db, app
from .models import Usuario, Jogador

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario = Usuario.query.filter_by(email=email).first()
        if not usuario:
            flash('Verifique o email e senha e tente novamente', category='error')
        elif not check_password_hash(usuario.senha, senha):
            flash('Verifique o email e senha e tente novamente', category='error')
        else:
            login_user(usuario, remember=True)
            flash('Seja bem-vindo novamente bagre!', category='succes')
            return redirect(url_for('views.home'))

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.logout'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email').lower()
        senha = request.form.get('senha')
        senha_confirmacao = request.form.get('senha_confirmacao')

        nome = request.form.get('nome').title()
        vulgo = request.form.get('vulgo')
        numero = request.form.get('numero')
        insta = request.form.get('insta')
        insta = request.form.get('insta')

        usuario = Usuario.query.filter_by(email=email).first()
        jogador = Jogador.query.filter_by(vulgo=vulgo).first()
        if usuario:
            flash('Email já cadastrado', category='error')
            print(usuario)
        # elif jogador:
        #     flash('Vulgo já cadastrado', category='error')
        #     print(jogador)
        # elif len(email) == 0:
        #     flash('Informe um email válido', category='error')
        # elif len(senha) < 5:
        #     flash('A senha precisa ter pelo menos 5 dígitos', category='error')
        # elif senha != senha_confirmacao:
        #     flash('As senhas digitadas não estão iguais', category='error')
        # elif len(nome) < 4:
        #     flash('O nome precisa ter pelo menos 4 dígitos', category='error')
        # elif len(vulgo) < 2:
        #     flash('O vulgo precisa ter pelo menos 2 dígitos', category='error')
        # elif int(numero) < 0 and int(numero) > 999:
        #     flash('O número deve ter no máximo 3 dígitos e ser positivo', category='error')
        else:
            path_imagem = None
            print("Request files: ", request.files)
            if "imagem" in request.files:
                file = request.files["imagem"]
                if file.filename != "":
                    filename = secure_filename(file.filename)
                    path_imagem = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                    file.save(path_imagem)
                print(path_imagem, file)

            novo_jogador = Jogador(
                nome=nome,
                vulgo=vulgo,
                numero=int(numero),
                insta=insta,
                imagem=path_imagem,
            )
            db.session.add(novo_jogador)
            novo_usuario = Usuario(
                email=email,
                senha=generate_password_hash(senha, method='pbkdf2:sha256'),
                jogador_id=novo_jogador.id,
            )
            db.session.add(novo_usuario)
            db.session.commit()
            login_user(novo_usuario, remember=True)
            flash('Parabéns, agora você é um bagre!', category='succes')

            return redirect(url_for('views.home'))

    return render_template("sign-up.html", user=current_user)