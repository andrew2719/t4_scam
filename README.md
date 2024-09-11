# FastAPI Message App

This is a simple message application built with FastAPI, allowing users to type and view messages.

## Project Structure

```
t4_scam/
│
├── static/
│   └── (empty for now)
│
├── templates/
│   ├── index.html
│   ├── type.html
│   └── view.html
│
├── main.py
└── README.md
```

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/andrew2719/t4_scam.git
   cd t4_scam
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

Start the FastAPI server: this allows every ip to interact
   ```
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```


## Usage

- The home page (`/`) provides links to type a message or view messages.
- Click on "Type a message" to access the `/type` page where you can submit new messages.
- Click on "View messages" to see all submitted messages on the `/view` page.
- The view page automatically refreshes every 5 seconds to show new messages.

## Files

- `main.py`: Contains the FastAPI application and route handlers.
- `templates/index.html`: The home page template.
- `templates/type.html`: The page for typing and submitting messages.
- `templates/view.html`: The page for viewing all messages with auto-refresh functionality.
- `static/`: Directory for static files (currently empty, can be used for CSS, JavaScript, etc.).

## Notes

- This application uses in-memory storage for messages, so they will be lost when the server restarts.
- For production use, consider implementing a database for persistent storage.

## Contributing

Feel free to fork this repository and submit pull requests to contribute to this project.

## usage
Upload in cloud and celebrate