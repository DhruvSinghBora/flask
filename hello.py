from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
# define global string variable

global_var = 'hello world'
@app.route('/dhruv')
def python_route():
    return render_template('index.html')

@app.route('/success/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest %s' %( global_var,guest)

# @app.route('/success/<name>')
# def hello_user(name):
#    if name =='admin':
#       return redirect(url_for('hello_admin'))
#    else:
#       return redirect(url_for('hello_guest',guest = name))


@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))


if __name__ == '__main__':
    # app.run(debug=True)
    app.run('127.0.0.1', 5001, True)