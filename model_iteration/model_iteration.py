import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, cross_validate
from sklearn.metrics import confusion_matrix
from warnings import filterwarnings

filterwarnings('ignore')

class ModelIteration:

    """
    Class to handle model iteration, cross-validation, hyperparameter tuning, and confusion matrix visualization.
    """

    def __init__(self):

        """
        Initialize the statistics DataFrame to store cross-validation results.
        """

        self.stats = pd.DataFrame()

    def run_cv(self, model_name, pipeline, X, y):

        """
        Run cross-validation for a given model and store the results.

        Args:
            model_name (str): Name of the model.
            pipeline (Pipeline): Sklearn pipeline containing preprocessing and model.
            X (DataFrame): Features for training.
            y (Series): Target variable.
        """
        
        cv = cross_validate(pipeline, X, y, cv=5, return_train_score=True, scoring=['recall', 'f1', 'roc_auc'])
        cv_mean = {k: np.mean(v) for k, v in cv.items()}
        cv_df = pd.DataFrame.from_dict(cv_mean, orient='index').T
        cv_df = cv_df.rename(columns={n: n.replace('_', ' ').title() for n in cv_df.columns}).T
        cv_results = cv_df.drop(['Fit Time', 'Score Time']).T
        cv_results['Model'] = model_name
        self.stats = pd.concat([self.stats, cv_results])
    
    def get_stats(self):

        """
        Display the cross-validation statistics for all the models run.
        """

        display(self.stats.set_index('Model'))
    
    @staticmethod
    def tune(estimator, param_grid, X, y, method='grid'):

        """
        Perform hyperparameter tuning using GridSearchCV or RandomizedSearchCV.

        Args:
            estimator (Estimator): Sklearn estimator object.
            param_grid (dict): Dictionary containing hyperparameter grid or distribution.
            X (DataFrame): Features for training.
            y (Series): Target variable.
            method (str): Tuning method, either 'grid' for GridSearchCV or 'random' for RandomizedSearchCV. Default is 'grid'.

        Returns:
            Estimator: Best estimator after search.
            dict: Best hyperparameters.
        """

        if method == 'grid':
            search = GridSearchCV(estimator=estimator, param_grid=param_grid, cv=5, scoring='recall')
        elif method == 'random':
            search = RandomizedSearchCV(estimator=estimator, param_distributions=param_grid, cv=5, n_iter=10, n_jobs=-1, scoring='recall')
        else:
            raise ValueError("Method must be either 'grid' or 'random'.")

        search.fit(X, y)
        return search.best_estimator_, search.best_params_
    
    @staticmethod
    def confusion(model, model_name, X, y):

        """
        Visualize the confusion matrix using a heatmap.

        Args:
            model (Estimator): Trained Sklearn model.
            model_name (str): Name of the model.
            X (DataFrame): Features to make predictions.
            y (Series): Actual target variable.
        """

        model.fit(X, y)
        y_pred = model.predict(X)
        conf_mat = confusion_matrix(y, y_pred)
        conf_mat = pd.DataFrame(conf_mat, columns=['0', '1'], index=['0', '1']).T
        conf_mat.index.name = model_name

        annot_labels = [
        ['TN: ' + str(conf_mat.iloc[0, 0]), 'FN: ' + str(conf_mat.iloc[0, 1])], 
        ['FP: ' + str(conf_mat.iloc[1, 0]), 'TP: ' + str(conf_mat.iloc[1, 1])]
        ]

        sns.heatmap(conf_mat, annot=annot_labels, fmt='', cmap='magma')
        plt.xlabel('Actual')
        plt.ylabel('Predicted')
        plt.title(f'Confusion Matrix, {conf_mat.index.name}')
        plt.show()