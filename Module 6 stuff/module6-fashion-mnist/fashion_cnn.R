# Module 6: Fashion MNIST CNN in R (keras3, using Python 3.12's TensorFlow underneath)

# Tell R which Python to use BEFORE loading keras (path is specific to this PC)
Sys.setenv(RETICULATE_PYTHON = "C:/Users/CCIR0634/AppData/Local/Python/pythoncore-3.12-64/python.exe")
library(keras3)

CLASS_NAMES <- c("T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
                 "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot")

# 1. Load and prepare the data (scale to 0-1, add the channel dimension)
fashion <- dataset_fashion_mnist()
x_train <- array_reshape(fashion$train$x / 255, c(60000, 28, 28, 1))
x_test  <- array_reshape(fashion$test$x / 255, c(10000, 28, 28, 1))
y_train <- fashion$train$y
y_test  <- fashion$test$y

# 2. The CNN class (Reference Class = R's Python-style class)
FashionCNN <- setRefClass("FashionCNN",
  fields = list(model = "ANY"),
  methods = list(
    initialize = function(...) {
      # Six layers: Conv2D, MaxPooling2D, Conv2D, MaxPooling2D, Flatten, Dense
      model <<- keras_model_sequential(input_shape = c(28, 28, 1)) |>
        layer_conv_2d(filters = 32, kernel_size = c(3, 3), activation = "relu") |>
        layer_max_pooling_2d(pool_size = c(2, 2)) |>
        layer_conv_2d(filters = 64, kernel_size = c(3, 3), activation = "relu") |>
        layer_max_pooling_2d(pool_size = c(2, 2)) |>
        layer_flatten() |>
        layer_dense(units = 10, activation = "softmax")
      model |> compile(optimizer = "adam",
                       loss = "sparse_categorical_crossentropy",
                       metrics = "accuracy")
      callSuper(...)
    },
    train = function(x, y, epochs = 5) {
      model |> fit(x, y, epochs = epochs, batch_size = 64, validation_split = 0.1)
    },
    evaluate_model = function(x, y) {
      model |> evaluate(x, y, verbose = 0)
    },
    predict_classes = function(images) {
      probabilities <- model |> predict(images, verbose = 0)
      max.col(probabilities) - 1   # R counts from 1, the labels count from 0
    }
  )
)

# 3. Create, train and evaluate
cnn <- FashionCNN$new()
summary(cnn$model)
cnn$train(x_train, y_train, epochs = 5)
scores <- cnn$evaluate_model(x_test, y_test)
cat(sprintf("\nTest accuracy: %.2f%%\n", scores[["accuracy"]] * 100))

# 4. Predict two test images
predicted <- cnn$predict_classes(x_test[1:2, , , , drop = FALSE])
for (i in 1:2) {
  cat(sprintf("Image %d - Predicted: %s | Actual: %s\n",
              i, CLASS_NAMES[predicted[i] + 1], CLASS_NAMES[y_test[i] + 1]))
}