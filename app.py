# # import os
# # from flask import Flask, render_template, request, jsonify, send_from_directory
# # import spacy
# # import pandas as pd
# # import logging

# # app = Flask(__name__)
# # nlp = spacy.load("en_core_web_sm")

# # # Configure logging
# # logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # # Define directory to store downloaded files
# # DOWNLOAD_DIR = "downloads"
# # if not os.path.exists(DOWNLOAD_DIR):
# #     os.makedirs(DOWNLOAD_DIR)

# # @app.route("/")
# # def index():
# #     return render_template("index.html")

# # @app.route("/process_text", methods=["POST"])
# # def process_text():
# #     data = request.get_json()
# #     text = data.get("text", "")
# #     entity_type = data.get("entityType", "all")  # default to "all" if not provided
    
# #     # Log the received text
# #     logging.info(f"Received text: {text}")
    
# #     # Process the text with SpaCy
# #     doc = nlp(text)
    
# #     # Extract entities based on entity type
# #     if entity_type == "all":
# #         entities = [{"text": ent.text, "start": ent.start_char, "end": ent.end_char, "label": ent.label_} for ent in doc.ents]
# #     elif entity_type == "org":
# #         entities = [{"text": ent.text, "start": ent.start_char, "end": ent.end_char, "label": ent.label_} for ent in doc.ents if ent.label_ == "ORG"]
    
# #     # Log the extracted organization entities
# #     print(entities)
# #     logging.info(f"Extracted organization entities: {entities}")
    
# #     # Extract entities of type ORDINAL and create a table
# #     ordinal_entities = []
# #     for ent in doc.ents:
# #         if ent.label_ == "ORDINAL":
# #             ordinal_entities.append({"entity": ent.text, "words_from_text": ent.root.text})
    
# #     # Log the extracted ordinal entities
# #     logging.info(f"Extracted ordinal entities: {ordinal_entities}")
    
# #     # Create DataFrame for the entity table
# #     df = pd.DataFrame(ordinal_entities)
# #     entity_table_html = df.to_html(index=False)
    
# #     # Save entity table as HTML file
# #     filename = "entity_table.html"
# #     file_path = os.path.join(DOWNLOAD_DIR, filename)
# #     df.to_html(file_path, index=False)
    
# #     return jsonify({"org_entities": entities, "entity_table_html": entity_table_html, "file_path": file_path})

# # @app.route("/download/<path:filename>")
# # def download(filename):
# #     return send_from_directory(DOWNLOAD_DIR, filename, as_attachment=True)

# # if __name__ == "__main__":
# #     app.run(host='0.0.0.0',port='5000',debug=True)


# import os
# from flask import Flask, render_template, request, jsonify, send_from_directory
# import spacy
# import pandas as pd
# import logging

# app = Flask(__name__)
# nlp = spacy.load("en_core_web_sm")

# # Configure logging
# logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # Define directory to store downloaded files
# DOWNLOAD_DIR = "downloads"
# if not os.path.exists(DOWNLOAD_DIR):
#     os.makedirs(DOWNLOAD_DIR)

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/process_text", methods=["POST"])
# def process_text():
#     data = request.get_json()
#     text = data.get("text", "")
#     entity_type = data.get("entityType", "all")  # default to "all" if not provided
    
#     # Log the received text
#     logging.info(f"Received text: {text}")
    
#     # Process the text with SpaCy
#     doc = nlp(text)
    
#     # Extract entities based on entity type
#     if entity_type == "all":
#         entities = [{"text": ent.text, "start": ent.start_char, "end": ent.end_char, "label": ent.label_} for ent in doc.ents]
#     elif entity_type == "org":
#         entities = [{"text": ent.text, "start": ent.start_char, "end": ent.end_char, "label": ent.label_} for ent in doc.ents if ent.label_ == "ORG"]
    
#     # Log the extracted organization entities
#     print(entities)
#     logging.info(f"Extracted organization entities: {entities}")
    
#     # Extract entities of type ORDINAL and create a table
#     ordinal_entities = []
#     for ent in doc.ents:
#         if ent.label_ == "ORDINAL":
#             ordinal_entities.append({"entity": ent.text, "words_from_text": ent.root.text})
    
#     # Log the extracted ordinal entities
#     logging.info(f"Extracted ordinal entities: {ordinal_entities}")
    
#     # Create DataFrame for the entity table
#     df = pd.DataFrame(ordinal_entities)
#     entity_table_html = df.to_html(index=False)
    
#     # Save entity table as CSV file
#     csv_filename = "entity_table.csv"
#     csv_file_path = os.path.join(DOWNLOAD_DIR, csv_filename)
#     df.to_csv(csv_file_path, index=False)
    
#     return jsonify({"org_entities": entities, "entity_table_html": entity_table_html, "csv_file_path": csv_file_path})

# @app.route("/download_csv")
# def download_csv():
#     csv_file_path = request.args.get("csv_file_path")
#     if not csv_file_path:
#         return jsonify({"error": "CSV file path not provided"}), 400
    
#     return send_from_directory(os.path.dirname(csv_file_path), os.path.basename(csv_file_path), as_attachment=True)

# if __name__ == "__main__":
#     app.run(host='0.0.0.0',port='5000',debug=True)

import os
from flask import Flask, render_template, request, jsonify, send_from_directory
import spacy
import pandas as pd
import logging

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define directory to store downloaded files
DOWNLOAD_DIR = "downloads"
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process_text", methods=["POST"])
def process_text():
    data = request.get_json()
    text = data.get("text", "")
    entity_type = data.get("entityType", "all")  # default to "all" if not provided
    
    # Log the received text
    logging.info(f"Received text: {text}")
    
    # Process the text with SpaCy
    doc = nlp(text)
    
    # Extract entities based on entity type
    if entity_type == "all":
        entities = [{"text": ent.text, "start": ent.start_char, "end": ent.end_char, "label": ent.label_} for ent in doc.ents]
    elif entity_type == "org":
        entities = [{"text": ent.text, "start": ent.start_char, "end": ent.end_char, "label": ent.label_} for ent in doc.ents if ent.label_ == "ORG"]
    
    # Log the extracted organization entities
    logging.info(f"Extracted organization entities: {entities}")
    
    # Extract entities of type ORDINAL and create a table

    ordinal_entities = [{"entity": ent.text, "words_from_text": ent.root.text} for ent in doc.ents if ent.label_ == "CARDINAL"]
    
    # Log the extracted ordinal entities
    logging.info(f"Extracted ordinal entities: {ordinal_entities}")
    
    # Create DataFrame for the entity table
    df = pd.DataFrame(ordinal_entities)
    
    # Save entity table as CSV file
    csv_filename = "entity_table.csv"
    csv_file_path = os.path.join(DOWNLOAD_DIR, csv_filename)
    df.to_csv(csv_file_path, index=False)
    
    return jsonify({"org_entities": entities, "csv_file_path": csv_file_path})

@app.route("/download_csv")
def download_csv():
    csv_file_path = request.args.get("csv_file_path")
    if not csv_file_path:
        return jsonify({"error": "CSV file path not provided"}), 400
    
    return send_from_directory(os.path.dirname(csv_file_path), os.path.basename(csv_file_path), as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5000',debug=True)
