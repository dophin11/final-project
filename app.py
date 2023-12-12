from flask import Flask,render_template, request
from function import call_api
app = Flask(__name__)

@app.route("/")
def start():
    return render_template('start.html')
@app.route("/index", methods=['GET'])
def index():
    username = request.args.get('name')
    return render_template('index.html', name=username)

@app.route("/results", methods=['GET','POST'])
def results():
    if request.method == 'POST':
        food = request.form['food']
        amount = request.form['amount']
        query = f"{amount} {food}"
        api_result = call_api(query)


        result_data = api_result

        return render_template('results.html', query=query, results=result_data)

    return "This page only accepts POST request"

if __name__ == '__main__':
    app.run(debug=True)
