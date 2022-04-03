from flask import Flask, render_template, request, jsonify
import os
import pymongo
from flask_pymongo import PyMongo
from traccing import tracing, opentracing_tracer
import opentracing

from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

app.config["MONGO_DBNAME"] = "example-mongodb"
app.config[
    "MONGO_URI"
] = "mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb"

mongo = PyMongo(app)


@app.route("/")
@tracing.trace()
def homepage():
    span = tracing.get_span()
    opentracing_tracer.inject(span, opentracing.Format.TEXT_MAP, 'hello world')
    # Log para incluir o evento no Jaeger
    span.log_kv({'event': 'Carregando os dados da pessoa.'})
    return "Hello World"


@app.route("/api")
def my_api():
    answer = "something"
    return jsonify(repsonse=answer)


@app.route("/star", methods=["POST"])
def add_star():
    star = mongo.db.stars
    name = request.json["name"]
    distance = request.json["distance"]
    star_id = star.insert({"name": name, "distance": distance})
    new_star = star.find_one({"_id": star_id})
    output = {"name": new_star["name"], "distance": new_star["distance"]}
    return jsonify({"result": output})


if __name__ == "__main__":
    app.run()
