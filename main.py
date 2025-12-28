import typer as ty
from typing import Optional

app = ty.Typer()

@app.command()
def intro(name: str, iq: int, display: bool = True):
    print(f'Hello {name}')
    if display:
        print(f'Your iq is {iq}')


@app.command()
def outro(name: str):
    print(f'Goodbye {name}')

@app.command()
def add_task(title: str, content: Optional[str | None] = None):
    print("Title:", title)
    if content is not None:
        print("Content:", content)


if __name__ == "__main__":
    app()