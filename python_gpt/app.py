from openai import OpenAI
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
client = OpenAI(api_key="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")
system="""
너는 음식점 AI야
아래는 음식 종류 아래종류의 메뉴 말고 다른 메뉴는 없어
-삼겹살
-대패 삼겹살
-물냉
삼겹살은 1인분에 5000원.
"""

message =[{"role" : "system"
           ,"content" : system}]
def ask(text):
    user_input = {"role":"user", "content": text}
    message.append(user_input)
    resp = client.chat.completions.create(
        model='gpt-3.5-turbo'
        ,messages=message)
    bot_text = resp.choices[0].message.content
    bot_resp={"role":"assistant","content":bot_text}
    message.append(bot_resp)
    return bot_text
@app.route('/')
def index():
    return render_template('chat.html')
@app.route('/ask', methods=['POST'])
def handler_ask():
    user_input = request.json['text']
    resp = ask(user_input)
    return jsonify({'response': resp})

if __name__ == '__main__':
    app.run(debug=True)
