
from fastapi import FastAPI

import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = FastAPI()


@app.get("/")
def root():
    return {"status": "Server is alive!"}


@app.get("/process")
def process(number: int = 7):
    logging.debug(f"Request has been received. Starting the process with number {number}...")
    time.sleep(1)
    number += 1
    logging.debug(f"Inc number: {number}")
    time.sleep(1)
    number += 1
    logging.debug(f"Inc number: {number}")
    time.sleep(1)
    number += 1
    logging.debug(f"Inc number: {number}")
    time.sleep(1)
    number += 1
    logging.debug(f"Inc number: {number}")
    time.sleep(1)
    number += 1
    logging.debug(f"Inc number: {number}")
    logging.debug(f"Request has been completed.")
    return {"process_number": number}

