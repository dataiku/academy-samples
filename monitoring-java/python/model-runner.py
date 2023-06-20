from dataikuscoring import load_model
import pandas as pd

# Load the model from current export path
model = load_model('./model/model-initial-2023_03_24-15_25_49.zip')

input_df = pd.read_csv('./input/pokemon_for_scoring.csv')
predict_result = model.predict(input_df)
output_df = input_df
output_df['prediction'] = predict_result
print(" Output of model.predict(): {}".format(output_df))
output_df.to_csv('./output/pokemon_scored_python.csv', index=False)

