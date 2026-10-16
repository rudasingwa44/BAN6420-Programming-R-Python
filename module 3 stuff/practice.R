BankAccount <- setRefClass("BankAccount",
  fields = list(owner = "character", balance = "numeric"),
  methods = list(
    deposit = function(amount) {
      balance <<- balance + amount            # <<- updates the object's own field
    },
    show = function() {
      cat(owner, "has", balance, "\n")
    }
  )
)

acc <- BankAccount$new(owner = "Ivan", balance = 100)
acc$deposit(50)
acc$show()        # Ivan has 150