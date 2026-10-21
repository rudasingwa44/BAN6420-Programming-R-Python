# R integration: ratings distribution with ggplot2
library(ggplot2)
df <- read.csv("Netflix_shows_movies_cleaned.csv")

rating_chart <- ggplot(df, aes(x = rating)) +
  geom_bar(fill = "steelblue") +
  labs(title = "TV-MA and TV-14 are the most common ratings",
       x = "Rating", y = "Number of titles") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

print(rating_chart)                                   # show it
ggsave("ratings_r.png", rating_chart, width = 8, height = 5)   # keep it