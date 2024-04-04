from flask import Flask, request, jsonify, render_template
from transformers import pipeline, BartTokenizer, BartForConditionalGeneration

app = Flask(__name__)

# Initialize BART tokenizer and model
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

# Create a text summarization pipeline
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.get_json()
    input_text = data.get('text', '')

    # Generate the summary
    summary = summarizer(input_text, max_length=75, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)

    return jsonify({'summary': summary[0]['summary_text']})

#if __name__ == "__main__":
    #app.run(debug=True)
