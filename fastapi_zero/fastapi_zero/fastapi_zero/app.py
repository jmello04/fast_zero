from fastapi import FastAPI
from http import HTTPStatus
from fastapi_zero.schemas import UserSchema, Message, UserPublic, UserDB
app = FastAPI(title= 'Minha API bala')

database = []

@app.get(
    '/',
    status_code=HTTPStatus.OK,
    response_model=Message
)
def read_root():
    #return {'message': 'Olá mundo!'}
    return Message(message='PEI!') 

@app.post(
        '/users/',
        status_code=HTTPStatus.CREATED,
        response_model=UserPublic
)
def create_user(user: UserSchema):
   user_with_id = UserDB(
       username=user.username,
       email=user.email,
       password=user.password,
       id=len(database) + 1
       
   )

   database.append(user_with_id)
   
   return user_with_id 

