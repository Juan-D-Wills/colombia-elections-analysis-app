from fastapi import FastAPI

app = FastAPI()

from enum import Enum

class ModelName(str, Enum):
    sgd = 'stochastic-gradient-descend'
    rf = 'random-forest'
    svm = 'support-vector-machine'


@app.get('/')
def root():
    return {'Hello': 'World'}


# func args that are not present in path params are interpreted as query params
fake_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get('/items')
def read_items(skip:int = 0, limit:int = 10):
    return fake_db[skip : skip + limit]


# paths with same root path must be above if they are hardcoded
@app.get('/items/my-item')
def read_my_item():
    return {'item': 'This is my item'}


# path parameter and function argument doesn't requiere to have the exact same name, but it is highly recommended
@app.get('/items/{item_id}')
def read_item(item_id:int, msg:str|None = None, is_long:bool = False):
    item = {'item_id':item_id}

    if msg:
        item.update({'message': msg})

    if is_long:
        item.update({'warning': 'The following description is very large, so take some time apart to read it compleatly'})

    return item

# enum enables to have fixed values for path parameter
@app.get('/model/{model_name}')
def read_model(model_name:ModelName):
    if model_name == ModelName.rf:
        return {model_name: 'This model uses many decision trees to work'}
    
    if model_name.value == 'stochastic-gradient-descend':
        return {model_name: 'This model supports online learning'}
    
    if model_name == ModelName.svm:
        return {model_name: 'This model works by setting a threshold'}
    

# the output hint applys only for what the function returns, further parsing is handled somewhere else
@app.get('/file/{file_name:path}')
def read_file(file_name:str) -> dict[int, str]:
    import os
    root = os.getcwd()
    with open(f'{root}/{file_name}') as f:
        return {line_i:content for line_i, content in enumerate(f.readlines())}

# query params can be set to be requiered by not setting a default value, and of course both query types can be set on a single path operation
@app.get('/user/{user_id}/items/{item_id}')
def get_user_item(user_id:int, item_id:int, needy:str, msg:str|None = None):
    response = {'user' : user_id, 'item_id' : item_id, 'needed_query_param' : needy}
    if msg:
        response.update({'message' : msg})
    return response


from pydantic import BaseModel

class Item(BaseModel):
    name:str
    price:float|int
    description:str|None = None
    tax:float = 0

# A Pydantic models tell fastapi to only allow data structures that match with an specific schema
@app.get('/send-item')
def send_item(item:Item):
    item.name = item.name.capitalize()
    item_dict = item.model_dump()
    if item.tax is not None: # to accept if it is 0
        price_with_tax = item.tax + item.price
        item_dict.update({'price_with_tax' : price_with_tax})

    return item_dict

# fastapi recognices by 
@app.put('/items/update-item/{item_id}')
def update_item(item_id:int, item:Item, is_long:bool, msg:str|None = None):
    item_dict = {'item_id' : item_id, **item.model_dump()}

    if is_long:
        item_dict.update({'is_long' : is_long})

    if msg:
        item_dict.update({'message' : msg})

    return item_dict


# add extra validation to query params
from fastapi import Query
from typing import Annotated
@app.get('/all-items')
def get_all_items(q:Annotated[str|None, Query(max_length=50)] = None):
    items = {'all_items': [{'item_id':1, 'name':'notebook'}, {'item_id':2, 'name':'TV'}]}
    if q:
        items.update({'q':q})
    return items