from werkzeug.security import generate_password_hash
from models import db, User, Folder, File
from sqlalchemy.orm.attributes import flag_modified
import shortuuid
import os
import shutil
from config import config

class ManagerUser():
    @classmethod
    def get_by_id(self, id:str):
        user = db.session.get(User, id)
        # if user:
        #     user.password = True
        return user
    
    @classmethod
    def register(self, username:str, password:str):
        user = User(username, generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
    
    @classmethod
    def login(self, username:str, password:str):
        user:User | None = db.session.execute(db.select(User).where(User.username == username)).scalar()
        
        if user:
            if User.check_password(user.password, password):
                user.password = True
                return user
            else:
                return False
        else:
            return None
    
    @classmethod
    def valid_username(self, username:str):
        user:User = db.session.execute(db.select(User).where(User.username == username)).scalar()
        
        return False if user else True


class ManagerFolder():
    @classmethod
    def create(self, name:str):
        folder = Folder(name)
        db.session.add(folder)
        db.session.commit()

    @classmethod
    def delete(self, id:str):
        folder = db.session.get(Folder, id)
        if folder:
            for file in folder.files:
                if os.path.exists(os.path.join(config["production"].IMG_PATH, file.name)):
                    shutil.rmtree(os.path.join(config["production"].IMG_PATH, file.name))
            
            db.session.delete(folder)
            db.session.commit()
    
    @classmethod
    def update(self, id:str, name:str):
        folder = db.session.get(Folder, id)
        if folder:
            folder.name = name
            db.session.commit()
            
class ManagerFile():
    @classmethod
    def create(self, name:str, id_folder:str, template:str):
        init_content = {}
        if template == "blank":
            init_content = {"":""}
        elif template == "project":
            init_content = {"name": "", "description": "", "technologys": [], "images": [], "url": ""}
        file = File(name, template, init_content)
        if id_folder:
            folder = db.session.get(Folder, id_folder)
            if folder:
                file.folder = folder
            else:
                return False
            
        db.session.add(file)
        db.session.commit()
        return True
        
            

    @classmethod
    def delete(self, id:str):
        file = db.session.get(File, id)
        if file:
            if os.path.exists(os.path.join(config["production"].IMG_PATH, file.name)):
                shutil.rmtree(os.path.join(config["production"].IMG_PATH, file.name))
            db.session.delete(file)
            db.session.commit()
    
    @classmethod
    def update(self, id:str, name:str, template:str, content:dict, new_images = [], delete_images = []):
        file = db.session.get(File, id)
        if file:
            if name: 
                if file.name in os.listdir(os.path.join(config["production"].IMG_PATH)):
                    os.rename(os.path.join(config["production"].IMG_PATH, file.name), os.path.join(config["production"].IMG_PATH, name))
                file.name = name
                 
            if template: file.template = template
            
            if new_images:
                new_images_names = self.save_imgs(new_images, file.name)
                if not "images" in file.content:
                    file.content["images"] = []
                    
                file.content["images"].extend(new_images_names)
                flag_modified(file, "content")
            
            if delete_images:
                actual_images = file.content["images"]
                for delete_image in delete_images:
                    actual_images.remove(delete_image)
                file.content["images"] = actual_images
                flag_modified(file, "content")
                self.delete_imgs(delete_images, file.name)
                
            
            if file.template == "project":
                if "name" in content: 
                    if content["name"]:
                        file.content["name"] = content["name"]
                        flag_modified(file, "content")
                if "description" in content: 
                    if content["description"]:
                        file.content["description"] = content["description"]
                        flag_modified(file, "content")
                if "technologys" in content:
                    if content["technologys"]:
                        file.content["technologys"] = content["technologys"]
                        flag_modified(file, "content")
                if "images" in content:
                    if content["images"]:
                        pass
                if "url" in content:
                    if content["url"]:
                        if content["url"] == ".": content["url"] = ""
                        file.content["url"] = content["url"]
                        flag_modified(file, "content")
                
            elif file.template == "blank":
                if "" in content: 
                    if content[""]:            
                        file.content[""] = content[""]
                        flag_modified(file, "content")
                
            db.session.commit()
    
    @classmethod
    def save_imgs(self, imgs: list, dirname: str):
        """
        Retorna una lista con los nuevos nombres de las imagenes
        """
        imgs_names = []
        
        if not os.path.exists(os.path.join(config["production"].IMG_PATH, dirname)):
            os.mkdir(os.path.join(config["production"].IMG_PATH, dirname))
            
        for img in imgs:
            ext = img.filename.split('.')[-1]
            filename = shortuuid.uuid()
            img_name = f"{filename}.{ext}".replace('\\', '/')
            img.save(os.path.join(config["production"].IMG_PATH, dirname, img_name))
            imgs_names.append(img_name)
            
        return imgs_names
    
    @classmethod
    def delete_imgs(self, img_names: list, dirname: str):
        for img_name in img_names:
            abs_img_path = os.path.join(config["production"].IMG_PATH, dirname, img_name)
            if os.path.exists(abs_img_path):
                os.remove(abs_img_path)
        
            

def get_main_content():
    data = []
    files:list[File] = db.session.execute(db.select(File).where(File.id_folder == None)).scalars().all()
    return files