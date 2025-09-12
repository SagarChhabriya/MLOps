# Flask

1. WSGI: Web Server Gateway Interface
2. Jinja Template Engine



- Flask is a web framework which is created using python programming language. 
- Web Server: Where we are goind to deploy our web applications (developed using Flask).
    - Ex: AWS EC2, Azure App, Apace
    


### Hello World in Flask

```py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask developers"


if __name__=="__main__":
    app.run(debug=True)


# in cmd > python file_name.py

```




