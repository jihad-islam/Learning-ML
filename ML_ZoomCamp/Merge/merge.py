import nbformat

first = nbformat.read("churn_prediction_logistic_regression_3.5.ipynb", as_version=4)
second = nbformat.read("churn_mutual_information_3_6.ipynb", as_version=4)

first.cells.extend(second.cells)

nbformat.write(first, "churn_prediction_logistic_regression_3.6_done.ipynb")
