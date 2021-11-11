# IF NEEDED FOR AWS, DB KEYS, OR ANY OTHER CONFIG FILES #


"""Flask configuration."""
# from os import environ, path
# from dotenv import load_dotenv


# basedir = path.abspath(path.dirname(__file__))
# load_dotenv(path.join(basedir, '.env'))

# TESTING = True
# DEBUG = True
# FLASK_ENV = 'development'
SECRET_KEY = 'SECRET_KEY'

# AWS Secrets
AWS_ENDPOINT = "dbs-seed.cq637ugrj1yy.us-east-1.rds.amazonaws.com"
AWS_PORT: 3306
AWS_USERNAME: "admin"
AWS_PW: "dbs_seed_2021"