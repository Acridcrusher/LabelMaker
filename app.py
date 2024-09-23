from flask import Flask, render_template, request, url_for, flash, redirect,send_from_directory
import templates
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "897654534657890"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/build.html", methods=("GET", "POST")) # done
def build():
    if request.method == 'POST':
        client = request.form['client']
        user = request.form['user']
        duedate = request.form['duedate']
        ticketno = request.form['ticketno']
        serialno = request.form['serialno']
        ettag = request.form['ettag']
        addnote = request.form['addnote']
        templates.buildLabel(client,user,duedate,ticketno,serialno,ettag,addnote)
        return redirect(f"./history/{ticketno}.html")
    return render_template("build.html")

@app.route("/repair.html") # done
def repair():
    if request.method == 'POST':
        client = request.form['client']
        ticketno = request.form['ticketno']
        date = request.form['datereceived']
        ettag = request.form['ettag']
        makemodel = request.form['makemodel']
        serialno = request.form['serialno']
        addnotes = request.form['addnotes']
        templates.repairLabel(client,ticketno,date,ettag,makemodel,serialno,addnotes)
        return redirect(f"./history/{ticketno}.html")
    return render_template("repair.html")

@app.route("/stock.html", methods=("GET", "POST")) # done
def stock():
    neworused = ['new','used']
    if request.method == 'POST':
        client = request.form['client']
        NorU = request.form['neworused']
        date = request.form['datereceived']
        ettag = request.form['ettag']
        device = request.form['device']
        serialno = request.form['serialno']
        addnote = request.form['addnote']
        templates.stockLabel(client, NorU,date,ettag,device,serialno,addnote)
        return redirect(f"./history/stock-{client}.html")
    return render_template("stock.html", neworused=neworused)

@app.route("/dispose.html")
def dispose():
    if request.method == 'POST':
        client = request.form['client']
        ticketno = request.form['ticketno']
        date = request.form['date']
        device = request.form['device']
        serialno = request.form['serialno']
        ettag = request.form['ettag']
        addnotes = request.form['addnotes']
        templates.stockLabel(client,ticketno,date,ettag,device,serialno,addnotes)
        return redirect(f"./history/{ticketno}.html")
    return render_template("dispose.html")

@app.route("/history.html")
def history():
    directory = "./history"
    files = os.listdir(directory)
    return render_template("history.html", files=files)

@app.route("/history/<filename>")
def open_file(filename):
    directory = "./history"
    return send_from_directory(directory,filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)