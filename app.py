from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# 데이터 불러오기
data = pd.read_csv('cox-violent-parsed_filt_usable.csv')

# 데이터 분석 및 시각화
# 예시: 나이에 따른 폭력적 재범 여부 시각화
age_vs_violent_recid = data.groupby('age')['is_violent_recid'].mean()
plt.plot(age_vs_violent_recid)
plt.xlabel('Age')
plt.ylabel('Mean of Violent Recidivism')
plt.title('Age vs. Violent Recidivism')
plt.savefig('graph.py')  # 그래프를 파일로 저장

@app.route('/')
def index():
    # 그래프 파일을 HTML에 삽입하여 웹페이지에 표시
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return render_template('index.html', graph=graph_url)

if __name__ == '__main__':
    app.run(debug=True)
