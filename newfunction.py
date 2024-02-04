import re
import string
import random
import mysql.connector
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

# DATABASE CONNECTION
mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="passmate")
mycursor=mydb.cursor()

# FUNCTION FOR ADDING PASSWORDS TO DB
def add_pass_to_db(passdata):
    dholu=passdata['id']
    bholu=passdata['input']
    sform1="insert into datatable (identifier, userdata) values (%s,%s)"
    datainpt1=[(dholu,bholu)]
    mycursor.executemany(sform1,datainpt1)
    mydb.commit()

# FUNCTION FOR SEARCHING IN DB
def load_pass_from_db():
    sform2="select * from datatable"
    mycursor.execute(sform2)
    result=mycursor.fetchall()
    result_dicts=[]
    for row in result:
         dict_temp={
             "id":row[0],
             "identifier":row[1],
             "userdata":row[2],
         }
         result_dicts.append(dict_temp)
    return result_dicts

load_pass_from_db()

# FUNCTION FOR RETURNING SPECIFIC PASSWORD
def load_spass_from_db(id):
    result=load_pass_from_db()
    for i in result:
        if i['identifier']==id:
            return i['userdata']  
