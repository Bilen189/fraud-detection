# Task 2: Model Building and Training

## Objective
The objective of Task 2 was to build, train, evaluate, and compare fraud detection models for both the e-commerce fraud dataset and the credit card fraud dataset.

## Models Trained
Two models were trained for each dataset:

1. Logistic Regression
   - Used as an interpretable baseline model.
   - Helps establish a simple benchmark.

2. Random Forest
   - Used as an ensemble model.
   - Captures non-linear relationships between features and fraud outcomes.

## Evaluation Metrics
Because both datasets are imbalanced, accuracy was not used as the main evaluation metric. Instead, the following metrics were used:

- AUC-PR
- F1-Score
- Confusion Matrix

AUC-PR is important because it focuses on performance for the minority fraud class. F1-Score balances precision and recall, which is useful when both false positives and false negatives have business costs.

## Resampling Strategy
SMOTE was applied only to the training set. The test set was not resampled so that model evaluation remained realistic and free from data leakage.

## Model Comparison
The models were compared using AUC-PR and F1-Score. The best model was selected based on fraud detection performance, stability, and interpretability.

## Model Selection
The best-performing model should be selected based primarily on AUC-PR and F1-Score rather than accuracy. If Random Forest outperforms Logistic Regression, it should be selected as the stronger predictive model. However, Logistic Regression remains useful as an interpretable baseline.

## Business Justification
In fraud detection, false negatives can lead to direct financial losses because fraudulent transactions are missed. False positives can harm customer trust because legitimate users may be blocked. Therefore, the selected model should balance fraud detection power with customer experience.