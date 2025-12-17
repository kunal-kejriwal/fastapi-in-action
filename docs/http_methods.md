# HTTP Methods in FastAPI

This document explains commonly used HTTP methods
and how they are implemented in FastAPI using
basic request bodies.

At this stage, request payloads are handled as
plain dictionaries to focus on HTTP semantics
rather than data validation.

---

## GET

    - Retrieves data from the server
    - Does not modify server state
    - Should be idempotent

    Example:
        ```http
        GET /items

POST

    - Creates a new resource

    - Data is sent in the request body

    - Not idempotent

    Example:

        POST /items

    Request body:

        {
        "name": "Laptop",
        "price": 1200
        }

PUT

    - Replaces an existing resource completely

    - Idempotent

    - Requires the full object representation

    Example:

        PUT /items/1

PATCH

    - Partially updates an existing resource

    - Used when updating only specific fields

    - Not guaranteed to be idempotent

    Example:

        PATCH /items/1

DELETE

    - Removes a resource

    - Idempotent

    Example:

        DELETE /items/1


Notes

    - At this stage, request bodies are treated as plain dictionaries.

    - This keeps examples simple and focused on HTTP behavior.

    - Pydantic models can be introduced later for validation and schema enforcement.