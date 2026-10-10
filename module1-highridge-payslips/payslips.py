#Highridge Construction Company - Weekly Payment Slips (python)
import random

random.seed(42) #This makes the random data the same everytime I run

total_workers = 400
workers = []

# am creating the workers
for i in range(1,total_workers+1):
    worker = {

        "id" : i,
        "name" : "Worker_" + str(i),
        "gender" : random.choice(["Male","Female"]),
        "salary" : random.randint(5000,35000)

    }
    workers.append(worker)

#adding one bad worker on purpose to test error handling

workers.append({"id" : total_workers+1,"name": "Worker_test","gender":"Male","salary":"N/A"})

#here we are deciding the employee level (Female rule first because ranges overlap)

def get_level(salary,gender):
    if salary > 7500 and salary < 3000 and gender == "Female":
        return"A5-F"
    elif salary > 10000 and salary < 20000:
        return "A1"
    else:
        return "Standard"

#we print the payslips for each worker

for worker in workers:
    try:
        if type(worker["salary"]) != int:
            raise ValueError("Salary is not a number")

        level = get_level(worker["salary"],worker["gender"])
        print("Payment slip | ID:", worker["id"], "| Name:", worker["name"],
              "| Gender :", worker["gender"], "| salary ($):", worker["salary"], "| Level:", level)
    except Exception as error:
        print ("Error processing worker", worker["id"],"-",error)
        
