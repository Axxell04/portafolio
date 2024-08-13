import os
from dotenv import load_dotenv, set_key, dotenv_values, get_key
import sqlite3

load_dotenv()

class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_SAMESITE = 'None'
    MAIN_PATH = os.path.dirname(os.path.abspath(__file__))
    STATIC_PATH = os.path.join(MAIN_PATH, "static")
    IMG_PATH = os.path.join(STATIC_PATH, "img")

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}


def init_user():
    try:
        user_created = bool(int(get_key(".env", "USER_CREATED")))
        if user_created:
            return
        
        db = sqlite3.connect(os.path.join(Config.MAIN_PATH, "instance", "portafolio.db"))
        with db:
            cursor = db.cursor()
            id_admin = os.environ.get("ID_ADMIN")
            username_admin = os.environ.get("USERNAME_ADMIN")
            password_admin = os.environ.get("PASSWORD_ADMIN")
            params = (id_admin, username_admin, password_admin)
            cursor.execute("INSERT INTO user (id, username, password) VALUES (?,?,?)", params)
            db.commit()
            set_key(".env", "USER_CREATED", "1")
        return True
    except Exception as e:
        print(e)
        return False