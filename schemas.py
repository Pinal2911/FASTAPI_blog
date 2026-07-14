from pydantic import BaseModel, ConfigDict, Field, EmailStr
from datetime import datetime
#post model inherting basemodel
class UserBase(BaseModel):
    username: str = Field(min_length=1,max_length=50)
    email: EmailStr = Field(max_length=120)

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    image_file: str | None
    image_path: str

class UserUpdate(BaseModel):
    username: str | None = Field(default=None, min_length=1,max_length=50)
    email : EmailStr | None = Field(default=None,max_length=120)
    image_file: str | None = Field(default=None,min_length=1,max_length=200)

class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    
class PostUpdate(BaseModel):
    title: str | None = Field(default=None,min_length=1,max_length=100)
    content: str | None = Field(default=None,min_length=1)
#postcreate inherting postbase
class PostCreate(PostBase):
    user_id :int

#post response inherits postbase so eventually it will inherit all properties of it
class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)
    id:int
    date_posted: datetime
    user_id: int
    author: UserResponse



