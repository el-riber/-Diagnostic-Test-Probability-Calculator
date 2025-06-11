
# 🧪 Diagnostic Test Probability Calculator

This Python program calculates the probability of having a disease based on diagnostic test results using **Bayes' Theorem**. It is designed to help medical professionals assess the reliability of positive or negative results given the test's sensitivity, specificity, and the disease prevalence.

---

## 📌 What It Calculates

Given:
- **Prevalence** – Probability that a person has the disease (P(Disease))
- **Sensitivity** – Probability that the test is positive if the person has the disease (P(Test+ | Disease))
- **Specificity** – Probability that the test is negative if the person doesn’t have the disease (P(Test- | No Disease))

The program computes:
- **P(Disease | Test Positive)**
- **P(Disease | Test Negative)**

---

## 🧪 Example

```

Enter disease prevalence (0–100%): 5
Enter test sensitivity (0–100%): 95
Enter test specificity (0–100%): 98

📈 Probability of disease given a POSITIVE test result: 71.43%
📉 Probability of disease given a NEGATIVE test result: 0.26%

````

---

## 🚀 How to Run

### Requirements
- Python 3.7 or higher (no external libraries required)

### Run the script:

```bash
python diagnostic_test_calculator.py
````

---

## ✅ Test Cases

### Normal:

1. Prevalence = 5%, Sensitivity = 95%, Specificity = 98%
2. Prevalence = 20%, Sensitivity = 90%, Specificity = 85%
3. Prevalence = 1%, Sensitivity = 99%, Specificity = 99%

### Edge:

1. Prevalence = 0% → Output should be 0% for all results
2. Prevalence = 100% → Output should be 100% for positive, 0% for negative
3. Sensitivity or Specificity = 0% → Return extreme probabilities


---

## 📄 License

This project is part of the Application Development BAS program.



