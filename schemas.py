from pydantic import BaseModel, ConfigDict, Field
#post model inherting basemodel
class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=50)

#postcreate inherting postbase
class PostCreate(PostBase):
    pass

#post response inherits postbase so eventually it will inherit all properties of it
class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)

    id:int
    date_posted:str



