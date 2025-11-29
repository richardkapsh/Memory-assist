MemoryAssist Animal Password

A lightweight Python CLI tool that retrieves a user's saved password from a REST API and displays it in the terminal.

-Features
Sends HTTP GET requests to a RESTful API
Parses JSON responses using Python’s built-in libraries
Simple terminal interface
Handles basic error cases (invalid username, network failure, missing fields)

-Tech Stack
- **Python 3**
- `requests` (for HTTP calls)
- `json` (for parsing API responses)

-Project Structure
- `memory_assist.py` – main script containing all logic

-How to Run
1. Install dependencies:

```bash
pip install requests

2. Clone the repository:

```bash
git clone https://github.com/richardkapsh/Memory-assist

3. Move into the project directory
```bash
cd Memory-assist

4. API Key Requirement

This tool uses the API Ninjas service for retrieving password data.
To run the project, you must generate your own API key:

a. Go to https://api-ninjas.com/
b. Create a free account
c. Generate an API key
d. Export it as the `ANIMAL_API_KEY` environment variable:

**Mac/Linux**
```bash
export ANIMAL_API_KEY="your_api_key_here"


5. Run the script:

```bash
python3 animal_auth_personal.py


- What I Learned
While building this tool, I learned how to interact with an existing REST API using Python’s requests library. I gained experience making HTTP GET requests with query parameters and parsing JSON responses to extract useful information. I also learned how to handle common issues such as invalid keys or unexpected API responses, and how to design a simple terminal interface to display results clearly for the user. This project strengthened my understanding of how client-side programs communicate with web APIs in real-world applications.
