import jwt
import datetime
from config import BasicConfig
from app import db,bcrypt

class Usuario(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    email=db.Column(db.String(255),unique=True,nullable=False)
    password=db.Column(db.String(255),nullable=False)
    registrado=db.Column(db.DateTime,nullable=False)
    admin=db.Column(db.Boolean,nullable=False,default=False)

    def __init__(self,email,password,admin=False):
        self.email=email
        self.password=bcrypt.generate_password_hash(
            password,BasicConfig.BCRYPT_LOG_ROUNDS
        ).decode()
        self.registrado=datetime.datetime.now()
        self.admin=admin

    def encode_auth_token(self,user_id):
        try:
            payload={
                'exp':datetime.datetime.utcnow()+datetime.datetime(days=0,minutes=10),
                'iat':datetime.datetime.utcnow(),
                'sub':user_id
            }
            return jwt.encode(
                payload,
                BasicConfig.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e
        
    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload=jwt.decode(
                auth_token,
                BasicConfig.SECRET_KEY,
                algorithms=["HS256"]
            )
            return payload['sub']
        except jwt.ExpiredSignatureError as e:
            print(e)
            return "token expirado"
        except jwt.InvalidTokenError as e:
            return "token invalido"