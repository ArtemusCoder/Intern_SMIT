import json

from init import create_app
from typing import Dict, List
from models.Rate import Rate, Rate_Pydantic
from datetime import date
from fastapi import UploadFile, status
from fastapi.responses import JSONResponse

app = create_app()


@app.post("/rate/create/", status_code=201)
async def add_rate(items: Dict[str, List[Dict]]):
    for date_item, objects in items.items():
        for rate_obj in objects:
            try:
                y, m, d = [int(i) for i in date_item.split('-')]
                await Rate.create(cargo_type=rate_obj['cargo_type'], rate=float(rate_obj['rate']), date=date(y, m, d))
            except ValueError:
                return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                    content="Wrong values")
            except KeyError:
                return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                    content="Wrong sending structure")
    return {"status": "ok"}


@app.post("/uploadjson/")
async def create_upload_file(file: UploadFile):
    try:
        if file.content_type != "application/json":
            raise Exception("Wrong type of file")
        json_data = json.load(file.file)
        result = await add_rate(json_data)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=str(e))
    return {"status": "ok"}


@app.get("/rates/", status_code=201)
async def get_rates():
    return await Rate_Pydantic.from_queryset(Rate.all())


@app.get("/rate/")
async def get_rate(cargo_type: str, sending_date: date):
    return await Rate.get(cargo_type=cargo_type, date=sending_date).values('rate')


@app.get("/calculate/rate")
async def calculate_rate(cost: float, cargo_type: str, sending_date: date):
    result = await get_rate(cargo_type, sending_date)
    rate = result['rate']
    return cost * rate
