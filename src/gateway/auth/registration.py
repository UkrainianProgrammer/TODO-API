import os, requests, datetime
import psycopg2
from dotenv import load_dotenv

load_dotenv()

dbUrl = os.environ.get("POSTGRES_URL")
dbName = os.environ.get("POSTGRES_DB")

def register():
    pass