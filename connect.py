import psycopg2
from config import DATABASE_URL
from psycopg2.extras import RealDictCursor

def get_connection():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)