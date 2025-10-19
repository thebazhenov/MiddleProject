from app_context import AppContext, EmailValidate


class User(AppContext):
    login: str
    email: EmailValidate

    class Config:
        schema_extra = [
            {
                "login": "string",
                "email": "string"
            }
        ]
        