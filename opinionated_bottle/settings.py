from envparse import env

env.read_envfile()

HOST = env("HOST", cast=str)
PORT = env("PORT", cast=int)
DEBUG = env("DEBUG", cast=bool)
RELOADER = env("RELOADER", cast=bool)
