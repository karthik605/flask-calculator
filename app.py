from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            result = [a+b,a-b,a*b,a/b if b!=0 else '∞']
        except ValueError:
            result = 'Invalid input. Please enter numbers.'
    return render_template('index.html',result=result)

if __name__ == '__main__':
    app.run(debug = True)

