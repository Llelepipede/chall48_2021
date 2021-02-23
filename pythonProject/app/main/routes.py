from flask import Blueprint, render_template, redirect, url_for, request
from app.extensions import mongo

main = Blueprint('main', __name__)

fs =


@main.route('/')
def index():
    return render_template("index.html")


@main.route('/ajout_images', methods=['POST'])
def ajout_images():
    if 'image' in request.files:
        print("ok")
        image = request.files['image']
        mongo.save_file(image.filename, image)
        mongo.db.equipe40.insert_one({
            'image_name': image.filename
        })

    return redirect(url_for('main.index'))


@main.route('/bibliotheque')
def bibliotheque():

    return render_template('biblio.html', list=mongo.db.fs.chunck.find({}))


