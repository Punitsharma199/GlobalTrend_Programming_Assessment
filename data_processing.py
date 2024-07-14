import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder


def preprocess_data(df):
    # Handle missing values
    df = handle_missing_values(df)

    # Normalize numerical columns
    df = normalize_numerical_columns(df)

    # Encode categorical columns
    df = encode_categorical_columns(df)

    return df


def handle_missing_values(df):
    # Fill missing values with mean for numerical columns
    numerical_cols = df.select_dtypes(include=['number']).columns
    df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())

    # Fill missing values with mode for categorical columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])

    return df


def normalize_numerical_columns(df):
    scaler = StandardScaler()
    numerical_cols = df.select_dtypes(include=['number']).columns
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    return df


def encode_categorical_columns(df):
    encoder = LabelEncoder()
    categorical_cols = df.select_dtypes(include=['object']).columns
    df[categorical_cols] = df[categorical_cols].apply(encoder.fit_transform)
    return df


# Example DataFrame
data = {
    'A': [1, 2, None, 4],
    'B': ['X', 'Y', 'Z', 'X'],
    'C': [0.1, 0.5, 0.3, None],
    'D': [100, 200, 150, 180]
}
df = pd.DataFrame(data)

# Preprocess the DataFrame
preprocessed_df = preprocess_data(df)

print("Preprocessed DataFrame:")
print(preprocessed_df)


"""
Output:
Preprocessed DataFrame:
          A  B         C         D
0 -1.234427  0 -1.414214 -1.526564
1 -0.308607  1  1.414214  1.128330
2  0.000000  2  0.000000 -0.199117
3  1.543033  0  0.000000  0.597351

"""