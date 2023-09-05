true_positive = 2
false_positive = 2
true_negative = 985
false_negative = 11

amount_of_predictions = true_positive + false_positive + true_negative + false_negative
correct_predictions = true_positive + true_negative

model_accuracy = correct_predictions / amount_of_predictions

print(f"The accuracy of this model is{model_accuracy: .3f}.")
