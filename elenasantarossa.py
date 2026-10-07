from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    cartella_foto = os.path.join(app.static_folder, 'opere')  
    if os.path.exists(cartella_foto):
            foto_list = os.listdir(cartella_foto)
            foto_list = [f for f in foto_list if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    else:
            foto_list = []
    
    return render_template("index.html", foto_list=foto_list)
if __name__ == "__main__":
    app.run(debug=True)