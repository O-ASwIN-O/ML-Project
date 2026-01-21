import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Sample data
data = CustomData(
    gender="female",
    race_ethnicity="group B",
    parental_level_of_education="bachelor's degree",
    lunch="standard",
    test_preparation_course="none",
    reading_score=72,
    writing_score=74
)

pred_df = data.get_data_as_data_frame()
print("DataFrame:")
print(pred_df)

predict_pipeline = PredictPipeline()
results = predict_pipeline.predict(pred_df)
print("Prediction result:", results)