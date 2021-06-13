# Flask
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

# SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class users(db.Model):
    u_id = db.Column(db.String(40), primary_key = True, nullable = False)
    password = db.Column(db.String(40), nullable = False)
    name = db.Column(db.String(20), nullable = False)
    round1 = db.Column(db.String(20), nullable=False, default = 'not_attended')
    r1_time = db.Column(db.Integer)
    round2 = db.Column(db.String(20), nullable=False, default = 'not_qualified')
    r2_time = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.u_id}:{self.password}:{self.name}:{self.round1}:{self.r1_time}:{self.round2}:{self.r2_time}"

def get_data():
    db_obj = users.query.all()
    p_list = []
    for i in range(len(db_obj)):
        db_str = str(db_obj[i])
        db_list = db_str.split(':')
        temp = {}
        temp['u_id'] = db_list[0]
        temp['password'] = db_list[1]
        temp['name'] = db_list[2]
        temp['round1'] = db_list[3]
        temp['r1_time'] = db_list[4]
        temp['round2'] = db_list[5] 
        temp['r2_time'] = db_list[6]
        p_list.append(temp)
    return p_list

def check_u_id(u_id, password):
    data = get_data()
    for i in data:
        if (i['u_id'] == u_id) and (i['password'] == password):
            return True
    return False

def get_u_data(u_id):
    data = get_data()
    for i in data:
        if i['u_id'] == u_id:
            return i
    return None

def get_round_det(x):
    if x == 1:
        db_obj = users.query.order_by(users.round1).all()
        p_list = []
        for i in range(len(db_obj)):
            db_str = str(db_obj[i])
            db_list = db_str.split(':')
            # print(db_list)
            temp = {}
            temp['u_id'] = db_list[0]
            temp['password'] = db_list[1]
            temp['name'] = db_list[2]
            temp['round1'] = db_list[3]
            temp['r1_time'] = db_list[4]
            temp['round2'] = db_list[5] 
            temp['r2_time'] = db_list[6]
            p_list.append(temp)
            # print(temp)
        return p_list

    elif x == 2:
        db_obj = users.query.filter(users.round1 == 'qualified').order_by(users.round2).all()
        p_list = []
        for i in range(len(db_obj)):
            db_str = str(db_obj[i])
            db_list = db_str.split(':')
            temp = {}
            temp['u_id'] = db_list[0]
            temp['password'] = db_list[1]
            temp['name'] = db_list[2]
            temp['round1'] = db_list[3]
            temp['r1_time'] = db_list[4]
            temp['round2'] = db_list[5] 
            temp['r2_time'] = db_list[6]
            p_list.append(temp)
        return p_list
    
    else:
        db_obj = users.query.filter(users.round2 == 'qualified').order_by(users.round3).all()
        p_list = []
        for i in range(len(db_obj)):
            db_str = str(db_obj[i])
            db_list = db_str.split(':')
            temp = {}
            temp['u_id'] = db_list[0]
            temp['password'] = db_list[1]
            temp['name'] = db_list[2]
            temp['round1'] = db_list[3]
            temp['r1_time'] = db_list[4]
            temp['round2'] = db_list[5] 
            temp['r2_time'] = db_list[6]
            p_list.append(temp)
        return p_list

