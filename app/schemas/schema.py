from app import ma
from marshmallow import fields


class PostSchema(ma.Schema):
    id =  fields.Integer(dump_only=True)
    title = fields.String()
    content = fields.String()
    fechacreacion = fields.DateTime()
    user = fields.Integer()
    category = fields.Integer()

class ComentSchema(ma.Schema):
    id =  fields.Integer(dump_only=True)
    coment =fields.String()
    fechacreacion = fields.DateTime()
    user = fields.Integer()
    post = fields.Integer()

class UserSchema(ma.Schema):
    id =  fields.Integer(dump_only=True)
    name = fields.String()
    correo = fields.String()
    password = fields.String()
    posts = fields.Nested(PostSchema, many=True)
    coments = fields.Nested(ComentSchema,many=True)

class CategorySchema(ma.Schema):
    id =  fields.Integer(dump_only=True)
    etiqueta = fields.String()
    posts =posts = fields.Nested(PostSchema, many=True)