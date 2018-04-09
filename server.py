from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = 'durantula'

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/results', methods=['GET', 'POST'])
def process():
    name = request.form['name']
    language = request.form['language']
    location = request.form['location']
    comment = request.form['comment']
    
    if len(name) < 1:
        flash(f'Name Cannot be empty')
        return redirect('/')
    if len(comment) > 30:
        flash(f'Soory bro. message was too long!')
        return redirect('/')
    if len(comment) < 1:
        flash(f'Soory bro. message was too SHORT!')
        return redirect('/')
    
    return render_template('results.html', name = name, language = language, location = location, comment = comment)
if __name__=="__main__":
    app.run(debug = True)   