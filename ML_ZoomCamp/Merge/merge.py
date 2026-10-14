import nbformat

first = nbformat.read("churn_prediction_logistic_regression_3.6_done.ipynb", as_version=4)
second = nbformat.read("churn_correlation_3_7.ipynb", as_version=4)

first.cells.extend(second.cells)

nbformat.write(first, "churn_prediction_logistic_regression_3.7_done.ipynb")
