from enum import Enum
from pathlib import Path
from typing import Annotated, Union

import pandas as pd
from fastapi.responses import FileResponse as APIFileResponse
from typing import Optional, Annotated, Any

from fastapi import Depends, FastAPI, HTTPException, Query, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from pydantic import BaseModel

from starlette.datastructures import URL
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.responses import FileResponse

from app.exceptions import value_error_handler
from emo.paths import get_data_path

app = FastAPI(title="Environmental monitoring service API",
              description="API service with metadata. Web page: https://environmental-monitoring-82bc1f9868c5.herokuapp.com")
app.mount("/templates", StaticFiles(directory="./templates"), name="templates")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
templates = Jinja2Templates(directory="templates")


def https_url_for(*params, **path_params: Any):

    http_url: URL = params[0]

    # Replace 'http' with 'https'
    return URL(str(http_url).replace('http://', 'https://'))


templates.env.globals["https_url_for"] = https_url_for

sipe_users = {
    "dreamlone": {
        "username": "dreamlone",
        "password": "FAKehashed12345SuperSecret#PasswordForThat21",
    },
    "university": {
        "username": "university",
        "password": "FAKehasheduniversity"
    }
}


class User(BaseModel):
    username: str


class UserInDB(User):
    password: str


class OutputFormat(str, Enum):
    csv = 'csv'
    excel = 'xlsx'
    parquet = 'parquet'


def fake_decode_token(token):
    return User(username=token + "FAKedecoded")


def fake_hash_password(password: str):
    return "FAKehashed" + password


@app.get("/", response_class=HTMLResponse)
def get_root(request: Request):
    return templates.TemplateResponse("./description.html", {"request": request})


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


@app.get("/metadata_per_station")
def get_metadata_per_station(token: Annotated[str, Depends(get_current_user)],
                             station: str = 'Kilpisjärvi'):
    """ Return information per station

    Important: For demonstration purposes support only Kilpisjärvi station
    """
    df = pd.read_excel(Path(get_data_path(), 'corrected_version.xlsx'), sheet_name=station)
    df = df.fillna('None')
    return df.to_dict('records')


@app.get("/metadata_per_station_as_file")
def get_metadata_per_station_as_file(token: Annotated[str, Depends(get_current_user)],
                                     station: str = 'Kilpisjärvi', output_format: OutputFormat = OutputFormat.csv):
    api_folder_results = Path(get_data_path(), 'api_results')
    if api_folder_results.exists() is False:
        api_folder_results.mkdir(exist_ok=True, parents=True)

    # Convert on the fly
    df = pd.read_excel(Path(get_data_path(), 'corrected_version.xlsx'), sheet_name=station)
    if output_format.name == 'csv':
        file_name = f'{station}.csv'
        df.to_csv(Path(api_folder_results, file_name), index=False)
    elif output_format.name == 'parquet':
        file_name = f'{station}.parquet'
        df.to_parquet(Path(api_folder_results, file_name), index=False)
    elif output_format.name == 'excel':
        file_name = f'{station}.xlsx'
        df.to_excel(Path(api_folder_results, file_name), index=False)
    else:
        raise ValueError(f'Format {output_format.name} does not supported')

    file_path = Path(api_folder_results, file_name)
    return FileResponse(file_path, filename=file_name)


@app.get("/dataset_by_id")
def get_dataset_by_id(token: Annotated[str, Depends(get_current_user)],
                      index: str = 'a0c62d62-c0b3-4c3e-b82f-fb2f1c99b941'):
    """ """
    known_ids = ['a0c62d62-c0b3-4c3e-b82f-fb2f1c99b941', 'd79f09a0-f8d8-4328-8b21-38bb15d72357']
    if index not in known_ids:
        raise ValueError(f'Dataset with id {index} does not exist')

    return {"message": "This is the demo page. Dataset is not provided"}


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


@app.post("/token")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = sipe_users.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    password = fake_hash_password(form_data.password)
    if password != user.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


app.exception_handler(ValueError)(value_error_handler)
