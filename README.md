# Regression Analysis on Hypothetical Dataset

This project demonstrates regression analysis on a hypothetical dataset to analyze the relationship between study habits, attendance, and final grades. The dataset is generated randomly, and the analysis includes data visualization, model fitting, and result interpretation.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Dependencies](#dependencies)
- [License](#license)

## Overview

The project focuses on:

1. Generating a hypothetical dataset containing weekly study hours, attendance rates, and final grades.
2. Performing regression analysis to understand the impact of `Hours_Studied` and `Attendance_Rate` on `Final_Grade`.
3. Visualizing the relationships with scatter plots and fitted regression lines.

## Features

- **Hypothetical Dataset Generation**:
  - Randomly simulates weekly study hours (2-10), attendance rates (70-100%), and final grades.
- **Regression Analysis**:
  - Evaluates the influence of `Hours_Studied` and `Attendance_Rate` on `Final_Grade`.
  - Outputs regression model summaries for detailed insights.
- **Visualization**:
  - Scatter plots with regression lines for intuitive analysis.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Faizi805/regression.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```bash
   python regression.py
   ```
2. The script generates the dataset, performs regression analysis, and displays visualizations.

### Code Breakdown

#### Step 1: Dataset Generation

A dataset is created with the following features:
- **Week**: Sequential weeks (1-10).
- **Hours_Studied**: Random values between 2 and 10.
- **Attendance_Rate**: Random percentages between 70 and 100.
- **Final_Grade**: Simulated as a function of study hours, attendance rate, and randomness.

#### Step 2: Regression Analysis

- Uses `statsmodels` to fit linear regression models.
- Two models:
  1. `Final_Grade ~ Hours_Studied`
  2. `Final_Grade ~ Attendance_Rate`

#### Step 3: Visualization

- Scatter plots for each predictor against `Final_Grade`.
- Includes regression lines for better interpretation.

## Results

The analysis outputs:
1. **Regression Model Summaries**:
   - Key metrics like R-squared, coefficients, and p-values.
2. **Scatter Plots**:
   - `Hours_Studied` vs `Final_Grade` with a fitted line.
   - `Attendance_Rate` vs `Final_Grade` with a fitted line.

## Dependencies

- Python 3.x
- pandas
- numpy
- statsmodels
- matplotlib

Install dependencies using:
```bash
pip install pandas numpy statsmodels matplotlib
```

## License

This project is licensed under the [MIT License](LICENSE).

---

### Example Output

#### Dataset Snapshot:

| Week | Hours_Studied | Attendance_Rate | Final_Grade |
|------|---------------|-----------------|-------------|
| 1    | 7             | 95              | 47          |
| 2    | 4             | 80              | 34          |
| ...  | ...           | ...             | ...         |

#### Regression Summary (Hours Studied):

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:            Final_Grade   R-squared:                       0.85
... (rest of the output)
```

#### Visualization:

- Scatter plots and fitted lines are displayed in the output.

---

Contributions are welcome! Feel free to fork, create issues, or submit pull requests.

