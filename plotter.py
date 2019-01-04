import requests as s
import numpy as np
import collections
import matplotlib.pyplot as plt
from flask import Flask
app = Flask(__name__)

@app.route('/my-first-web-application', methods = ['POST'])

def plotter(current_time, current_endpoint, current_index):

    headers{'Content-type': 'application/json'}
    url = current_endpoint + current_index + '/_search'
    query = {'query': {'term': {'timestampGMT': current_time}}}

    r = s.get(url, data=query, headers=headers) # requests.get, post, and delete have similar syntax

    timeTemperature = map(
        lambda y: y['temperature'], r
    )

    hist = collections.Counter(timeTemperature)

    plot = plt.bar(np.array(hist.keys())-0.4, hist.values()); plt.show()

    return render('./plot.png', plot)

if __name__ == '__main__':
    app.run()
