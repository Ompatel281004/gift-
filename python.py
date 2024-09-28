from flask import Flask, request, render_template
import os
import google.generativeai as genai

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    genai.configure(api_key="AIzaSyDSmRduNeU9zUT_g9HhWxCP7BMQd5mFV7w")
    

    # Create the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-exp-0827",
    generation_config=generation_config
    #safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    chat_session = model.start_chat(
    history=[]
    )

    if request.method == 'POST':
        user_input = request.form['age']
        user_input1 = request.form['gender']
        user_input2 = request.form['occasion']
        user_input3 = request.form['relationship']
        user_input4 = request.form['budget']
        user_input5 = request.form['preferences']

        print(f'Input received: {user_input}')  # Print to console
        # print(f'Input received: {user_input1}')
        # print(f'Input received: {user_input2}')
        # print(f'Input received: {user_input3}')
        # print(f'Input received: {user_input4}')
        # print(f'Input received: {user_input5}')

        alluser_input=f'give suggestion for gifts on given criteria, age:{user_input}, gender:{user_input1}, ocassion:{user_input2}, relationship:{user_input3}, budget:{user_input4}, preference:{user_input5}'
        
        print(f'Input received: {alluser_input}')


        query=alluser_input
        response = chat_session.send_message(query)
        print(response.text)
        return f'You entered: {alluser_input}'
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    







