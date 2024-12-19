from fastapi import FastAPI, Path, HTTPException, Form, Request
from typing import List, Annotated
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/")
async def main(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}")
def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id - 1]})
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")


@app.post("/")  #user/{username}/{age}
# async def create_user(request: Request,
#                       username: Annotated[
#                           str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
#                       age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=18)]
#                       ) -> HTMLResponse:

async def create_user(request: Request, username: str = Form(
    min_length=5, max_length=20, description="Enter username", example="UrbanUser"),
                      age: int = Form(ge=18, le=120, description="Enter age", example=18)) -> HTMLResponse:
    user_id = max((u.id for u in users), default=0) + 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.put("/user/{user_id}/{username}/{age}")
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
