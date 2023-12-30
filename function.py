import re
import string
import random
from sqlalchemy import create_engine,text
import pymysql
import os


def checkpasswordstrength(siu):    
    password=siu
    uppercase_pattern = re.compile(r"[A-Z]")
    lowercase_pattern = re.compile(r"[a-z]")
    digit_pattern = re.compile(r"\d")
    special_char_pattern = re.compile(r"[\W_]")

    has_uppercase = uppercase_pattern.search(password)
    has_lowercase = lowercase_pattern.search(password)
    has_digit = digit_pattern.search(password)
    has_special_char = special_char_pattern.search(password)

    password_score = 0

    if has_uppercase:
        password_score += 20
    if has_lowercase:
        password_score += 20
    if has_digit:
        password_score += 20
    if has_special_char:
        password_score += 20
    if len(password) >= 7:
        password_score += 20
    if len(password) <=3:
        password_score -= 10

    return password_score

def generatepassword(len):
    length=len
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for i in range(length))

    return password

from sqlalchemy import create_engine,text
db_connection_string=os.environ['DB_CONNECTION_STRING']
engine = create_engine(db_connection_string,
                       connect_args={
                           "ssl":{
                               "ssl_ca":"/etc/ssl/cert.pem"
                           }
                       },
                       pool_size=20
                       )


def add_pass_to_db(passdata):
    with engine.connect() as conn:
        dholu=passdata['id']
        bholu=passdata['input']
        query=text(f"insert into passmate (identifier, userdata) values ('{dholu}', '{bholu}')")
        conn.execute(query)


def load_pass_from_db():
    with engine.connect() as conn:
        result=conn.execute(text("select * from passmate"))
        result_dicts=[]
        for row in result.all():
            dict_a={
            "id":row[0],
            "identifier":row[1],
            "userdata":row[2],
            }
            result_dicts.append(dict_a)
    return result_dicts

def load_spass_from_db(id):
    result=load_pass_from_db()
    for i in result:
        if i['identifier']==id:
            return i['userdata']
