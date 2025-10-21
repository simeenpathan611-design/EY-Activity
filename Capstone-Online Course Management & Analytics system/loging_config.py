import logging

logging.basicConfig(
    filename='etl_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_new_enrollment(enrollment_id):
    logging.info(f"New enrollment added: {enrollment_id}")

def log_error(msg):
    logging.error(msg)

def log_etl_status(status):
    logging.info(f"ETL process {status}")