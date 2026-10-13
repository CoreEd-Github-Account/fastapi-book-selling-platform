from sqlmodel import  Field, SQLModel



class CreateUserRequest(SQLModel):
    username: str
    email: str
    uni_name: str
    Phone_number: str