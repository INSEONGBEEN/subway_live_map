from flask import Flask, render_template, jsonify
import pandas as pd
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

# 역 이름 정규화 함수
def normalize_station_name(name):
    return name.split('(')[0].strip()

@app.route('/')
def index():
    return render_template("index.html", folium_map='')

@app.route('/api/stations')
def get_stations():
    df = pd.read_csv('./data/station.csv', encoding='cp949')
    df['호선명'] = df['호선'].astype(str).str.strip() + '호선'
    return jsonify(df.to_dict(orient='records'))

@app.route('/api/trains')
def get_trains():
    import urllib.parse

    API_KEY = '544a595858646c7338337545527652'
    df = pd.read_csv('./data/station.csv', encoding='cp949')
    df['호선명'] = df['호선'].astype(str).str.strip() + '호선'
    station_coords = {row['역명']: (row['위도'], row['경도']) for _, row in df.iterrows()}
    results = []

    for line in df['호선명'].unique():
        try:
            encoded_line = urllib.parse.quote(line)
            url = f"http://swopenapi.seoul.go.kr/api/subway/{API_KEY}/xml/realtimePosition/0/100/{encoded_line}"
            res = requests.get(url)
            res.encoding = 'utf-8'

            # 응답이 XML이 아니면 스킵
            if not res.text.strip().startswith("<?xml"):
                print(f"[응답 오류] {line}: {res.text[:100]}")
                continue

            root = ET.fromstring(res.text)

            for row in root.findall("row"):
                statn = row.findtext("statnNm").strip()
                if statn in station_coords:
                    lat, lon = station_coords[statn]
                    results.append({
                        "line": line,
                        "station": statn,
                        "trainNo": row.findtext("trainNo"),
                        "dest": row.findtext("statnTnm"),
                        "status": row.findtext("trainSttus"),
                        "lat": lat,
                        "lon": lon
                    })

        except Exception as e:
            print(f"[ERROR] {line}: {e}")

    return jsonify(results)
if __name__ == '__main__':
    app.run(debug=True)
