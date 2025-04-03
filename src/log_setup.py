import logging

def setup_logging():
    app_handler = logging.FileHandler("logs/app.log")
    app_handler.setLevel(logging.INFO)
    error_handler = logging.FileHandler("logs/error.log")
    error_handler.setLevel(logging.ERROR)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            app_handler,
            error_handler,
            logging.StreamHandler()
        ]
    )
