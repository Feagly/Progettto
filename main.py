from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from typing import Annotated

from starlette.responses import RedirectResponse

app = FastAPI()
templates = Jinja2Templates(directory = "templates")
app.mount("/static", StaticFiles(directory = "static"), name = "static")

class Product(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=30)]
    price: Annotated[float, Field(gt=0)]
    location: Annotated[str, Field(min_length=3, max_length=30)]

product_list = [Product(name="Tastiera Meccanica", price=8.99, location="Corsia A")]

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="home.html", context={"text": "welcome to the store"})

@app.get("/products", response_class=HTMLResponse, name= "products")
def products(request: Request):
    return templates.TemplateResponse(request=request, name="products.html", context={"product_list": product_list})

@app.get("/add_product", response_class=HTMLResponse, name="add_product")
def add_product(request: Request):
    return templates.TemplateResponse(request=request, name="add_product.html", context= {"product_list": product_list})

@app.post("/insert_product_data")
def insert_product_data(
    name: Annotated[str, Form()],
    price: Annotated[float, Form()],
    location: Annotated[str, Form()]
):
    product = Product(name=name, price=price, location=location)
    product_list.append(product)
    return RedirectResponse(url="/products", status_code=303)