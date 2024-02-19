# Book Recommender Web App

## Project Title: Book Recommender

### Description:
The Book Recommender is a web application built using Flask, HTML, and CSS. It allows users to enter the name of a book and receive recommendations for similar books along with their authors and cover images. The application utilizes a simple Flask server to handle user requests, fetch recommendations from a recommendation function, and render the recommendations on the frontend.

Features:

- Users can enter the name of a book in a search field.
- Upon submitting the form, the application displays a list of recommended books, including their titles, authors, and cover images.
- The application provides a visually appealing user interface with a responsive design.
- Background image support enhances the aesthetics of the application.
- The Flask backend efficiently handles user requests and serves the appropriate responses.
Usage:

- Enter the name of a book in the search field.
- Click the "Get Recommendations" button.
- View the list of recommended books with their titles, authors, and cover images.

### How to Start:

#### For Mac:

1. Create a virtual environment:
   ```bash
   python3 -m venv env

2. Activate the virtual environment:
   ```bash
   source env/bin/activate #Mac
   .\env\Scripts\activate  #windows

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Start the Flask app:
   ```bash
   python app.py

Once the Flask app is running, you can access it through your web browser by navigating to http://localhost:5000/.
