from flask import Flask, render_template
import flask_sqlalchemy

app = Flask(__name__,
            static_folder="../frontend/dist/static",
            template_folder="../frontend/dist"
            )

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.db'
app.config['SECRET_KEY'] = 'secret_key'

db = flask_sqlalchemy.SQLAlchemy(app)

@app.route('/',defaults={'path':''})
@app.route('/<path:path>')

def index(path):
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)
