# 🚇 실시간 서울 지하철 위치 시각화 시스템

@injjang  
2025.05 ~ 2025.05

---

## 🔗 Live Demo  
https://subway-live-map.onrender.com/

## 📂 GitHub Repository  
https://github.com/INSEONGBEEN/subway_live_map

## 📘 Dev Log  
https://lnjjang.tistory.com/

---

## 📌 프로젝트 개요  
서울시 공공데이터 OpenAPI를 통해 실시간 지하철 위치 정보를 수집하고,  
역별 좌표와 연계하여 **현재 운행 중인 열차 위치를 지도 위에 시각화**합니다.  

Folium 기반 웹 지도를 Flask로 서비스하며, Render를 활용해 배포하였습니다.

---

## 🛠️ 주요 기능  

- `서울열린데이터광장` 실시간 열차 위치 API 연동
- CSV 기반 역별 위경도 매핑 및 호선별 색상 시각화
- 실시간 운행 중 열차 아이콘 시각화
- 지하철 호선별 수동 노선도 정의 및 지도 연결
- `.env` 파일을 통한 API KEY 보안 관리
- Render를 이용한 Flask App 배포

---

## 🧱 기술 스택  

| Category       | Tools                                |
|----------------|--------------------------------------|
| Language       | Python                               |
| Web Backend    | Flask                                |
| Visualization  | folium                               |
| Data Handling  | pandas, requests, xml.etree          |
| Deployment     | Render                               |
| Utilities      | python-dotenv, gunicorn              |

---

## 🗂️ 디렉토리 구조

```
📁 subway_live_map
├── app.py
├── requirements.txt
├── .env (배포 제외)
├── /data
│   └── station.csv
├── /static
│   └── subway.js
└── /templates
    └── index.html
```

---

## 🚀 실행 예시

- 페이지 접속 시 자동으로 실시간 열차 위치 불러오기
- 각 열차는 해당 호선 색상으로 원형 아이콘 표시
- Folium 지도 위에 전체 역 위치 및 노선 폴리라인 표시

---

## 🔧 보완할 점 & 향후 아이디어

| 한계점 | 보완 아이디어 |
|--------|----------------|
| 실시간 위치 정밀도 부족 | 각 열차의 진행 방향/속도 추정 로직 보완 |
| API 호출 제한 | 서비스 등록을 통해 호출량 상향 예정 |
| 수동 노선 연결 유지보수 | OSM 지하철 라인 데이터 자동 연동 검토 |
| 역명 불일치 가능성 | 역명 정규화 및 유사도 기반 대응 추가 |

---

## ✍️ 느낀 점

- Flask를 활용한 경량 웹 서비스 구성 경험
- 공공데이터 API와 좌표 기반 지도 시각화의 융합 가능성 체감
- 간단한 로직이지만 실시간성이 더해져 사용자에게 직관적 정보를 제공한다는 점이 흥미로웠음
- 배포 시 `.env` 설정, Render 환경변수 등록 등 실제 서비스 관점 고려가 유의미했음
