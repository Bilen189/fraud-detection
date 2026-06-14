# Task 3: Model Explainability Using SHAP

## Objective

The objective of Task 3 was to interpret the best-performing fraud detection model using feature importance and SHAP explainability techniques. Based on Task 2 results, the Random Forest model was selected because it achieved stronger predictive performance than Logistic Regression while still allowing feature importance analysis.

## Selected Model

The Random Forest model trained on the e-commerce fraud dataset was selected for explainability. This model was chosen because it provided strong fraud detection performance and supports built-in feature importance, making it suitable for comparison with SHAP explanations.

## Built-in Feature Importance

The Random Forest model's built-in feature importance was used as a baseline explainability method. The top 10 features were visualized to understand which variables contributed most to the model's fraud predictions.

Built-in feature importance helps identify influential variables, but it does not show how individual feature values push a prediction toward fraud or legitimate classification. For this reason, SHAP was also used.

## SHAP Summary Plot Interpretation

The SHAP summary plot provides a global view of feature impact across many predictions. It shows both the importance of each feature and the direction in which feature values influence the model output.

The top drivers of fraud prediction were identified from the SHAP summary plot and compared with the Random Forest feature importance plot. Features related to transaction behavior, account age, device activity, transaction velocity, and geolocation were expected to play important roles because they capture suspicious behavioral patterns.

## Comparison Between SHAP and Built-in Feature Importance

Both SHAP and Random Forest feature importance help explain the model, but they provide different types of insight.

Random Forest feature importance shows which features were most useful for splitting decision trees. SHAP explains how each feature contributed to individual predictions and whether it pushed the prediction toward fraud or legitimate classification.

If both methods highlight similar features, this increases confidence that those variables are important fraud indicators. If they differ, SHAP is more useful for understanding the direction and business meaning of the feature's effect.

## Individual Prediction Explanations

### True Positive Case

The true positive case represents a fraudulent transaction that the model correctly classified as fraud. SHAP force plot analysis helps show which feature values pushed the prediction toward the fraud class. This is important because it helps explain what signals the model used to correctly detect fraud.

### False Positive Case

The false positive case represents a legitimate transaction incorrectly flagged as fraud. This is important from a business perspective because false positives may frustrate customers, delay purchases, increase support costs, and reduce trust in the platform.

SHAP analysis of this case helps identify which features may have made the transaction appear suspicious even though it was legitimate.

### False Negative Case

The false negative case represents a fraudulent transaction incorrectly classified as legitimate. This is the most financially risky type of error because fraud is missed. SHAP analysis helps identify which fraud signals were weak or missing in this case, helping guide future improvements to the model.

## Top Fraud Drivers

Based on the feature importance and SHAP analysis, the most important fraud prediction drivers include:

1. Transaction velocity
2. Time since signup
3. User transaction count
4. Device transaction count
5. Country or geolocation-related risk indicators

These features are important because they capture behavioral, temporal, and geographic fraud patterns.

## Business Recommendations

### Recommendation 1: Add extra verification for very new accounts

Transactions made shortly after signup should receive additional verification, especially when combined with high purchase activity. This recommendation is connected to the time_since_signup feature, which captures how quickly a user makes a purchase after account creation.

### Recommendation 2: Monitor high transaction velocity

Users or devices with unusually high transaction frequency within a short time should be flagged for review or stepped-up authentication. This recommendation is linked to transaction_velocity, user_transaction_count, and device_transaction_count.

### Recommendation 3: Use country-level risk monitoring

Country-level fraud patterns should be incorporated into fraud monitoring dashboards. Transactions from countries with elevated fraud patterns should not automatically be blocked, but they can be assigned additional risk weight when combined with suspicious behavior.

### Recommendation 4: Review false positives regularly

False positive cases should be monitored to reduce unnecessary customer friction. If legitimate users are repeatedly flagged because of specific features, the model threshold or business rules may need adjustment.

## Conclusion

SHAP explainability provided deeper insight into how the Random Forest model made fraud predictions. While built-in feature importance identified the most influential features overall, SHAP helped explain individual correct and incorrect predictions. These insights can help Adey Innovations improve fraud monitoring, reduce financial loss, and preserve customer trust.