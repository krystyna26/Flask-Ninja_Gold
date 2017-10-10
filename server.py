from flask import Flask, render_template, request, redirect, session
import random, datetime
from time import gmtime, strftime

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def defaultPage():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    location = request.form['building']
    czas = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    if location == 'farm':
        goldF = random.randrange(10, 21) 
        info = {'money':goldF, 'place':location, "time": czas}
    elif location == 'cave':
        goldF = random.randrange(5,11)
        info = {'money':goldF, 'place':location, "time": czas}
    elif location == 'house':
        goldF = random.randrange(2,6)
        info = {'money':goldF, 'place':location, "time": czas}
    elif location == 'casino':
        goldF = random.randrange(-50,51)
        info = {'money':goldF, 'place':location, "time": czas}
    
    session['activities'].insert(0,info)
    session['gold'] += goldF     
    return redirect('/')

app.run(debug=True)