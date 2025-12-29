import typer as ty
from typing import Optional
import time
from rich.progress import track
import random

app = ty.Typer()

# @app.command()
# def intro(name: str, iq: int, display: bool = True):
#     print(f'Hello {name}')
#     if display:
#         print(f'Your iq is {iq}')


# @app.command()
# def outro(name: str):
#     print(f'Goodbye {name}')
def animation():
    total = 0
    for value in track(range(100), description="Processing"):
        time.sleep(0.001)
        total += random.randint(0, 4)

@app.command()
def add_task(title: str, content: Optional[str | None] = None):
    animation()
    print("Title:", title)
    if content is not None:
        print("Content:", content)

@app.command()
def get_all_task(completed: Optional[bool | None] = None):

    animation()

    if completed is None:
        print("You'll get all the task")
    elif completed:
        print("You'll get only true task")
    else:
        print("You'll get all incomplete task")

@app.command()
def delete_task(id :int):
    animation()

    print(f"The task with the id {id} will be deleted")

@app.command()
def update_task(id: int,
                title: str | None = None, 
                content: str | None = None,
                completed: str | None = None):
    animation()

    print(f"Task with id {id} will be updated")
    payload = {}

    if title is not None:
        payload.update({"title": title})
    if content is not None:
        payload.update({"content": content})
    if completed is not None:
        payload.update({"completed": completed})

    print(payload)





if __name__ == "__main__":
    app()