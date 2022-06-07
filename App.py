from flask import Flask,request,render_template
import Add

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/total', methods= ['POST', 'GET'])
def total():
    if request.method == 'POST':
        # Then get the data from the form
        Input_1 = request.form['Input_1']
        Input_2 = request.form['Input_2']

        sum=Add.add(float(Input_1),float(Input_2))
        return render_template("total.html", variable=sum)
    else:
        return "Error"



if __name__=="__main__":
    app.run(debug=True)