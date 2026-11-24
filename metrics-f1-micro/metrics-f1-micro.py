def f1_micro(y_true, y_pred):
    true_positives = sum(
        actual == predicted
        for actual, predicted in zip(y_true, y_pred)
    )
    errors = len(y_true) - true_positives
    denominator = 2 * true_positives + 2 * errors
    return round(2 * true_positives / denominator, 4)