from math import ceil
from typing import Optional
from fastapi import FastAPI, HTTPException, status
from mock_db import db

app = FastAPI()


@app.get("/posts/")
def index(limit: Optional[int] = 5, page: Optional[int] = 1):

    total_pages = ceil(len(db) / limit)
    first_index = (page - 1) * limit
    last_index = page * limit

    json_response = {
        "meta_data": {
            "pages": total_pages,
            "current_page": page,
            "limit": limit,
            "next_page": f"http://127.0.0.1:8000/posts?limit={limit}&page={page + 1}",
            "previous_page": f"http://127.0.0.1:8000/posts?limit={limit}&page={page - 1}",
        },
        "data": db[first_index:last_index],
    }

    return json_response


def find_post_id(id):
    for post in db:
        if post["id"] == id:
            return post
    return None


@app.get("/posts/{id}")
def show(id: int):
    post = find_post_id(id)

    if post:
        return {"data": post}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"id {id} does not exist!"
        )
