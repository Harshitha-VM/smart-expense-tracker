## 1. Which parts of the code were AI-generated vs. written by me

### AI-Assisted Components

I used ChatGPT to help generate:

* The initial FastAPI project structure.
* The Pydantic `Expense` model.
* JSON file storage functions for reading and writing expenses.
* Boilerplate code for the REST API endpoints.
* Initial pytest test templates.
* README and project documentation drafts.

### Implemented and Modified by Me

I:

* Created the project structure and files.
* Integrated all generated code into the project.
* Added sample expense data and tested different scenarios.
* Fixed import and module path issues encountered while running pytest.
* Verified endpoint behavior using FastAPI Swagger UI.
* Ensured the application met all assignment requirements.
* Updated and refined the generated code where necessary.

---

## 2. What I validated, tested, or changed in the AI output, and why

I reviewed and tested all AI-generated code before using it.

Changes and validations performed:

* Verified that expenses are correctly stored and retrieved from `expenses.json`.
* Tested all API endpoints through Swagger UI (`/docs`).
* Confirmed duplicate expense IDs return an appropriate error response.
* Verified category filtering works correctly regardless of letter case.
* Tested overall expense totals and category-wise totals using sample data.
* Tested expense deletion and confirmed that deleted records are removed from the JSON file.
* Fixed import path issues that caused pytest to fail when importing the `src` package.
* Updated the test configuration to ensure the test suite runs successfully from the project root directory.
* Executed the full test suite and verified that all tests pass.

---

## 3. Any AI suggestion I decided not to use, and why

### SQLite Database

AI suggested using SQLite for data persistence.

Reason:
The assignment explicitly stated that a database was not required and that local file storage was acceptable. I chose JSON file storage because it satisfied the requirements while keeping the implementation simple.

### Additional Features

AI suggested adding extra functionality such as search endpoints and monthly summaries.

Reason:
The assignment only required expense creation, retrieval, filtering, totals, and deletion. To keep the solution focused and within scope, I implemented the required functionality and used FastAPI's built-in Swagger/OpenAPI documentation as the optional bonus feature.
