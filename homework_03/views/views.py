from fastapi import APIRouter

router = APIRouter(tags=["Items"])

items = {1: "John",
         2: "Kate",
         3: "Mike",
         }


@router.get("/items")
def get_items():
    return items


@router.post("/add_item")
def add_item(item):
    items.update({str(len(items)+1): item})
    return {"Message": "Added successfully"}
