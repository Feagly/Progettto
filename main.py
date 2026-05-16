from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory = "templates")
app.mount("/static", StaticFiles(directory = "static"), name = "static")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="home.html", context={"text": "welcome to the store"})

@app.get("/products", response_class=HTMLResponse, name= "products")
def products(request: Request):
    product_list = [{"name": "Tastiera Meccanica", "price": 8.99, "location": "Corsia A"}]
    return templates.TemplateResponse(request=request, name="products.html", context={"product_list": product_list})