# Authentication System

## Overview

This authentication system is designed to provide secure authentication services for accessing critical internal APIs. It offers features like user registration, login, logout, and token-based authentication using JSON Web Tokens (JWT). The system is built using the Falcon web framework for Python and utilizes a PostgreSQL database for storing user information.

## Features

- User Registration: Users can register by providing their email and password. Passwords are securely hashed using the SHA-256 algorithm before storage.
  
- User Login: Registered users can log in by providing their email and password. Upon successful login, the system issues a JWT token that can be used for subsequent authenticated requests.
  
- User Logout: Authenticated users can log out, which invalidates their JWT token and prevents further access to protected resources.
  
- Rate Limiting: The system implements rate limiting to prevent abuse and ensure fair usage of resources. It limits the number of login attempts per hour and per minute.

## Setup

### Prerequisites

- Python 3.x
- PostgreSQL
- Docker

### Installation

1. Clone the repository: `git clone <repository_url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Configure the database connection in `db/database.py`
4. Initialize the database schema: `python db/init_db.py`

### Usage

1. Start the Falcon application: `gunicorn -b 0.0.0.0:8000 app:app`
2. Access the API endpoints using a REST client or HTTP requests.

## API Endpoints

### User Registration

- **URL:** `/auth/register`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
      "email": "user@example.com",
      "password": "password123"
  }
  ```
- **Response:**
  - Status Code: `201 Created`
  - Body:
    ```json
    {
        "message": "Registration successful"
    }
    ```

### User Login

- **URL:** `/auth/login`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
      "email": "user@example.com",
      "password": "password123"
  }
  ```
- **Response:**
  - Status Code: `200 OK`
  - Body:
    ```json
    {
        "message": "Login successful",
        "token": "<JWT_token>"
    }
    ```

### User Logout

- **URL:** `/auth/logout`
- **Method:** `POST`
- **Request Header:**
  - `Authorization: Bearer <JWT_token>`
- **Response:**
  - Status Code: `200 OK`
  - Body:
    ```json
    {
        "message": "Logout successful"
    }
    ```

## Contributing

Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests to improve the authentication system.

## License

This project is licensed under the [MIT License](LICENSE).

---

This README provides an overview of the authentication system, including features, setup instructions, API endpoints, and guidelines for contributing. Users can follow the instructions to set up and use the system efficiently.