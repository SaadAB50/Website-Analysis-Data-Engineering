# Website-Analysis-Data-Engineering
# Image Alt Tag Analyzer

## Overview
The Image Alt Tag Analyzer is a web application designed to analyze web pages and provide a detailed breakdown of image elements, specifically focusing on the presence or absence of `alt` attributes. It helps in assessing the accessibility and SEO friendliness of web pages.

## Features
- **Web Crawling**: Fetches web pages and analyzes all image tags.
- **Image Analysis**: Reports total images, images with `alt` tags, and images without `alt` tags.
- **Metadata Extraction**: Retrieves and displays the title, meta description, and meta keywords of web pages.
- **Data Storage**: Stores analysis results in a MongoDB database for future retrieval.
- **Front-End Interface**: Provides a user-friendly web interface to input URLs for analysis and view results in a tabulated format.

## Technology Stack
- **Flask**: Serves the backend and the web interface.
- **MongoDB**: Handles data storage and retrieval.
- **Python**: Backend programming language.
- **HTML/CSS/JavaScript**: Front-end technologies for the user interface.

## Prerequisites
Before you can run the application, ensure you have the following installed:
- Python 3.6+
- MongoDB
- Flask
- PyMongo
- BeautifulSoup

## Setup Instructions
- Clone the repository
- Start MongoDB:
Ensure MongoDB is running on your system. You can typically start MongoDB with: mongod
- Run the Flask Application
Start the application by executing:
python app.py
- Access the Web Interface
Open a web browser and navigate to:
http://localhost:5000/
- Use the provided form to submit URLs for analysis. Results will be displayed on the same page under the form.

- Running the Application
Once everything is set up, the application will be accessible via a web browser at `http://localhost:5000/`. Enter a URL in the form and click the "Analyze" button to view the analysis of image tags including `alt` attributes.

## Notes
- Ensure that MongoDB service is running before starting the Flask app.
- Check Python and library versions if you encounter any compatibility issues.

## Support
For support, contact saad.ahmed.bari@gmail.com or open an issue in the GitHub repository.
