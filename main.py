from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
from transformers import T5ForConditionalGeneration, T5Tokenizer

app = Flask(__name__)

# Load T5 model and tokenizer
model_name = "t5-base"
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

@app.route('/text_summarization', methods=['POST'])
def text_summarization():
    data = request.json
    text = data['text']
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, max_length=150, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return jsonify({'summary': summary})

@app.route('/web_summarization', methods=['POST'])
def web_summarization():
    data = request.json
    url = data['url']
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        paragraphs = soup.find_all('p')
        for p in paragraphs:
            print("********** Paragraph: ", p)
        text = ' '.join([p.text for p in paragraphs])
        print("Tokens: ", text)
        inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = model.generate(inputs, max_length=150, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
