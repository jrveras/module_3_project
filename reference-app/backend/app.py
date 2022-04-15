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
    with opentracing.tracer.start_span('welcome', child_of=span) as span_child:
        answer = "Welcome My Home Page!!!"
        span_child.log_kv({'event': '[HOMEPAGE] Tracing Welcome Answer.'})
        span_child.set_tag("lenght_answer", len(answer))
    span.log_kv({'event': '[HOMEPAGE] Tracing Home Page!'})
    return answer


@app.route("/api")
@tracing.trace()
def my_api():
    span = tracing.get_span()
    
    with opentracing.tracer.start_span('answer', child_of=span) as span_child:
        answer = "something"
        span_child.log_kv({'event': '[MY_API] Tracing My API Answer.'})
        span_child.set_tag("lenght_answer", len(answer))
    
    span.log_kv({'event': '[MY_API] Tracing Something!'})
    
    return jsonify(repsonse=answer)

@app.route("/health")
@tracing.trace()
def health():
    span = tracing.get_span()
    span.log_kv({'event': '[HEALTH] Tracing Health!'})
    status = "It's UP!!!"
    return jsonify(repsonse=status)


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
