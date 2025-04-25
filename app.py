from flask import Flask, render_template,request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/QA',methods=['GET','POST'])
def QA():
    keys = 'AIzaSyCnGPWQw_QVP_PFxn6rDszLg1zbWk-cp_A'
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={keys}'

    head = {
    'Content-Type':'application/json'
    }

    
    if request.method == 'POST':
        propts = request.form.get('inputs')

        data = {
        "contents": [{
        "parts":[{"text": propts}]
            }]
        }

        responce = requests.post(url=url,headers=head,json=data)
        if responce.status_code == 200:
            ds = responce.json()
            res = ds["candidates"][0]["content"]["parts"][0]["text"]
            return render_template('QA.html',inputs=propts,ai=res)
    return render_template('QA.html')

if __name__ == '__main__':
    app.run(debug=True)