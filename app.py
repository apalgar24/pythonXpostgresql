#app.py
from flask import Flask, request, session, redirect, url_for, render_template, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
import re 
from werkzeug.security import generate_password_hash, check_password_hash
 
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("index.html") 
@app.route('/login',methods=['POST'])
def login():
    from flask import request
    usuario=request.form.get("usuario")
    contraseña=request.form.get("contraseña")
    db=request.form.get("db")
    conn = psycopg2.connect(dbname=db, user=usuario, password=contraseña, host="localhost")
    cur = conn.cursor()
    cur.execute("SELECT gestor FROM gestores;")
    gestores = cur.fetchall()
    ids=[]
    for gestor in gestores:
        ids.append(gestor[0])
    return render_template("login.html",ids=ids)
