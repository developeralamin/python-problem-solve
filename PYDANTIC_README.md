# Pydantic

## What is Pydantic?

**Pydantic** is a Python library for **data validation**, **serialization**, and **parsing**.

FastAPI uses Pydantic to validate incoming request data and serialize outgoing response data.

---

# Responsibilities of Pydantic

- Validate request data
- Convert data types
- Serialize Python objects to JSON
- Deserialize JSON to Python objects
- Generate API schemas for Swagger/OpenAPI

---

# Basic Example

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

Request

```json
{
    "name": "Alamin",
    "age": 25
}
```

Creates a Python object:

```python
user.name
user.age
```

---

# Validation Example

Schema

```python
class User(BaseModel):
    age: int
```

Request

```json
{
    "age": "abc"
}
```

Response

```text
Validation Error
Input should be a valid integer
```

---

# Type Conversion

```python
class User(BaseModel):
    age: int
```

Request

```json
{
    "age": "25"
}
```

Pydantic automatically converts

```python
"25"
```

to

```python
25
```

---

# BaseModel

Every schema inherits from

```python
BaseModel
```

Example

```python
class User(BaseModel):
    name: str
```

---

# model_dump()

Converts a Pydantic model into a Python dictionary.

```python
user = User(name="Alamin", age=25)

print(user.model_dump())
```

Output

```python
{
    "name": "Alamin",
    "age": 25
}
```

---

# model_validate()

Creates a Pydantic object from Python data.

```python
data = {
    "name": "Alamin",
    "age": 25
}

user = User.model_validate(data)
```

---

# Field()

Used for extra validation.

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    age: int = Field(gt=0)
```

Only accepts values greater than zero.

---

# Optional Field

```python
from typing import Optional

class User(BaseModel):
    phone: Optional[str] = None
```

---

# List

```python
from typing import List

class Course(BaseModel):
    students: List[str]
```

---

# Nested Model

```python
class Address(BaseModel):
    city: str

class User(BaseModel):
    name: str
    address: Address
```

---

# Email Validation

```python
from pydantic import EmailStr

class User(BaseModel):
    email: EmailStr
```

Only valid email addresses are accepted.

---

# Response Model

```python
class UserResponse(BaseModel):
    id: int
    email: EmailStr
```

```python
@app.get("/users/{id}", response_model=UserResponse)
```

Only fields inside `UserResponse` are returned.

---

# Serialization

Python Object

↓

JSON

```python
user.model_dump()
```

---

# Deserialization

JSON

↓

Python Object

```python
User.model_validate(data)
```

---

# Config (Pydantic v1)

```python
class UserResponse(BaseModel):

    id: int

    class Config:
        orm_mode = True
```

Purpose

- Allow reading data from ORM objects
- Configure model behavior

---

# ConfigDict (Pydantic v2)

```python
from pydantic import ConfigDict

class UserResponse(BaseModel):

    id: int

    model_config = ConfigDict(
        from_attributes=True
    )
```

`from_attributes=True` replaces

```python
orm_mode = True
```

---

# Common Config Options

```python
model_config = ConfigDict(

    from_attributes=True,

    extra="forbid",

    frozen=True,

    validate_assignment=True,

    str_strip_whitespace=True
)
```

### from_attributes=True

Read data from ORM objects.

### extra="forbid"

Reject unknown fields.

### frozen=True

Model becomes immutable.

### validate_assignment=True

Validate values when assigning after creation.

### str_strip_whitespace=True

Automatically removes leading and trailing spaces.

---

# Pydantic vs SQLAlchemy

| Pydantic | SQLAlchemy |
|----------|------------|
| Data Validation | ORM |
| Request Schema | Database Model |
| Response Schema | Database Table |
| BaseModel | Base |
| JSON Handling | Database Handling |

---

# FastAPI Request Flow

```
Client

↓

JSON Request

↓

Pydantic Validation

↓

Python Object

↓

Business Logic

↓

SQLAlchemy ORM

↓

Database

↓

SQLAlchemy Object

↓

Pydantic Response Model

↓

JSON Response
```

---

# Industry Standard Schema Structure

```python
class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    email: EmailStr | None = None
    password: str | None = None


class UserResponse(UserBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )
```

---

# Important Methods

| Method | Purpose |
|---------|----------|
| model_dump() | Convert model to dictionary |
| model_validate() | Create model from data |
| model_copy() | Copy model |
| model_json_schema() | Generate JSON schema |

---

# Important Types

- str
- int
- float
- bool
- EmailStr
- UUID
- datetime
- date
- Decimal
- HttpUrl

---

# Summary

- Pydantic validates request data.
- Pydantic serializes response data.
- FastAPI automatically integrates with Pydantic.
- `BaseModel` is the foundation of every schema.
- `model_dump()` converts models to dictionaries.
- `model_validate()` creates models from dictionaries.
- `response_model` uses Pydantic schemas to filter and validate responses.
- SQLAlchemy manages the database.
- Pydantic manages data validation and serialization.