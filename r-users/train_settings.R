library(gbm)
library(caret)

fit.control <- trainControl(
    method = "repeatedcv",
    number = 3,
    repeats = 2,
    classProbs = TRUE,
    summaryFunction = twoClassSummary
)

gbm.grid <-  expand.grid(
    interaction.depth = c(1, 3, 5, 9),
    n.trees = (1:10)*50,
    shrinkage = 0.1,
    n.minobsinnode = 5
)
