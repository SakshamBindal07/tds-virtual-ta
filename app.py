from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

@app.route('/api/', methods=['POST'])
def answer():
    data = request.get_json()
    question = data.get('question')
    image_b64 = data.get('image')

    image_status = "No image received."
    if image_b64:
        try:
            image_bytes = base64.b64decode(image_b64)
            image_status = f"Image received ({len(image_bytes)} bytes)."
        except Exception as e:
            image_status = f"Error decoding image: {e}"

    return jsonify({
        "answer": f"You asked: {question} | {image_status}",
        "links": []
    })

if __name__ == '__main__':
    app.run(debug=True)
