# ner_application
BITS pilani NLP Application semeseter 3 assignment 2

Named Entity Recognition Application <br>
This application performs Named Entity Recognition (NER) on input text and displays the identified entities, allowing users to download a table containing the identified entities.

Setup <br>
Follow these steps to set up and run the application:

1. Clone the Repository
Clone this repository to your local machine:

git clone https://github.com/Mrjaggu/ner_application.git

2. Create a Virtual Environment

cd ner_application
virtualenv venv

Activate the virtual environment:

On Windows:
 venv\Scripts\activate

On macOS and Linux:
 source venv/bin/activate

3. Install Dependencies
Install the required Python packages using pip:
 pip install -r requirements.txt

4. Run the Application
Run the Flask application:
 python app.py

The application will start running on http://localhost:5000/.

5. Access the Application
Open your web browser and navigate to http://localhost:5000/ to access the application.

Usage<br>
1. Enter your text in the textarea provided.
2. Select the entity type (All Entities or Organizations) from the dropdown menu.
3. Click on "Process Text" to analyze the text and display the identified entities.
4. Click on "Download Entity Table" to download a CSV file containing the identified entities.
5. Optionally, use the "Insert Pre-defined Text" button to insert pre-defined text into the textarea.

About <br>
This application is created by Group 8.
