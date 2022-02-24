from flask import Flask,render_template,request, redirect, url_for
import db
from models import Portafolio

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contacto", methods =["POST"])
def contactar():
    consulta = Portafolio(nombre =request.form['nombre'], email=request.form['email'], mensaje=request.form['mensaje'], asunto=request.form['asunto'])
    db.session.add(consulta)  # Añadir el objeto de Hotel a la base de datos
    db.session.commit()  # Ejecutar la operacion pendiente de la base de datos
    db.session.close()
    return redirect(url_for("home"))


@app.route("/consulta", methods =["POST"])
def consultas():
    consulta = Portafolio(nombre =request.form['nombre'], email=request.form['email'], mensaje=request.form['mensaje'], asunto=request.form['asunto'])
    db.session.add(consulta)  # Añadir el objeto de Hotel a la base de datos
    db.session.commit()  # Ejecutar la operacion pendiente de la base de datos
    db.session.close()
    return redirect(url_for("home"))

if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine) #Creamos el modelo de datos
    app.run(debug=True)