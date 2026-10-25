# Module 6 Assignment – Fashion MNIST Classification (CNN + FastAPI + Docker)

A six-layer Convolutional Neural Network (CNN) that classifies Fashion MNIST clothing
images, built as a class in both **Python** and **R** (Keras), served through a
**FastAPI** web service and packaged with **Docker**.

## Files
| File / folder | Description |
|---|---|
| `fashion_cnn.ipynb` | Python: `FashionCNN` class, training, evaluation, 2 predictions, saves the model and sample images |
| `fashion_cnn.R` | R: the same CNN as an R Reference Class (keras3), training and 2 predictions |
| `fashion-mnist-service/` | FastAPI service: `main.py`, `Dockerfile`, `requirements.txt`, the trained `fashion_cnn.keras` and sample images |
| `screenshots/` | Proof of local, Docker and R results |

## CNN architecture (6 layers)
| # | Layer | Purpose |
|---|---|---|
| 1 | Conv2D (32 filters, 3x3, ReLU) | detect simple features such as edges |
| 2 | MaxPooling2D (2x2) | reduce size, keep the strongest signals |
| 3 | Conv2D (64 filters, 3x3, ReLU) | detect more complex shapes |
| 4 | MaxPooling2D (2x2) | reduce size again |
| 5 | Flatten | convert the 2D feature maps into one vector |
| 6 | Dense (10, softmax) | probabilities for the 10 clothing classes |

Input: 28x28 greyscale images, scaled to 0–1. Optimizer: Adam. Loss: sparse categorical
cross-entropy. Trained for 5 epochs with 10% of the training data held back for validation.

## Results
| Version | Test accuracy | Sample predictions |
|---|---|---|
| Python | **89.64%** | Ankle boot ✔, Pullover ✔ |
| R | **88.64%** | Ankle boot ✔, Pullover ✔ |
| FastAPI (local) | – | `sample_0_Ankle boot.png` → Ankle boot (0.9978) |
| FastAPI in Docker | – | `sample_1_Pullover.png` → Pullover (0.9997) |

## Requirements
- Python 3.12 with: `pip install tensorflow matplotlib pillow fastapi "uvicorn[standard]" python-multipart requests`
- R 4.x with: `install.packages("keras3")` (uses Python's TensorFlow through reticulate)
- Docker (or GitHub Codespaces, which has Docker pre-installed)

## How to run
### 1. Python model
Open `fashion_cnn.ipynb` and click **Run All**. It trains the CNN, shows two predictions,
saves `fashion_cnn.keras` into `fashion-mnist-service/`, and saves two sample PNG images
for testing the API.

### 2. R model
In `fashion_cnn.R`, update the `RETICULATE_PYTHON` path at the top to your own Python 3.12
(it must have TensorFlow installed). Then in R:
```r
setwd("path/to/module6-fashion-mnist")
source("fashion_cnn.R", echo = TRUE)
```

### 3. FastAPI service (local)
```bash
cd fashion-mnist-service
python -m uvicorn main:app --reload
```
Open http://localhost:8000/docs → `POST /predict` → upload a sample PNG → **Execute**.

### 4. Docker
```bash
cd fashion-mnist-service
docker build -t fashion-mnist-service:v1 .
docker run -d -p 8000:8000 --name fashion-api fashion-mnist-service:v1
```
Open http://localhost:8000/docs (or the forwarded port 8000 in Codespaces) and test `/predict`,
or run: `python sample_request.py "sample_1_Pullover.png"`.

## Notes
- **Test images:** Fashion MNIST images show light clothing on a black background, so the
  sample PNGs are saved from the test set itself. Ordinary photos would need inverting first.
- **Docker environment:** Docker Desktop could not be installed on the work PC (WSL is not
  available), so the image was built and run in **GitHub Codespaces**, which provides Docker.
- **Versions:** the model was trained with TensorFlow 2.21, the same version used in the
  Docker image (`tensorflow-cpu==2.21.0`), so the saved model loads without compatibility issues.

## Screenshots
- `screenshots/local_prediction.png` – FastAPI prediction running locally
- `screenshots/docker_prediction.png` – prediction from the running Docker container
- `screenshots/r_output.png` – R model accuracy and predictions

**Author:** Ivan Rudasingwa