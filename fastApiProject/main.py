from fastapi import FastAPI

from user import user

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/users")
async def get_users():
    return [user.get_user_info() for user in users_list]

users_list = [
    user(1, "JohnDoe", "password123", "123 Main St", "555-1234", "New York", "USA"),
    user(2, "JaneDoe", "password456", "456 Oak St", "555-5678", "Los Angeles", "USA"),
    user(3, "Alice", "password789", "789 Pine St", "555-9101", "Chicago", "USA")
]
