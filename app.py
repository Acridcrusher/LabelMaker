from flask import Flask, render_template, request, url_for, flash, redirect,send_from_directory, jsonify
import databaseInteraction
import templates
import json
import os

directory = os.path.dirname(os.path.abspath(__file__))


app = Flask(__name__)
app.config['SECRET_KEY'] = "897654534657890"

@app.route("/")
def index():
    return render_template("build.html")

@app.route("/build", methods=("GET","POST"))
def build():
    if request.method == 'POST':
        client = request.form['client']
        user = request.form['user']
        duedate = request.form['duedate']
        ticketno = request.form['ticketno']
        serialno = request.form['serialno']
        ettag = request.form['ettag']
        addnotes = request.form['addnote']
        ticketType = "build" # is needed for the templates to work when applied
        databaseInteraction.add_to_database(client, user, duedate, ticketno, serialno, ettag, addnotes, ticketType)
        return send_from_directory(directory='static',path="output.html")
    return render_template("build.html")

@app.route("/dispose", methods=("GET","POST"))
def dispose():
    if request.method == 'POST':
        client = request.form['client']
        ticketno = request.form['ticketno']
        date = request.form['date']
        device = request.form['device']
        serialno = request.form['serialno']
        ettag = request.form['ettag']
        addnotes = request.form['addnotes']
        ticketType = "dispose"
        databaseInteraction.add_to_database(client,device,date,ticketno,serialno,ettag,addnotes,ticketType)
        return send_from_directory(directory='static',path="output.html")
    return render_template("dispose.html")

@app.route("/repair", methods=("GET","POST"))
def repair():
    if request.method == 'POST':
        client = request.form['client']
        ticketno = request.form['ticketno']
        date = request.form['datereceived']
        ettag = request.form['ettag']
        make = request.form['makemodel']
        serialno = request.form['serialno']
        addnotes = request.form['addnotes']
        ticketType = "repair"
        databaseInteraction.add_to_database(client,make,date,ticketno,serialno,ettag,addnotes,ticketType)
        return send_from_directory(directory='static',path="output.html")
    return render_template("repair.html")

@app.route("/stock", methods=("GET","POST"))
def stock():
    neworused = ['new','used']
    if request.method == 'POST':
        client = request.form['client']
        newused = request.form['neworused']
        date = request.form['datereceived']
        ettag = request.form['ettag']
        device = request.form['device']
        serialno = request.form['serialno']
        addnotes = request.form['addnote']
        ticketType = 'stock'
        databaseInteraction.add_to_database(client,newused,date,device,serialno,ettag,addnotes,ticketType)
        return send_from_directory(directory='static',path="output.html")
    return render_template("stock.html",neworused=neworused)

@app.route("/history")
def history():
    return render_template("history.html")

@app.route('/get_data')
def get_data():
    with open(os.path.join(directory,"Labelinfo.json"), 'r') as file:
        data = json.load(file)
    return jsonify(data)

@app.route("/create_html/<entryname>")
def create_html(entryname):
    databaseInteraction.create_html(entryname)
    return jsonify({"status":"success","entryname":entryname})

@app.route('/run-script')
def run_script():
    databaseInteraction.printpdf()
    return jsonify({'status':'Label printing'})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

# client = request.form['client']
# user = request.form['tbc']
# duedate = request.form['duedate']
# ticketno = request.form['ticketno']
# serialno = request.form['serialno']
# ettag = request.form['ettag']
# addnote = request.form['addnote']