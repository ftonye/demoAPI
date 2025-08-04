from flask import Flask,request


app = Flask(__name__)




@app.route("/")
def startServer():
    return '<h1>PI SmartHome API has started</h1>'

@app.route("/updateFrontDoor")
def updateFrontDoor():
    rep = int(request.args.get("state"))
    #faire une mise a jours dansla bd
    #rn utilisant la valeur de rep

    if rep == 1:
        return 'La porte est ouverte'
    elif rep == 0:
        return 'La porte est ferme'