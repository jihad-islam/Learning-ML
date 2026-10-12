import nbformat

first = nbformat.read("churn_data_preparation_3_2.ipynb", as_version=4)
second = nbformat.read("churn_feature_importance_3_5.ipynb", as_version=4)

first.cells.extend(second.cells)

nbformat.write(first, "churn_prediction_logistic_regression_3.5.ipynb")
