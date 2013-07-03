import os
basedir = ospath.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = "never-know-what-it-is"

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHMEY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

