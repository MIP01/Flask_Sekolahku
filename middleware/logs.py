import logging
from flask import request, g
from time import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def start_timer():
    g.start = time()

def log_request_info():
    logger.info(f"Request: {request.method} {request.url} - Body: {request.get_data(as_text=True)}")

def log_response_info(response):
    if hasattr(g, 'start'):
        duration = time() - g.start
        logger.info(f"Response: {response.status_code} - Duration: {duration:.2f}s - Response: {response.get_data(as_text=True)}")
    return response

def log_error_info(exception=None):
    if exception:
        logger.error("An error occurred", exc_info=True)

def init_logging_middleware(app):
    app.before_request(start_timer)
    app.before_request(log_request_info)
    app.after_request(log_response_info)
    app.teardown_request(log_error_info)