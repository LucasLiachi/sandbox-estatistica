# Hospital Queue Simulation Guide

This guide provides step-by-step instructions for running and understanding the hospital queue simulation system.

## Quick Start

1. **Install Required Dependencies**
```bash
pip install numpy matplotlib pandas
```

2. **Run the Simulation**
```bash
python simulacao.py --arrival-rate 2 --service-rate 3
```

## Configuration Parameters

- `arrival-rate`: Average number of patients arriving per hour (λ)
- `service-rate`: Average number of patients a doctor can serve per hour (μ)
- `time-unit`: Unit of time for rates ("hours" or "minutes", default: "hours")
- `output-dir`: Directory to save results (optional)

## Understanding the Models

### M/M/1 Model (Single Doctor)
- **Formulas Used**:
  - Utilization (ρ) = λ/μ
  - Average Queue Length (Lq) = ρ²/(1-ρ)
  - Average Wait Time (Wq) = Lq/λ
- **Stability Condition**: λ < μ

### M/M/2 Model (Two Doctors)
- **Formulas Used**:
  - Utilization (ρ) = λ/(2μ)
  - System Empty Probability (P0) = [1 + ρ + ρ²/2]^(-1)
  - Average Queue Length (Lq) = (ρ² * P0)/(2(1-ρ))
  - Average Wait Time (Wq) = Lq/λ
- **Stability Condition**: λ < 2μ

## Example Usage and Output

1. **Basic Simulation**
```bash
python simulacao.py --arrival-rate 2 --service-rate 3
```

Expected output:
```
Queue Analysis Results:
==================================================
               Metric  Single Doctor  Two Doctors
          Utilization       0.666667     0.333333
     Avg Queue Length       1.333333     0.176471
Avg Wait Time (hours)       0.666667     0.088235

Adding a second doctor reduces average wait time by 86.8%
```

2. **Custom Output Directory**
```bash
python simulacao.py --arrival-rate 2 --service-rate 3 --output-dir results/
```

## Interpreting Results

1. **Utilization (ρ)**
   - Shows percentage of time doctors are busy
   - Higher values indicate higher workload
   - Values close to 1 suggest system overload

2. **Average Queue Length (Lq)**
   - Number of patients waiting in line
   - Lower values indicate better service

3. **Average Wait Time (Wq)**
   - Time patients spend waiting before service
   - Key metric for patient satisfaction

## Practical Applications

1. **Resource Planning**
   - Determine optimal number of doctors
   - Plan staff schedules
   - Identify peak hour requirements

2. **Performance Analysis**
   - Monitor service quality
   - Identify bottlenecks
   - Compare different staffing scenarios

3. **Patient Experience**
   - Estimate wait times
   - Improve patient satisfaction
   - Optimize appointment scheduling

## System Requirements

- Python 3.6 or higher
- NumPy
- Matplotlib
- Pandas

## Limitations

1. **Model Assumptions**
   - Poisson arrival process
   - Exponential service times
   - First-in-first-out discipline
   - Independent arrivals and service times

2. **Real-world Factors Not Modeled**
   - Emergency cases
   - Different types of treatments
   - Staff breaks and shifts
   - Patient no-shows

## Best Practices

1. **Data Collection**
   - Monitor actual arrival rates
   - Track service times
   - Record peak hours and patterns

2. **Model Validation**
   - Compare with actual data
   - Adjust parameters periodically
   - Document assumptions

3. **System Optimization**
   - Use results for staff scheduling
   - Plan for peak periods
   - Consider cost-benefit analysis
