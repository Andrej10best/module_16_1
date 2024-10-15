from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def get_main_page():
    return 'Главная страница'

@app.get('/user/admin')
async def get_admin_page():
    return 'Вы вошли как администратор'

@app.get('/user/{user_id}')
async def get_user_info(user_id):
    return f'Вы вошли как пользователь №{user_id}'

@app.get('/user')
async def get_user_number(username, age):
    return {'Имя:': username, 'Возраст:': age}

