from werkzeug.security import check_password_hash
import shortuuid
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, Boolean, ForeignKey, Text, JSON
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from flask_login import UserMixin

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class User(UserMixin, db.Model):
    id: Mapped[str] = mapped_column(String(30), primary_key=True, default=shortuuid.uuid)
    username: Mapped[str] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(255))

    def __init__(self, username:str, password:str):
        self.username = username
        self.password = password
    
    @classmethod
    def check_password(self, hash:str, password:str):
        return check_password_hash(hash, password)
    
class Folder(db.Model):
    id: Mapped[str] = mapped_column(String(30), primary_key=True, default=shortuuid.uuid)
    name: Mapped[str] = mapped_column(String(50))
    files: Mapped[list["File"]] = relationship("File", back_populates="folder", cascade="save-update, merge, delete")
    
    def __init__(self, name:str):
        self.name = name
    
    def add_file(self, file:"File"):
        self.files.append(file)
    
    def remove_file(self, file:"File"):
        self.files.remove(file)

    def to_dict(self):
        return {
            "id": self.id,
            "type": "folder",
            "name": self.name,
            "files": [file.to_dict() for file in self.files]
        }
        
class File(db.Model):
    id: Mapped[str] = mapped_column(String(30), primary_key=True, default=shortuuid.uuid)
    name: Mapped[str] = mapped_column(String(50))
    template: Mapped[str] = mapped_column(String(30))
    content: Mapped[dict] = mapped_column(JSON())
    id_folder: Mapped[str] = mapped_column(ForeignKey("folder.id"), nullable=True)
    folder: Mapped["Folder"] = relationship("Folder", back_populates="files")
    
    def __init__(self, name:str, template:str, content:dict, folder:Folder = None):
        self.name = name
        self.template = template
        self.content = content
        self.folder = folder
    
    def to_dict(self) -> dict[str, str]:
        return {
            "id": self.id,
            "type": "file",
            "name": self.name,
            "template": self.template,
            "content": self.content,
            "id_folder": self.id_folder
        }
    
        