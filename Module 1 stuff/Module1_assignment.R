total_workers <- 400

workers <- data.frame(
    id = 1:total_workers,
    name = paste0("Worker_", 1:total_workers),
    salary = sample(5000:35000,total_workers, replace = TRUE),
    gender = sample(c("Male", "Female"), total_workers, replace = TRUE)
)

print(head(workers))

for (i in 1:nrow(workers)) {
    tryCatch(
        {
            salary <- workers$salary[i]
            gender <- workers$gender[i]
            name <- workers$name[i]

            level <- "Standard"

            if (salary > 10000 & salary < 20000) {
                level <- "A1"
            } else if (salary > 7500 & salary < 30000 & gender == "Female") {
                level <- "A5-F"
            }
            
            cat(sprintf("Payment slip for %s : Level %s, Gender : %s, Salary : $%d\n", name, level, gender, salary))
            
        }, error = function(e) {
            cat(sprintf("Error processing worker %s: %s\n", workers$id[i], e$message))
        }
    )
}
