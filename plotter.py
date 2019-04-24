import requests
import numpy as np
import collections
import matplotlib.pyplot as plt
import json
from flask import Flask
app = Flask(__name__)

@app.route('/my-first-web-application', methods = ['POST'])

def get_data(minutesToView, endpoint, index):

    headers = {'Content-Type': 'application/json'}

    url = endpoint + index + '/_search'

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

    return {"url": url, "query": query_str, "headers": headers}

def API_request():

    response = requests.get(get_data()["url"], data=get_data()["query"], headers=get_data()["headers"])

    return response

def plot_data():

    timeTemperature = map(
        lambda y: y['temperature'], API_request()
    )

    hist = collections.Counter(timeTemperature)

    plot = plt.bar(np.array(hist.keys())-0.4, hist.values()); plt.show()

    return render('./plot.png', plot)

if __name__ == '__main__':
    app.run()
