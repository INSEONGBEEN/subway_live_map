
from flask import Flask, render_template, jsonify
import pandas as pd
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stations')
def get_stations():
    df = pd.read_csv('/Users/sayongja/Documents/공모전/subway_live_map/stations.csv')
    return jsonify(df.to_dict(orient='records'))

@app.route('/api/trains')
def get_trains():
    API_KEY = '524e554663646c733131376371794a65'
    lines = ["1호선", "2호선", "3호선", "4호선", "5호선", "6호선", "7호선", "8호선"]
    results = []

    for line in lines:
        url = f"http://swopenapi.seoul.go.kr/api/subway/{API_KEY}/xml/realtimePosition/0/100/{line}"
        res = requests.get(url)
        res.encoding = 'utf-8'
        try:
            root = ET.fromstring(res.text)
            for row in root.findall("row"):
                statn = row.findtext("statnNm")
                results.append({
                    "line": row.findtext("subwayNm"),
                    "station": statn,
                    "trainNo": row.findtext("trainNo"),
                    "dest": row.findtext("statnTnm"),
                    "status": row.findtext("trainSttus")
                })
        except:
            continue

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
