# Highridge Construction Company - Weekly Payment Slips (R)
set.seed(42)  # makes the random data the same every time we run

total_workers <- 400
workers <- list()

# 1. Create the workers
for (i in 1:total_workers) {
  workers[[i]] <- list(
    id = i,
    name = paste0("Worker_", i),
    gender = sample(c("Male", "Female"), 1),
    salary = sample(5000:35000, 1)
  )
}

# Add one bad worker on purpose to test the error handling
workers[[total_workers + 1]] <- list(id = total_workers + 1, name = "Worker_Test", gender = "Male", salary = "N/A")


# 2. Decide the employee level (Female rule first, because the ranges overlap)
get_level <- function(salary, gender) {
  if (salary > 7500 && salary < 30000 && gender == "Female") {
    return("A5-F")
  } else if (salary > 10000 && salary < 20000) {
    return("A1")
  } else {
    return("Standard")
  }
}


# 3. Print a payment slip for every worker
for (worker in workers) {
  tryCatch({
    if (!is.numeric(worker$salary)) {
      stop("salary is not a number")
    }

    level <- get_level(worker$salary, worker$gender)
    cat("Payment slip | ID:", worker$id, "| Name:", worker$name,
        "| Gender:", worker$gender, "| Salary ($):", worker$salary, "| Level:", level, "\n")
  }, error = function(e) {
    cat("Error processing worker", worker$id, "-", conditionMessage(e), "\n")
  })
}