from flask import Flask, render_template, jsonify, request
from config_db import BD
from producto import Producto

app = Flask(__name__)
bd = BD()
product = Producto()

@app.route("/")
@app.route("/index")
def index_view():
    return render_template("index.html")

@app.route("/productos")
def get_productos():
    productos = product.select()
    return jsonify(productos)

@app.route("/productos/", methods=["POST"])
def post_productos():
    datos_producto = request.get_json
    resultado = product.insert(datos_producto)
    return jsonify(resultado)

@app.route("/productos/<id>", methods=["PUT"])
def put_productos(id):
    datos_producto = request.get_json
    resultado = product.update(id, datos_producto)
    return jsonify(resultado)    

@app.route("/productos/<id>", methods=["DELETE"])
def delete_productos(id):
    resultado =product.delete(id)
    return jsonify(resultado)

@app.route("/productos/<id>", methods = ["GET"])
def get_by_id(id):
    producto = product.select_by_id(id)
    return jsonify(producto)

if __name__ == "__main__":
    bd.crear_tabla()
    app.run(debug=True)