library(ggplot2)

ggplot (data = df , aes(x=height, y= weight)) +
    geom_point() +
    labs(title = "Height vs Weight", x = "Height (cm)", y = "Weight (kg)") +
    theme_minimal()


library(lattice)

xyplot(weight ~ height, data = df)
histogram(~age, data = df)
xyplot(weight ~ height | gender , data = df)
bwplot(score ~ group, data = df)
