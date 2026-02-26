# nottingham_runtime.py
import requests
import json

API_URL = "http://127.0.0.1:8000/compute"  # or wherever FastAPI runs

def send_to_api(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

def main_runtime_loop():
    # Example logic output
    result = {
        "state": "gradient",
        "logic_result": 42,
        "runtime_phase": "Nottingham"
    }

    api_response = send_to_api(result)
    print("API Response:", api_response)

if __name__ == "__main__":
    main_runtime_loop()