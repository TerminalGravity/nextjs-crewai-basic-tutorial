# API Documentation

## Introduction
This document outlines the structure and functionality of the API endpoints within our application. It includes details on standard library imports, third-party imports, local application/library specific imports, and the Flask application setup with CORS policy. Additionally, it describes the available API routes, their methods, expected inputs, and outputs.

### Standard Library Imports
- `datetime` from the `datetime` module is used for handling date and time-related operations.
- `json` is imported for parsing JSON data.
- `Thread` from the `threading` module is utilized for running operations in separate threads.
- `uuid4` from the `uuid` module generates unique identifiers.

### Related Third-Party Imports
- `Flask`, `jsonify`, `request`, `abort`, and `send_file` from the `flask` package are used for creating the web application and handling HTTP requests and responses.
- `CORS` from the `flask_cors` package is used to handle Cross-Origin Resource Sharing (CORS).
- `load_dotenv` from the `dotenv` package loads environment variables.
- `pandas` as `pd` is used for data manipulation and analysis.

### Local Application/Library Specific Imports
- `CompanyResearchCrew` from the `crew` module is a custom class for handling company research operations.
- `append_event`, `jobs`, `jobs_lock`, and `Event` from the `job_manager` module are used for job management and event logging.
- `logger` from the `utils.logging` module is used for logging.

### Flask Application Setup
- The Flask application is initialized.
- CORS policy is set to allow all origins for routes under `/api/*`.

### API Routes

#### Download Report
- Route: `/api/download_report/<job_id>`
- Method: `GET`
- Description: Allows downloading a report for a specific job ID. The report can be in CSV format. The route assumes a function `get_job_data` retrieves the job's data, which is then converted to a CSV file and sent as a downloadable file.

#### Kickoff Crew
- Function: `kickoff_crew(job_id, companies, positions)`
- Description: Initiates the company research crew with the provided job ID, companies, and positions. Logs the start and completion of the crew. Handles exceptions by logging errors and updating the job status to 'ERROR'. Upon successful completion, updates the job status to 'COMPLETE' and logs the event.

#### Run Crew
- Route: `/api/crew`
- Method: `POST`
- Description: Receives a request to run the crew with specified companies and positions. Validates the input data and starts a new thread to kickoff the crew. Returns a JSON response with the job ID.

#### Get Status
- Route: `/api/crew/<job_id>`
- Method: `GET`
- Description: Retrieves the status of a specific job ID. Locks the job management to safely access the job's details. Parses the job result into a JSON object if possible. Returns a JSON response with the job ID, status, result, and events.

### Running the Application
- The Flask application is configured to run in debug mode on port 3001.

