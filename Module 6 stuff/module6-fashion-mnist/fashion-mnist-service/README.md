# Fashion MNIST Model Service (FastAPI + Docker)

This folder turns your trained Fashion MNIST classifier into a running web service
and packages that service so it behaves the same on any machine.

## Files
- `main.py`          The FastAPI application that serves predictions.
- `requirements.txt` The Python packages the service needs.
- `Dockerfile`       The recipe used to build the container image.
- `.dockerignore`    Files Docker should ignore when building.

## Step 1: Add your trained model
Train your CNN (see your assignment), then save it from Keras as:

    model.save("fashion_cnn.keras")

Copy that `fashion_cnn.keras` file into this folder, next to `main.py`.

## Step 2: Run the service locally
    pip install -r requirements.txt
    uvicorn main:app --reload

Open the interactive documentation at http://localhost:8000/docs
Use the `/predict` endpoint to upload an image and view the predicted label.

## Step 3: Build and run with Docker
    docker build -t fashion-mnist-service:v1 .
    docker run -d -p 8000:8000 --name fashion-api fashion-mnist-service:v1

The service is now available at http://localhost:8000

## Step 4: Test a prediction
    python sample_request.py path/to/an_image.png

You should receive a JSON response with the predicted class index, label, and confidence.
