from flask import Flask, request, jsonify
import g4f

app = Flask(__name__)

@app.route('/eva', methods=['POST'])
def process_request():
    data = request.get_json()
    # Extract the relevant fields from the request data
    user_message = data['messages'][1]['content']
    system_message = data['messages'][0]['content']

    # Prepare the chat history 
    response = g4f.ChatCompletion.create(
        model='gpt-3.5-turbo',
        provider=g4f.Provider.Aichat,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ],
      stream = "true",
    )

    print(response)

    
    # Join the response messages into a single string
    result = ''.join(response)
    result = result.replace("OpenAI", "Pharmalite.in")
    result = result.replace("ChatGPT", "PharmaChat")
    result = result.replace("GPT", "PharmaChat")

    # Return the response as a JSON object
    return jsonify({
        "model": "text-davinci-003",
        "object": "chat.completion",
        "choices": [
            {"finish_reason": "stop", "index": 0, "message": {"content": result, "role": "assistant"}}
        ],
        "usage": {"prompt_tokens": 6, "completion_tokens": 39, "total_tokens": 45}
    })

  

@app.route('/', methods=['GET'])
def get_status():
    # Return a simple JSON response indicating the server status
    return jsonify({"status": "Server is running bhencho..!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
