import nbformat

first = nbformat.read("churn_prediction_logistic_regression_3.11_done.ipynb", as_version=4)
second = nbformat.read("3.12Using_the_Model_Notes.ipynb", as_version=4)

first.cells.extend(second.cells)

nbformat.write(first, "churn_prediction_logistic_regression_3.12_done.ipynb")
