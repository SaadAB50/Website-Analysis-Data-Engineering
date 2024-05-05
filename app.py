from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from crawler import fetch_and_analyze
from datetime import datetime

app = Flask(__name__)

# Setup MongoDB connection
client = MongoClient('localhost', 27017, username='crawlerUser', password='securePassword123')
db = client.web_analysis
page_analysis = db.page_analysis

@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    url = request.json.get('url') if request.is_json else request.form.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400

    # Check if the URL has already been analyzed
    existing_data = page_analysis.find_one({"url": url})
    if existing_data:
        # Convert MongoDB document to standard output format
        formatted_data = format_data(existing_data)
        return jsonify({"message": "Data retrieved from database", "data": formatted_data}), 200

    # Perform new analysis
    analysis = fetch_and_analyze(url)
    if "error" in analysis:
        return jsonify({"error": analysis["error"]}), 500

    # Save new analysis result in MongoDB
    document_id = save_data(url, analysis)
    return jsonify({"message": "Data saved successfully!", "id": str(document_id), "analysis": analysis}), 201

def save_data(url, analysis):
    analysis_document = {
        "url": url,
        "title": analysis.get('title', 'No title available'),
        "crawl_date": datetime.now(),
        "total_images": analysis.get('total_images', 0),
        "images_with_alt": analysis.get('images_with_alt', 0),
        "images_without_alt": analysis.get('images_without_alt', 0),
        "meta": analysis.get('meta', {"description": "", "keywords": []})
    }
    result = page_analysis.insert_one(analysis_document)
    return result.inserted_id

def format_data(data):
    # Ensuring all necessary fields are present
    return {
        "title": data.get('title', 'No title available'),
        "total_images": data.get('total_images', 0),
        "images_with_alt": data.get('images_with_alt', 0),
        "images_without_alt": data.get('images_without_alt', 0),
        "meta": data.get('meta', {"description": "", "keywords": []})
    }

if __name__ == '__main__':
    app.run(debug=True)
