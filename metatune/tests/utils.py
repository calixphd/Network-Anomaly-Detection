import optuna, sklearn
import numpy as np
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
from optuna.trial import Trial
from ..baseline.base import BaseTuner
from ..tune_classifier import classifier_tuner_model_class_map
from ..tune_regressor import regressor_tuner_model_class_map


# load sample datasets
# regression
REG_X, REG_y = datasets.load_diabetes(return_X_y=True)
REG_X = MinMaxScaler().fit_transform(REG_X)
REG_y = ((REG_y - REG_y.min()) / (REG_y.max() - REG_y.min())) + 1e-4
REG_DATA = sklearn.model_selection.train_test_split(REG_X, REG_y, random_state=0)

# classification
CLS_X, CLS_y = datasets.load_iris(return_X_y=True)
CLS_X = MinMaxScaler().fit_transform(CLS_X)
CLS_DATA = sklearn.model_selection.train_test_split(CLS_X, CLS_y, random_state=0)

#multi-task regression
MULTITASK_REG_X, MULTITASK_REG_y = np.random.randn(200, 20), np.random.randn(200, 5)
MULTITASK_REG_X = MinMaxScaler().fit_transform(MULTITASK_REG_X)
MULTITASK_REG_y = MinMaxScaler().fit_transform(MULTITASK_REG_y)
MULTITASK_DATA = sklearn.model_selection.train_test_split(MULTITASK_REG_X, MULTITASK_REG_y, random_state=0)


# Define an objective function to be minimized.
def objective_factory(model: BaseTuner, task: str="regression"):
    """ generate objective function for given model """
    # unpack data
    if task == "regression":
        data = REG_DATA
        metric = sklearn.metrics.mean_squared_error
    else:
        data = CLS_DATA
        metric = sklearn.metrics.accuracy_score

    if hasattr(model, "is_multitask"):
        data = MULTITASK_DATA
        metric = sklearn.metrics.mean_squared_error

    X_train, X_val, y_train, y_val = data
    def objective(trial: Trial):
        sampled_model = model.sample_model(trial)
        sampled_model.fit(X_train, y_train)
        y_pred = sampled_model.predict(X_val)
        error = metric(y_val, y_pred)
        return error
    return objective


class BaseTest:
    model: BaseTuner = None
    task: str = None
    n_trials: int = 20

    def test_dict_mapping(self):
        if self.task == "classification":
            assert self.model.__class__.__name__ in classifier_tuner_model_class_map.keys()
        
        elif self.task == "regression":
            assert self.model.__class__.__name__ in regressor_tuner_model_class_map.keys()

        else: assert False

    def test_methods_and_attrs(self):
        assert hasattr(self.model, "sample_params")
        assert hasattr(self.model, "sample_model")
        assert hasattr(self.model, "model") and self.model.model is None

    def test_study(self):
        try:
            study = optuna.create_study()  # Create a new study.
            study.optimize(objective_factory(self.model, task=self.task), n_trials=self.n_trials)
            best = study.best_params
        except:
            best = None
        assert best is not None




