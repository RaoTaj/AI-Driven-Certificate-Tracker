import pandas as pd
from sklearn.linear_model import LogisticRegression

def train_model():
    # Using the provided data directly
    data = {
        "DaysLeft": [10, 8, 5, 2, 15]
    }
    df = pd.DataFrame(data)

    if "DaysLeft" not in df.columns:
        print("❌ Missing DaysLeft column in logs")
        return

    # Drop rows where DaysLeft is NaN
    df = df.dropna(subset=["DaysLeft"])

    df["Risk"] = df["DaysLeft"].apply(lambda x: 1 if x < 7 else 0)

    print(df["Risk"].value_counts())  # Add this line to check class distribution

    X = df[["DaysLeft"]]
    y = df["Risk"]

    if len(y.unique()) < 2:
        print("❌ Data mein sirf ek hi class hai. Model train nahi ho sakta.")
        return

    model = LogisticRegression()
    model.fit(X, y)

    print("✅ Model trained: Certificates with <7 days left are marked as High Risk")

    return model


if __name__ == "__main__":
    model = train_model()
    if model:
        sample = [[5]]  # Predict risk for cert with 5 days left
        pred = model.predict(sample)
        print(f"Prediction for 5 days left: {'High Risk' if pred[0]==1 else 'Safe'}")
