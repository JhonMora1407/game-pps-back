# Game PPP Back

Brief description of the project. This is a Rock-Paper-Scissors game where the player who wins 3 rounds first is the winner.

## Requirements

- Docker and Docker Compose (for the Docker option)
- Python 3.x (for the local option)
- pip (for the local option)

## Start the Project with Docker Compose

1. Make sure you have Docker and Docker Compose installed on your machine. You can download and install them from here.

2. Build and start the services defined in `docker-compose.yml`:
    ```sh
    docker-compose up --build
    ```

3. Access the application in your browser at `http://localhost:8000` (or the port you have configured).

## Start the Project Locally

1. Make sure you have Python and pip installed on your machine.

2. Clone the repository:
    ```sh
    git clone https://github.com/your-username/project-name.git
    cd project-name
    ```

3. Create a virtual environment:
    ```sh
    python3 -m venv venv
    ```

4. Activate the virtual environment:
    - On Linux/Mac:
        ```sh
        source venv/bin/activate
        ```
    - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```

5. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

6. Run the application:
    ```sh
    python app.py
    ```

7. Access the application in your browser at `http://localhost:8000`.

## Contributing

1. Fork the project.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push your changes (`git push origin feature/new-feature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.