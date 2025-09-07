from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    greetings = '<p>hello <strong><em>sir</em></strong> how you doing</p>'
    link = '<a href = "user/Ateeksh">click me!</a>'
    
    return greetings + link

@app.route("/user/<name>")
def greeting(name):
    idk = f'hello {name} what are you doing ???<br>'
    instruction = '<p> please change the name on the browser side according to ur wish'
    
    return idk+instruction

if __name__ == "__main__":
    app.run(debug = True)