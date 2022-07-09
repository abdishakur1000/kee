from pydantic import BaseSettings

"""THIS IS HOW YOU SET UP ENVIRONMENT_VARIABLES"""


class Settings(BaseSettings):
    D_hostname: str
    D_port: str
    D_password: str
    D_name: str
    D_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = '.env'



settings = Settings()
# print(settings.D_password)
# print(settings.D_username)
# print(settings.algorithm)
# print(settings.secret_key)
# print(settings.MY_API_URL)

