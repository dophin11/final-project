from flask import Flask,render_template, request
from function import call_api
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/results", methods=['GET','POST'])
def results():
    if request.method == 'POST':
        query = request.form['query']
        api_result = call_api(query)


        result_data = api_result

        return render_template('results.html', query=query, results=result_data)

    return "This page only accepts POST request"

if __name__ == '__main__':
    app.run(debug=True)
