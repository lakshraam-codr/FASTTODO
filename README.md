# FastAPI Todo App

A simple Todo application built with FastAPI, SQLAlchemy, and PostgreSQL.

## Features

- Create, read, update, and delete (CRUD) todos
- PostgreSQL database integration
- Pydantic models for data validation
- Automatic API documentation at `/docs`

## Setup

1. **Clone or navigate to the project directory.**

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up the database:**
   - Ensure PostgreSQL is running.
   - Update `.env` with your database URL if needed (default: `postgresql://postgres:Raam%4021@localhost:5432/TODO`).

6. **Run the application:**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8001
   ```

7. **Access the API:**
   - API docs: `http://localhost:8001/docs`
   - Interactive docs: `http://localhost:8001/redoc`

## API Endpoints

- **POST /todos**: Create a new todo
  - Body: `{"title": "string", "description": "string", "completed": false}`
  - Response: Created todo with ID

- **GET /todos**: Get all todos
  - Response: List of todos

- **GET /todos/{id}**: Get a single todo by ID
  - Response: Todo object or 404 if not found

- **PUT /todos/{id}**: Update a todo by ID
  - Body: `{"title": "string", "description": "string", "completed": boolean}`
  - Response: Updated todo or 404 if not found

- **DELETE /todos/{id}**: Delete a todo by ID
  - Response: `{"message": "Todo deleted"}` or 404 if not found

## Project Structure

- `main.py`: FastAPI app and endpoints
- `models.py`: SQLAlchemy models
- `schemas.py`: Pydantic schemas
- `database.py`: Database configuration
- `requirements.txt`: Dependencies
- `.env`: Environment variables

## Testing

Use Postman or curl to test the endpoints. Example:

```bash
# Create a todo
curl -X POST http://localhost:8001/todos -H "Content-Type: application/json" -d '{"title":"Test","description":"Desc","completed":false}'

# Get all todos
curl http://localhost:8001/todos
```