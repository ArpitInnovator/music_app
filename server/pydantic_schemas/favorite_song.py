from pydantic import BaseModel  #type: ignore

class FavoriteSong(BaseModel):
    song_id: str
    