from flask import Flask, render_template, request, jsonify, json
from flask_login import login_required, login_user, logout_user, LoginManager
from models import db, Folder, File
from manager import ManagerUser, ManagerFolder, ManagerFile

from config import config, init_user

from sender_mails import send_mail

app = Flask(__name__)

app.config.from_object(config["production"])

login_manager_app = LoginManager()
login_manager_app.init_app(app)

db.init_app(app)
with app.app_context():
    db.create_all()
    init_user()
    RES_ERROR_PARAMS = jsonify(success=False, message="Error en los parametros"), 400
    
@login_manager_app.user_loader
def load_user(id_user:str):
    return ManagerUser.get_by_id(id_user)

@app.route("/")
def inicio():
    return render_template("index.html")

### SESSIONS ###

@app.route("/login", methods=["POST"])
def login():
    try:
        username = request.json["username"]
        password = request.json["password"]
        
        res_login = ManagerUser.login(username, password)
        if res_login:
            login_user(res_login)
            return jsonify(success=True, message="Inicio de sesion exitoso")
        elif res_login == False:
            return jsonify(success=False, message="Contraseña incorrecta"), 400
        elif res_login == None:
            return jsonify(success=False, message="Usuario no encontrado"), 400
        
    except Exception as e:
        print(e)
        return RES_ERROR_PARAMS

@app.route("/logout")
def logout():
    logout_user()
    return jsonify(success=True, message="Sesion cerrada")

### SESSIONS ###

### REST ###

@app.route("/api/get/main_content", methods=["GET"])
def get_main_content():
    data = []
    files:list[File] = db.session.execute(db.select(File).where(File.id_folder == None)).scalars().all()
    folders:list[Folder] = db.session.execute(db.select(Folder)).scalars().all()
    data.extend([file.to_dict() for file in files])
    data.extend([folder.to_dict() for folder in folders])
    
    return jsonify(success=True, data=data)

## FOLDER ##

@app.route("/api/get/folder/<string:id>", methods=["GET"])
def get_folder(id:str):
    folder = db.session.get(Folder, id)
    if folder:
        return jsonify(success=True, data=folder.to_dict())
    else:
        return jsonify(success=False, message="Carpeta no encontrada"), 404

@app.route("/api/create/folder", methods=["POST"])
@login_required
def create_folder():
    try:
        name = request.json["name"]
        ManagerFolder.create(name)
        return jsonify(success=True, message="Carpeta creada correctamente")
    except:
        return RES_ERROR_PARAMS

@app.route("/api/delete/folder", methods=["POST"])
@login_required
def delete_folder():
    try:
        id = request.json["id"]
        ManagerFolder.delete(id)
        return jsonify(success=True, message="Carpeta eliminada correctamente")
    except:
        return RES_ERROR_PARAMS

@app.route("/api/update/folder", methods=["POST"])
@login_required
def update_folder():
    try:
        id = request.json["id"]
        name = request.json["name"]
        ManagerFolder.update(id, name)
        return jsonify(success=True, message="Carpeta actualizada correctamente")
    except:
        return RES_ERROR_PARAMS
    
## FOLDER ##

## FILE ##

@app.route("/api/get/file/<string:id>", methods=["GET"])
def get_file(id:str):
    file = db.session.get(File, id)
    if file:
        return jsonify(success=True, data=file.to_dict())
    else:
        return jsonify(success=False, message="Archivo no encontrado"), 404

@app.route("/api/create/file", methods=["POST"])
@login_required
def create_file():
    try:
        name = request.json["name"]
        id_folder = request.json["id_folder"]
        template = request.json["template"]
        
        created = ManagerFile.create(name, id_folder, template)
        if created:
            return jsonify(success=True, message="Archivo creado correctamente")
        else:
            return jsonify(success=False, message="Error al crear el archivo"), 400
    except Exception as e:
        print(e)
        return RES_ERROR_PARAMS

@app.route("/api/delete/file", methods=["POST"])
@login_required
def delete_file():
    try:
        id = request.json["id"]
        ManagerFile.delete(id)
        return jsonify(success=True, message="Archivo eliminado correctamente")
    except:
        return RES_ERROR_PARAMS

@app.route("/api/update/file", methods=["PATCH"])
@login_required
def update_file():
    try:
        id = request.form["id"]
        name = request.form["name"]
        template = request.form["template"]
        content = json.loads(request.form["content"])
        new_images = request.files.getlist("new_images")
        delete_images = json.loads(request.form["delete_images"])
        print(id, name, template, content)
        for delete_image in delete_images:
            print(delete_image)
            
        ManagerFile.update(id, name, template, content, new_images, delete_images)
        return jsonify(success=True, message="Archivo actualizado correctamente")
    except Exception as e:
        print(e)
        return RES_ERROR_PARAMS

## FILE ##

@app.route("/api/send_mail", methods=["POST"])
def mail_sender():
    try:
        mail = request.json["mail"]
        name = request.json["name"]
        message = request.json["message"]
        send_mail(message, mail, name)
    except:
        return RES_ERROR_PARAMS
        
    return jsonify(success=True, message="Mensaje enviado correctamente")

### REST ###