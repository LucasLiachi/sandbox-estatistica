# BCB Data Analysis with Linear Regression

A Python implementation for analyzing Brazilian Central Bank (BCB) time series data using statistical methods and linear regression.

## Project Structure

### Class: BCBAnalyzer

The main analysis class with the following key methods:

1. `fetch_and_save_data()`: 
   - Fetches data from BCB API
   - Stores in SQLite database

2. `load_data()`:
   - Loads data from database
   - Performs data preprocessing

3. `perform_analysis()`:
   - Calculates statistical measures
   - Performs linear regression
   - Returns analysis results

4. `plot_results()`:
   - Creates visualization plots
   - Shows time series and regression analysis

## Statistical Analysis

### Time Series Analysis
- Temporal data visualization
- Basic statistical measures:
  - Mean
  - Standard deviation
  - Trend analysis

### Linear Regression
- Model: y = βx + α
  - y: BCB values (dependent variable)
  - x: Time index (independent variable)
  - β: Slope coefficient
  - α: Intercept

## Usage Example

Introduction to Regression Models and Matrix Algebra

The lecture covers the fundamentals of **Applied Econometrics**, focusing on regression models and matrix algebra. The main points are as follows:

#### 1. **Regression Models**
- **Simple Linear Regression**:
  - Analyzes the relationship between a dependent variable ($$Y$$) and an independent variable ($$X$$).
  - Formula: $$Y_i = \beta_0 + \beta_1 X_i + e_i$$, where:
    - $$Y$$: dependent variable.
    - $$X$$: independent variable.
    - $$\beta_0, \beta_1$$: model coefficients.
    - $$e_i$$: random error.
    
- **Multiple Linear Regression**:
  - Relates $$Y$$ to two or more independent variables ($$X_1, X_2, ...$$).
  - Formula: $$Y_i = \beta_0 + \beta_1 X_{1i} + \beta_2 X_{2i} + e_i$$.
  - Benefits:
    - Better precision by including multiple explanatory variables.
    - Allows assessment of the individual impact of each independent variable.

- **Assumptions for Model Validity**:
  1. Linear relationship between $$X$$ and $$Y$$.
  2. Independent residuals.
  3. Homoscedasticity (constant variance of residuals).
  4. Normality of residuals.

#### 2. **Matrix Algebra**
- Matrices are used to organize data and solve linear systems.
- **Matrix Operations**:
  - **Addition/Subtraction**: Add/subtract corresponding elements of matrices of the same order.
  - **Multiplication**: Multiply rows of one matrix by columns of another.
  - **Transpose**: Swap rows for columns in a matrix.
  
- **Determinant**:
  - Applies only to square matrices.
  - Indicates whether a linear system has a unique solution.
  
- **Inverse Matrix**:
  - Used to solve linear systems.
  - Exists only for non-singular square matrices (determinant not equal to zero).

---

### Step-by-Step Application

#### Step 1: Identify the Problem
- Define the dependent ($$Y$$) and independent ($$X$$) variables.
- Example: Predict education level ($$Y$$) based on socioeconomic status ($$X_1$$) and race ($$X_2$$).

#### Step 2: Data Collection
- Obtain relevant data for the defined variables.

#### Step 3: Choose the Model
- Use simple regression if there's only one independent variable, or multiple regression for two or more variables.

#### Step 4: Build the Model
- Organize the data in matrix format.
- Use statistical software or manual calculations to estimate the coefficients ($$\beta_0, \beta_1, ...$$).

#### Step 5: Verify Assumptions
- Test the assumptions of linearity, independence of residuals, homoscedasticity, and normality.

#### Step 6: Interpret Results
- Analyze the coefficients to understand the impact of independent variables on the dependent variable.

#### Step 7: Apply Matrix Algebra (if necessary)
- Solve linear systems or manipulate data using matrix operations (addition, subtraction, multiplication).

#### Step 8: Validate the Model
- Evaluate the model's accuracy using metrics such as $$R^2$$ or statistical tests.