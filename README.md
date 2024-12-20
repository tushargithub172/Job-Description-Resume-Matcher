# Job Description and Resume Matcher

This project is a web-based application that uses Machine Learning and Natural Language Processing (NLP) techniques to match job descriptions with uploaded resumes. It streamlines the recruitment process by identifying the best candidates for a given role and provides insights for job seekers to improve their resumes.

---

## Project Structure

```
RESUMEMATCHINGSYSTEM/
├── input resume/          # Folder for storing user-uploaded resumes
├── instance/              # Instance folder for app-specific files
├── templates/             # HTML templates for the web application
│   ├── index.html         # Main page for input
│   ├── results.html       # Results page for displaying matches
├── uploads/               # Directory for uploaded files
├── Dockerfile             # Docker configuration for containerizing the app
├── job des.txt            # Sample job description file
├── main.py                # Main Flask application
├── models.py              # Python script containing ML/NLP logic
├── requirements.txt       # Dependencies for the project
```

---

## Features

- **Job Description Input**: Users can input job descriptions in a text area.
- **Resume Upload**: Upload one or more resumes in supported formats.
- **Resume Matching**: Uses NLP to score resumes based on relevance to the job description.
- **Results**: Displays compatibility scores and recommendations in an easy-to-read format.
- **Containerization**: Dockerized application for consistent deployment.

---

## Installation and Setup

### Prerequisites
- Python 3.7+
- Docker (optional, for containerization)

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/Job-Description-Resume-Matcher.git
   cd Job-Description-Resume-Matcher
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

4. Access the application at `http://127.0.0.1:5000` in your web browser.

---

## Docker Setup

1. Build the Docker image:
   ```bash
   docker build -t resume-matcher .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 resume-matcher
   ```

3. Access the application at `http://127.0.0.1:5000`.

---

## Usage

1. Open the web application in your browser.
2. Enter a job description in the provided text area.
3. Upload resumes using the "Choose Files" button.
4. Click on the "Match Resumes" button.
5. View the results, including compatibility scores and recommendations.

---

## Technologies Used

- **Frontend**: HTML, CSS
- **Backend**: Flask (Python)
- **ML/NLP**: Libraries such as NLTK, Scikit-learn
- **Containerization**: Docker

---

## Directory Details

- **`main.py`**: Contains the Flask application logic, including routes and backend processing.
- **`models.py`**: Implements the NLP model for resume and job description matching.
- **`templates/index.html`**: Frontend page for inputting job descriptions and uploading resumes.
- **`templates/results.html`**: Displays results to the user.
- **`requirements.txt`**: Specifies the dependencies needed for the project.
- **`Dockerfile`**: Contains instructions to build a Docker image for the project.

---

## Future Enhancements

- Adding support for more file formats.
- Enhancing the NLP model for better accuracy.
- Adding user authentication for secure usage.
- Providing downloadable reports of results.

---

## Acknowledgements

Developed by Tushar | BCA
