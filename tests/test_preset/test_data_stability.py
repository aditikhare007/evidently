import pandas as pd

from evidently.test_suite import TestSuite
from evidently.test_preset import DataStability


def test_data_stability_preset():
    test_current_dataset = pd.DataFrame(
        {
            "category_feature": ["t", "e", "", ""],
            "numerical_feature": [0.4, -12, None, 234],
            "target": [1, 1, None, 1],
            "prediction": [0, 0, None, 0],
        }
    )
    test_reference_dataset = pd.DataFrame(
        {
            "category_feature": ["y", "n", "n", "y"],
            "numerical_feature": [0, 1, 2, 5],
            "target": [0, 0, 0, 1],
            "prediction": [0, 0, 0, 1],
        }
    )
    data_quality_suite = TestSuite(tests=[
        DataStability(),
    ])

    data_quality_suite.run(current_data=test_current_dataset, reference_data=test_reference_dataset)
    assert not data_quality_suite
    assert len(data_quality_suite.as_dict()["tests"]) == 10
