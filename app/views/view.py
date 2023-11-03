from flask import (
    jsonify,
    render_template,
    request,
)

from app import app, db
from werkzeug.security import( 
    generate_password_hash, 
    check_password_hash
)
from app.models.models import (
    User,
    Post,
    Coment,
    Category
)
from app.schemas.schema import (
    PostSchema,
    UserSchema,
    ComentSchema,
    CategorySchema
)
from flask.views import MethodView

@app.route('/')
def index():
    return render_template('index.html')

class UserApi(MethodView):
    def get(self,user_id=None):
        if user_id is None:
            users = User.query.all()
            users_schema = UserSchema().dump(users, many=True)
            return jsonify(users_schema)
        
        user=User.query.get(user_id)
        user_schema= UserSchema().dump(user)
        return jsonify(user_schema)
    def post(self):
        data = request.get_json()
        name = data.get('name')
        correo = data.get('correo')
        password = data.get('password')

        password_hasheada=generate_password_hash(
        password=password,
        method="pbkdf2",
        salt_length=8
        )

        new_user = User(
            name=name,
            correo=correo,
            password=password_hasheada,
        )
        db.session.add(new_user)
        db.session.commit()

        return jsonify(MENSAJE=f"Se creo el usuario {name}")
    
    def put(self, user_id=None):
        if user_id is None:
            return jsonify(MENSAJE=f"Pasame un id para saber que actualizo")
        user =User.query.get(user_id) 

        data =request.get_json()
        #Para poder cambiar de nombre y contraseña tenes que poner los datos viejos tambien
        viejo_nombre_usuario=data.get("old_name")
        vieja_contraseña=data.get("old_password")

        if (viejo_nombre_usuario == user.name) and (check_password_hash(user.password,vieja_contraseña) == True):
            nuevo_nombre_de_usuario= data.get("new_name") 
            nueva_contraseña_de_usuario=data.get("new_password")

            password_hasheada=generate_password_hash(
            password=nueva_contraseña_de_usuario,
            method="pbkdf2",
            salt_length=8
            )

            user.name = nuevo_nombre_de_usuario
            user.password= password_hasheada
            db.session.commit()

            user_shema=UserSchema().dump(user)

            return jsonify(user_shema)
        else: return jsonify("su nombre o contraseña actuales no coinciden o no las esta cargando,por favor ingrese los datos correctos para poder actualizarlos")
    
    def delete(self,user_id=None):
        if user_id is None:
            return jsonify(MENSAJE=f"Pasame un id para saber que elimino")
        user =User.query.get(user_id)
        data =request.get_json()

        nombre_usuario=data.get("name")
        contraseña=data.get("password")

        if (nombre_usuario == user.name) and (check_password_hash(user.password,contraseña) == True):      
            #Elimino usuario
            db.session.delete(user)
            db.session.commit()
            return jsonify(Mensaje=f"El user:  {user_id} fue eliminado ")
        else: return jsonify("su nombre o contraseña no coinciden o no las esta cargando,por favor ingrese los datos correctos para poder eliminar su usuario")
    
# Registro url para aceder a la clase
app.add_url_rule("/user",view_func=UserApi.as_view("user"))
app.add_url_rule("/user/<user_id>",view_func=UserApi.as_view("user_by_id"))

class PostApi(MethodView):
    def get(self,post_id=None):
        if post_id is None:
            posts = Post.query.all()
            posts_schema = PostSchema().dump(posts, many=True)
            return jsonify(posts_schema)
        
        post=Post.query.get(post_id)
        post_schema= UserSchema().dump(post)
        return jsonify(post_schema)
    def post(self):
        data = request.get_json()
        title = data.get('title')
        content = data.get('content')
        user = data.get("user")
        category= data.get("category")

        new_post = Post(
            title=title,
            content=content,
            user=user,
            category=category
        )
        db.session.add(new_post)
        db.session.commit()

        return jsonify(MENSAJE=f"Se creo el post de titulo: {title}")
    
    def put(self, post_id=None):
        if post_id is None:
            return{"Mensaje":"Pasame un id para saber que actualizo"}
        post =Post.query.get(post_id) 

        data =request.get_json()
        nuevo_titulo_del_post= data.get("title") 
        nuevo_contenido_del_post = data.get("content")

        post.title = nuevo_titulo_del_post
        post.content=nuevo_contenido_del_post
        db.session.commit()

        post_shema=PostSchema().dump(post)

        return jsonify(post_shema)
    
    def delete(self,post_id=None):
        if post_id is None:
            return{"Mensaje":"Pasame un id para saber que elimino"}
        post =Post.query.get(post_id) 
        #Elimino usuario
        db.session.delete(post)
        db.session.commit()
        return jsonify(Mensaje=f"El post:  {post_id} fue eliminado ")
    
# Registro url para aceder a la clase
app.add_url_rule("/post",view_func=PostApi.as_view("post"))
app.add_url_rule("/post/<post_id>",view_func=PostApi.as_view("post_by_id"))

class ComentApi(MethodView):
    def get(self,coment_id=None):
        if coment_id is None:
            coments = Coment.query.all()
            coments_schema = ComentSchema().dump(coments, many=True)
            return jsonify(coments_schema)
        
        coment=Coment.query.get(coment_id)
        coment_schema= ComentSchema().dump(coment)
        return jsonify(coment_schema)
    def post(self):
        data = request.get_json()
        coment = data.get('coment')
        user = data.get("user")
        post= data.get("post")

        new_coment = Coment(
            coment=coment,
            user=user,
            post=post
        )
        db.session.add(new_coment)
        db.session.commit()

        return jsonify(MENSAJE=f"Se creo comentario:  {coment}")
    
    def put(self, coment_id=None):
        if coment_id is None:
            return{"Mensaje":"Pasame un id para saber que actualizo"}
        coment =Coment.query.get(coment_id) 

        data =request.get_json()
        nuevo_contenido_del_comentario= data.get("coment") 
        

        coment.coment = nuevo_contenido_del_comentario
        db.session.commit()

        coment_shema=ComentSchema().dump(coment)

        return jsonify(coment_shema)
    
    def delete(self,coment_id=None):
        if coment_id is None:
            return{"Mensaje":"Pasame un id para saber que elimino"}
        coment =Coment.query.get(coment_id) 
        #Elimino usuario
        db.session.delete(coment)
        db.session.commit()
        return jsonify(Mensaje=f"El comentario : {coment_id} fue eliminado ")
    
# Registro url para aceder a la clase
app.add_url_rule("/coment",view_func=ComentApi.as_view("coment"))
app.add_url_rule("/coment/<coment_id>",view_func=ComentApi.as_view("coment_by_id"))

class CategoryApi(MethodView):
    def get(self,category_id=None):
        if category_id is None:
            categorys = Category.query.all()
            categorys_schema = CategorySchema().dump(categorys, many=True)
            return jsonify(categorys_schema)
        
        category=Category.query.get(category_id)
        category_schema= CategorySchema().dump(category)
        return jsonify(category_schema)
    def post(self):
        data = request.get_json()
        etiqueta = data.get('etiqueta')
        
        new_category = Category(
            etiqueta=etiqueta,
        )
        db.session.add(new_category)
        db.session.commit()

        return jsonify(MENSAJE=f"Se creo la categoria:  {etiqueta}")
    
    def put(self, category_id=None):
        if category_id is None:
            return{"Mensaje":"Pasame un id para saber que actualizo"}
        category =Category.query.get(category_id) 

        data =request.get_json()
        nuevo_contenido_de_etiqueta= data.get("etiqueta") 
        

        category.etiqueta = nuevo_contenido_de_etiqueta
        db.session.commit()

        category_shema=CategorySchema().dump(category)

        return jsonify(category_shema)
    
    def delete(self,category_id=None):
        if category_id is None:
            return{"Mensaje":"Pasame un id para saber que elimino"}
        category =Category.query.get(category_id) 
        #Elimino usuario
        db.session.delete(category)
        db.session.commit()
        return jsonify(Mensaje=f"La categoria : {category_id} fue eliminada ")
    
# Registro url para aceder a la clase
app.add_url_rule("/category",view_func=CategoryApi.as_view("category"))
app.add_url_rule("/category/<category_id>",view_func=CategoryApi.as_view("category_by_id"))

