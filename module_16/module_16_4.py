from fastapi import FastAPI, Path, HTTPException
from typing import List, Annotated
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/")
async def main() -> dict:
    return {"message": "Главная страница."}


@app.get("/users")
async def get_all_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def create_user(
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=18)]
) -> str:
    user_id = max((u.id for u in users), default=0) + 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return f"User {new_user.id} is registered"


@app.put("/user/{user_id}")
async def update_user(user_id: int, user: User) -> str:
    for index, ex_user in enumerate(users):
        if ex_user.id == user_id:
            users[index] = User(id=user_id, username=user.username, age=user.age)
            return f"The user {user_id} is updated"

    raise HTTPException(status_code=404, detail=f"User {user_id} not found!")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    for index, ex_user in enumerate(users):
        if ex_user.id == user_id:
            users.pop(index)
            return f"User {user_id} has deleted!"
    raise HTTPException(status_code=404, detail=f"User {user_id} not found!")