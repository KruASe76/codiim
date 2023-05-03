from os import environ


token = environ.get("TOKEN")
admin_ids = tuple(map(int, environ.get("ADMINS").split(",")))
