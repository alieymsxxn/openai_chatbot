# OpenAI Chatbot Development Setup

This README provides instructions for setting up a development server for the Flask-based OpenAI chatbot.

## Prerequisites
- Ensure you have Python and Poetry installed on your machine.

## Setup Instructions

1. **Initialize the Poetry project:**
   ```bash
   poetry init
   ```

2. **Install the required dependencies:**
   ```bash
   poetry install
   ```

3. **Alternatively, run the Flask development server:**
   Set the `FLASK_APP` environment variable and run:
   ```bash
   FLASK_APP=src/run.py poetry run flask run
   ```

The application should now be running on `http://localhost:5000`.
Make sure to check the logs for any errors during startup.



# API Endpoints

This document provides an overview of the endpoints available in the ChatGPT API for managing prompts and retrieving responses.

## 1. Add Prompt

- **Endpoint**: `POST /openai/prompts`
- **Description**: Adds a new prompt to the system.
- **Request Headers**:
  - `Content-Type`: `application/json`
- **Request Body**:
  - `prompt`: The prompt to be added (e.g., "What is the capital of Latvia?").
- **Response**: 
  ```json
  {
      "message": "Prompt added successfully.",
      "response": {
          "prompt": "What is the capital of Latvia?",
          "prompt_index": 5
      }
  }
  ```

---

## 2. Get Prompt Response

- **Endpoint**: `GET /openai/prompts/{id}/response`
- **Description**: Retrieves the response for a specific prompt by its ID.
- **Request Parameters**:
  - `id`: The ID of the prompt (e.g., `0`).
- **Response**: 
  ```json
  {
      "message": "Response successfully generated.",
      "response": {
          "prompt": "What is the capital of Australia?",
          "reponse": "The capital of Australia is Canberra."
      }
  }
  ```

---

## 3. Update Prompt

- **Endpoint**: `PUT /openai/prompts/{id}`
- **Description**: Updates an existing prompt.
- **Request Headers**:
  - `Content-Type`: `application/x-www-form-urlencoded`
- **Request Body**:
  - `prompt`: The new prompt to replace the existing one (e.g., "What is the capital of Australia?").
- **Request Parameters**:
  - `id`: The ID of the prompt to be updated (e.g., `0`).
- **Response**: 
  ```json
  {
      "message": "Update has been successfully.",
      "response": {
          "final": "What is the capital of Australia?",
          "inital": "What is the capital of Australia?"
      }
  }
  ```

---

## 4. Delete Prompt

- **Endpoint**: `DELETE /openai/prompts/{id}`
- **Description**: Deletes a specific prompt by its ID.
- **Request Parameters**:
  - `id`: The ID of the prompt to be deleted (e.g., `1`).
- **Response**: 
  ```json
  {
      "message": "Prompt has been deleted",
      "response": {
          "deleted_prompt": "What is the capital of Latvia?",
          "deleted_prompt_index": 1
      }
  }
  ```

---

## Notes

- All endpoints are hosted on `http://127.0.0.1:5000`.
- Ensure the server is running before making requests to these endpoints.