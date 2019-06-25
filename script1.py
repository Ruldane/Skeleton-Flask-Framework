from flask import  Flask, render_template #render_template to insert html template

# need to name script1.py
# instance of the object Flask
app=Flask(__name__)

#home page
@app.route('/')
def home():
    return render_template("index.html")

#About page
@app.route('/about/')
def about():
    return render_template("about.html")

# case 1 - script executed
# __name__ = "__main__"
if __name__ == '__main__':
    app.run(debug=True)

