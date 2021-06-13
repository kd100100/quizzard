

# Flask
from flask import Flask, render_template, url_for, request, redirect, session
app = Flask(__name__)
app.secret_key='abhigyan'

# SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
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

from operations import check_u_id, get_u_data, get_data, get_round_det
from txt_dict import get_ques
import json

@app.route('/',methods=['POST','GET'])
def home():
    if request.method=="POST":
        u_id = request.form["u_id"]
        password = request.form["password"]
        print(u_id)
        if (check_u_id(u_id, password)):
            session["u_id"] = u_id
            return redirect("/dashboard")
        else:
            return redirect("/404/u_id")
    return render_template('index.html')

@app.route('/dashboard',methods=['POST','GET'])
def dashboard():
    data = get_u_data(session['u_id'])
    if data == None:
        return redirect("/404/u_id")
    else:
        return render_template('dashboard.html', data = data)

@app.route('/check/<det>')
def check_eligliblity(det):
    det = det.split('-')
    data = get_u_data(session['u_id'])
    print(det)
    if (det[0]=='1'):
        if (int(det[2]) >= 17 and int(det[3]) >= 18 and data['round1'] == 'not_attended'):
            session['quiz'] = True
            return redirect('/quiz/'+det[0])
        elif (int(det[2]) < 22 or int(det[3]) < 18):
            return redirect("/404/starts-6pm-1")
        else:
            return redirect("/404/attended-1")
    elif (det[0]=='2'):
        if data['round2'] == 'not_qualified':
            return redirect('/404/not_qualified-10-2')
        elif int(det[2]) >= 23 and int(det[3]) >= 10 and data['round2'] == 'not_attended':
            session['quiz'] = True
            return redirect('/quiz/'+det[0])
        elif (int(det[2]) < 23 or int(det[3]) < 10):
            return redirect("/404/starts-10am-2")
        else:
            return redirect("/404/attended-2")

@app.route('/quiz/<round>',methods=['POST','GET'])
def quiz(round):
    data = get_ques(round)
    q_count = len(data)
    if 'quiz' in session:
        del session['quiz'] 
        if round == '1':
            db.session.query(users).filter(users.u_id == session['u_id']).update({users.round1:"attended"})
            db.session.commit()
            return render_template('quizspl.html', ques = data, round = round, time = 1200000)
        elif round == '2':
            db.session.query(users).filter(users.u_id == session['u_id']).update({users.round2:"attended"})
            db.session.commit()
            return render_template('quizspl.html', ques = data, round = round, time = 600000)
    if request.method=="POST":
        marks = 0
        time_taken = int(request.form['time'])
        answers = []
        for i in range(q_count):
            try:
                print(request.form[str(i+1)].lower() + "-" + data[i]['crt'].lower())
                answers.append(request.form[str(i+1)])
                if request.form[str(i+1)].lower().lstrip().rstrip() == data[i]['crt'].lower().lstrip().rstrip():
                    marks += 1
            except:
                answers.append('n/a')
                marks = marks
            print(marks)
        if round == '1':
            db.session.query(users).filter(users.u_id == session['u_id']).update({users.round1:str(marks)})            
            session['r1_answers'] = "-".join(answers)
            db.session.query(users).filter(users.u_id == session['u_id']).update({users.r1_time:time_taken})
            db.session.commit()
        elif round == '2':
            db.session.query(users).filter(users.u_id == session['u_id']).update({users.round2:str(marks)})            
            session['r2_answers'] = "-".join(answers)
            db.session.query(users).filter(users.u_id == session['u_id']).update({users.r2_time:time_taken})
            db.session.commit()
        return redirect('/dashboard')

@app.route('/admin',methods=['POST','GET'])
def admin():  
    if ('admin_user' in session):
        if session['admin_user']=='kd1001':
            data = get_data()
            rnd1 = get_round_det(1)
            rnd2 = get_round_det(2)

            if request.method == 'POST':
                if request.form['button'] == 'reattend':
                    u_id = request.form['u_id']
                    round = request.form['round']
                    if round == '1':
                        db.session.query(users).filter(users.u_id == u_id).update({users.round1:'not_attended'})
                    elif round == '2':
                        db.session.query(users).filter(users.u_id == u_id).update({users.round2:'not_attended'})
                elif request.form['button'] == 'notqualified':
                    u_id = request.form['du_id']
                    round = request.form['dround']
                    if round == '1':
                        db.session.query(users).filter(users.u_id == u_id).update({users.round1:'not_qualified'})
                    elif round == '2':
                        db.session.query(users).filter(users.u_id == u_id).update({users.round2:'not_qualified'})
                elif request.form['button'] == 'change':
                    u_id = request.form['cu_id']
                    name = request.form['cname']
                    db.session.query(users).filter(users.u_id == u_id).update({users.name:name})
                elif request.form['button'] == 'del':
                    u_id = request.form['delu_id']
                    user = users.query.get(u_id)
                    db.session.delete(user)
                elif request.form['button'] == 'r1-r2':
                    u_id = request.form['u_id']
                    db.session.query(users).filter(users.u_id == u_id).update({users.round1:'qualified'})
                    db.session.query(users).filter(users.u_id == u_id).update({users.round2:'not_attended'})
                elif request.form['button'] == 'add_team':
                    u_id = request.form['u_id']
                    password = request.form['password']
                    name = request.form['name']
                    new = users(u_id = u_id, password = password, name = name)
                    db.session.add(new)
                db.session.commit()
                return redirect('/admin')
            return render_template('admin.html', data = data, rnd1 = rnd1, rnd2 = rnd2)
        else:
            return redirect('/admin-login')
    else:
        return redirect('/admin-login')

@app.route('/admin-login', methods = ['POST', 'GET'])
def admin_login():
    if request.method == 'POST':
        password = request.form['password']
        if password == 'kd1001':
            session['admin_user'] = password
        return redirect('/admin')
    return render_template('admin-login.html')

@app.route('/404/<error>')
def error_pg(error):
    error = error.split('-')
    print(error)
    if (error[0]=='u_id'):
        data = "Either Team Name or Password is wrong. Please check your email"
    elif (error[0]=='attended'):
        data = 'You have aleady attended the Round '+error[1]+'!'
    elif (error[0]=='starts'):
        data = 'Round '+error[2]+' starts at '+error[1]+'!'
    elif (error[0]=='not_qualified'):
        data = 'Either, quiz starts at '+error[2]+'am or you have not been qualified to Round '+error[1]+'! If you have been Qualified, you would have received mail by 11pm.'
    else:
        data = "There is some issue!"
    return render_template('404.html', data=data)

@app.route('/viewyouranswer')
def answers():
    return render_template('answers.html', session = session)

@app.route('/test/<data>')
def chck(data):
    return '<h1>'+data+'</h1>'

if __name__ == "__main__":
    app.run(debug=True)