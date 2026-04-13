import pandas as pd
import numpy as np
data = {
    "Name": ["A", "B", "C", "D"],
    "Age": [25, np.nan, 30, np.nan],
    "Salary": [50000, 60000, np.nan, 55000]
}
df = pd.DataFrame(data)

print("Original Data:")
print(df)