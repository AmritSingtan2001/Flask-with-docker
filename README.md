# Flask JSON Endpoint Application

This is a simple Flask application that receives JSON data via a POST request and returns a response with the received data and a success message.

## Features

- Receives JSON data via a POST request.
- Responds with the received data and a confirmation message.

## Prerequisites

- Python 3.6 or higher
- Flask

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/flask-json-endpoint.git
    cd flask-json-endpoint
    ```

2. Create a virtual environment and activate it:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install Flask
    ```
4. Install the required packages from requirements.txt file:
   ```sh
    pip install -r requirements.txt
    ```
## Usage

1. Run the application:

    ```sh
    python app.py
    ```

2. Send a POST request to the root endpoint (`/`) with JSON data. For example, you can use `curl`:

    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' http://127.0.0.1:5000/
    ```

3. The application will respond with the received data and a confirmation message:

    ```json
    {
        "received": {
            "key": "value"
        },
        "message": "JSON received successfully!"
    }
    ```



## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Acknowledgments

- Flask documentation: https://flask.palletsprojects.com/
