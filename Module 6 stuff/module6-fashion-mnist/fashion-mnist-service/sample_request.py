"""Send one image to the running service and print the prediction."""
import sys, requests

url = "http://localhost:8000/predict"
path = sys.argv[1] if len(sys.argv) > 1 else "sample.png"
with open(path, "rb") as f:
    response = requests.post(url, files={"file": f})
print(response.status_code, response.json())
