#step 4 unzip "Employee Profile.zip" and displaying the data
tryCatch(
    {
        if(!file.exists("Employee Profile.zip"))
        {stop("Employee Profile.zip not found. Run the Python notebook first.")}

        unzip("Employee Profile.zip", exdir = "unzipped")
        employee_data <- read.csv("unzipped/Employee Profile/employee_profile.csv")
        print(t(employee_data))
    },
    error = function(e) {cat("Error:", conditionMessage(e), "\n")}
)