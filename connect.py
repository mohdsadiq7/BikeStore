from flask import Flask, render_template, request, url_for , session , flash ,Response
from flask_mail import Mail, Message
import smtplib
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re 
import time
from flask_caching import Cache


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# HOMEPAGE ############################################
@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/artical')
def artical():
    return render_template('articles.html')

@app.route('/devel')
def develop():
    return render_template('developer.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/events')
def events():
    return render_template('events.html')
############################################################################

@app.route('/acc')
def student():
   return render_template('acc.html')


@app.route('/two')
def manoj():
    return render_template('acc2.html')

@app.route('/qqq')
def manojx():
    return render_template('acc.html')


@app.route('/tree')
def manoj2():
    return render_template('man.html',name="qwertyuio",price="123654")



#Page-1
@app.route('/four')
def manoj3():
    return render_template('single.html')

@app.route('/five')
def manoj4():
    return render_template('single-2.html')

@app.route('/six')
def manoj5():
    return render_template('single-3.html')

@app.route('/seven')
def manoj6():
    return render_template('single-4.html')

@app.route('/eight')
def manoj7():
    return render_template('single-5.html')

@app.route('/nine')
def manoj8():
    return render_template('single-6.html')

@app.route('/ten')
def manoj9():
    return render_template('single-7.html')

@app.route('/leven')
def manoj10():
    return render_template('single-8.html')


#Page-2
@app.route('/Oneone')
def manoj11():
    return render_template('single-9.html')

@app.route('/Onetwo')
def manoj12():
    return render_template('single-10.html')

@app.route('/Oneeit')
def manoj13():
    return render_template('single-11.html')

@app.route('/Onetre')
def manoj14():
    return render_template('single-12.html')

@app.route('/Onefor')
def manoj15():
    return render_template('single-13.html')

@app.route('/Onefiv')
def manoj16():
    return render_template('single-14.html')

@app.route('/Onesix')
def manoj17():
    return render_template('single-15.html')

@app.route('/Oneseven')
def manoj18():
    return render_template('single-16.html')

@app.route('/OneBuy')
def manoj_Buy():
    return render_template('abc.html')

@app.route('/OnePay')
def index():
    return render_template('index.html')

@app.route('/form',methods = ['GET' , 'POST'])
def form():
    if request.method == 'POST':
        glon = request.form['glon']

        return render_template('abc.html',glon=glon)


@app.route('/OneQW')
def manoj_Tq():
    return render_template('thankyou.html')




@app.route('/form123' , methods=["POST"]    )
def form123():
    Name = request.form.get("Name")
    Email = request.form.get("Email")
    Question = request.form.get("Question")
    
    name_m='''
            Name : %s\n
            Email : %s\n
            Question : %s\n
            '''%(Name,Email,Question)
    message = name_m
    server= smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("niebikershop@gmail.com","rkduucllpzxazdvj")
    server.sendmail("niebikershop@gmail.com","niebikershop@gmail.com",message)


    if not Name or not Email or not Question:
        error_statement="All fields are compulsary"
        return render_template("contact.html",error_statement=error_statement,Name=Name,Email=Email,Question=Question)

    return render_template("homepage.html")

@app.route('/index123' , methods=["POST"]    )
def index123():
    name = request.form.get("firstname")
    email = request.form.get("email")
    address = request.form.get("address")
    city = request.form.get("city")
    state = request.form.get("state")
    zipp = request.form.get("zip") 
    if name == None or email == None or zipp == None or city == None or state == None or address == None :
        
        return render_template("abc.html")
    name_m='''
        Thank You ,
        For Ordering From Bike Shop
        Details :-
        Name : %s\n
        Email : %s\n
        zip : %s\n
        '''%(name,email,zipp)
    message = name_m
    server= smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("niebikershop@gmail.com","rkduucllpzxazdvj")
    try:
        server.sendmail("niebikershop@gmail.com",email,message)
    except:
        error1 = "Please Fill The Left Side Fields"
        flash(error1)
        return render_template("abc.html",error=error1)
    return render_template('thankyou.html') , "Sent"


#Sign-Up###############################################################

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'manoj@99'
app.config['MYSQL_DB'] = 'bikeshop'


mysql = MySQL(app)

@app.route('/signup_db' , methods=['GET', 'POST'])
def signup_db():
    if request.method == "POST":
        details = request.form
        name_db = details['name']
        e_mail = details['email']
        passw = details['psw']
        passwd = details['psw-repeat']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO signup(name, email ,passwd) VALUES (%s, %s ,%s)", (name_db, e_mail ,passwd))
        mysql.connection.commit()
        cur.close()
        return render_template('thankyou.html')
    
    return render_template('thankyou.html')

#Login##########################################################################

@app.route('/login', methods=['GET', 'POST'])
def login123():
    username = request.form['uname']
    password = request.form['psw']
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM signup WHERE name = %s AND passwd = %s', (username, password))
    data = cursor.fetchone()
    if data == None:
        error = "BAD CREDENTIALS"
        flash(error)
        return render_template('login.html',error=error)
    else :
        
        return render_template('homepage_new.html', value = username)

@app.route("/logout")
def logout():
    # Response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return render_template('homepage.html')

#Customized Bikes########################################################################################

@app.route("/customized")
def customized():
    return render_template('custombikes.html')

@app.route("/Cruise")
def Cruise():
    return render_template('cruisebikes.html')

@app.route("/Sports")
def Sports():
    return render_template('sportsbikes.html')

@app.route("/Dirt")
def Dirt():
    return render_template('dirtbikes.html')

if __name__ == '__main__':
   app.run(debug = True)

