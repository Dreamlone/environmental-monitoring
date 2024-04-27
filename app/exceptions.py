from fastapi.responses import JSONResponse


def value_error_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"message": "Invalid argument", "detail": str(exc)},
    )
