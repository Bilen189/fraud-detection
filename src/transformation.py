import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from imblearn.over_sampling import SMOTE


def prepare_training_data(df, target_column, drop_columns=None):
    """
    Encode, split, impute, scale, and apply SMOTE to training data only.
    """
    if target_column not in df.columns:
        raise KeyError(f"Target column not found: {target_column}")

    if drop_columns is None:
        drop_columns = []

    existing_drop_columns = [col for col in drop_columns if col in df.columns]

    X = df.drop(columns=[target_column] + existing_drop_columns)
    y = df[target_column]

    X = pd.get_dummies(X, drop_first=True)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    imputer = SimpleImputer(strategy="median")
    X_train_imputed = imputer.fit_transform(X_train)
    X_test_imputed = imputer.transform(X_test)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train_imputed)
    X_test_scaled = scaler.transform(X_test_imputed)

    print("Before SMOTE:")
    print(y_train.value_counts())

    smote = SMOTE(random_state=42)
    X_train_resampled, y_train_resampled = smote.fit_resample(
        X_train_scaled,
        y_train
    )

    print("After SMOTE:")
    print(y_train_resampled.value_counts())

    return X_train_resampled, X_test_scaled, y_train_resampled, y_test