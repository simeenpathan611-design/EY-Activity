from fastapi import Request
from fastapi.responses import JSONResponse
import logging

logging.basicConfig(filename="backend.log", level=logging.INFO, format="%(asctime)s - %(message)s")


async def log_requests(request: Request, call_next):
    logging.info(f"Request: {request.method} {request.url}")
    try:
        response = await call_next(request)
        logging.info(f"Response status: {response.status_code}")
        return response
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return JSONResponse(status_code=500, content={"message": "Internal server error"})