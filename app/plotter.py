import os
import requests
import numpy as np
import collections
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import json
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/plot_data", methods=["POST"])
def plot_data():
    if request.method == "POST":
        minutesToView = request.form["minutesToView"]
        endpoint = request.form["endpoint"]
        index = request.form["index"]
        headers = {"Content-Type": "application/json"}
        url = endpoint + index + "/_search"
        then = "now" + "-" + str(minutesToView) + "m"
        query = {
                "query": {
                    "bool": {
                        "filter": {
                            "range": {
                                "metadata.time": {
                                    "gte": then,
                                    "lt":  "now"
                                }
                            }
                        }
                    }
                }
        }
        url = endpoint + index + "/_search"
        query_str = json.dumps(query)
        request_details = {"url": url, "query": query_str, "headers": headers}
        response = requests.get(request_details["url"], data=request_details["query"], headers=request_details["headers"])
        json_response = json.loads(response.content)
        sources = json_response['hits']['hits']
        temperatures = pd.DataFrame(data=None, columns=['temperature', 'time'])
        for source in range(len(sources)):
            keys = sources[source]['_source']['payload_fields'].keys()
            if 'temperature' in keys:
                temperatures.at[source,['temperature']] = sources[source]['_source']['payload_fields']['temperature']
                temperatures.at[source,['time']] = sources[source]['_source']['metadata']['time']
        plt.bar(range(len(temperatures['time'])),temperatures['temperature'])
        plt.xticks(range(len(temperatures['time'])), temperatures['time'], rotation='vertical')
        plt.tight_layout()
        plt.savefig("./static/plot.png")

        return render_template("index.html")

if __name__ == "__main__":
    app.run()
