from fastapi import FastAPI
from http import HTTPStatus
from fastapi_zero.schemas import UserSchema, Message  
app = FastAPI(title= 'Minha API bala')

@app.get(
    '/',
    status_code=HTTPStatus.OK,
    response_model=Message
)
def read_root():
    #return {'message': 'Olá mundo!'}
    return Message(message='PEI!') 

@app.post('/users/')
def create_user(user: UserSchema):
   return user

