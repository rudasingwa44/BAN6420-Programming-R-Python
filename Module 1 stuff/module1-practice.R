tryCatch(
    {
        data <- read.csv("data.csv")
    }, error = function(e) {
        print("Error: File not found")
    },finally = {
        print("Execution complete")
    }
)