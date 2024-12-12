from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/")
async def main() -> dict:
    return {"message": "Главная страница."}


@app.get("/users")
async def get_all_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_user(
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=18)]
) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, Возраст: {age}'
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=1, description="Enter user_id", example=1)],
                      username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=18)]
) -> str:
    user_id_str = str(user_id)
    if user_id_str in users:
        users[user_id_str] = f'Имя: {username}, Возраст: {age}'
        return f"The user {user_id} is updated"

    raise HTTPException(status_code=404, detail=f"User {user_id} not found!")


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, description="Enter user_id", example=1)]) -> str:
    user_id_str = str(user_id)
    if user_id_str in users:
        users.pop(user_id_str)
        return f"User {user_id} has deleted!"
    raise HTTPException(status_code=404, detail=f"User {user_id} not found!")