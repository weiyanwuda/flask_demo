# This is a simple example web app that is meant to illustrate the basics.
from flask import Flask, render_template, redirect, g, request, url_for, jsonify, json
import urllib
import requests  # similar purpose to urllib.request, just more convenience

app = Flask(__name__)


@app.route("/")
def show_list():
    resp = requests.get("http://74.105.240.195:5001/api/items")
    resp = resp.json()
    return render_template('index.html', todolist=resp)


@app.route("/add", methods=['POST'])
def add_entry():
    requests.post("http://74.105.240.195:5001/api/items", json={
                  "what_to_do": request.form['what_to_do'], "due_date": request.form['due_date']})
    return redirect(url_for('show_list'))


@app.route("/delete/<item>")
def delete_entry(item):
    item = urllib.parse.quote(item)
    requests.delete("http://74.105.240.195:5001/api/items/"+item)
    return redirect(url_for('show_list'))


@app.route("/mark/<item>")
def mark_as_done(item):
    item = urllib.parse.quote(item)
    requests.put("http://74.105.240.195:5001/api/items/"+item)
    return redirect(url_for('show_list'))


if __name__ == "__main__":
    app.run("0.0.0.0")
