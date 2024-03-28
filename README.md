# ner_application
BITS pilani NLP Application semeseter 3 assignment 2

Named Entity Recognition Application
This application performs Named Entity Recognition (NER) on input text and displays the identified entities, allowing users to download a table containing the identified entities.

Setup
Follow these steps to set up and run the application:

1. Clone the Repository
Clone this repository to your local machine:

git clone https://github.com/your_username/your_repository.git

2. Create a Virtual Environment

cd your_repository
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

Usage
Enter your text in the textarea provided.
Select the entity type (All Entities or Organizations) from the dropdown menu.
Click on "Process Text" to analyze the text and display the identified entities.
Click on "Download Entity Table" to download a CSV file containing the identified entities.
Optionally, use the "Insert Pre-defined Text" button to insert pre-defined text into the textarea.

About
This application is created by Group 8.
