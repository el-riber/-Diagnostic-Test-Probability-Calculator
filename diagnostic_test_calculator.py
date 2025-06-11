def bayes_theorem(prevalence, sensitivity, specificity):
    # Convert percentages to decimals
    P_D = prevalence / 100
    P_not_D = 1 - P_D
    P_pos_given_D = sensitivity / 100
    P_neg_given_not_D = specificity / 100
    P_pos_given_not_D = 1 - P_neg_given_not_D

    # P(Disease | Test Positive)
    numerator_pos = P_pos_given_D * P_D
    denominator_pos = numerator_pos + (P_pos_given_not_D * P_not_D)
    P_D_given_pos = numerator_pos / denominator_pos if denominator_pos else 0

    # P(Disease | Test Negative)
    numerator_neg = (1 - P_pos_given_D) * P_D
    denominator_neg = numerator_neg + (P_neg_given_not_D * P_not_D)
    P_D_given_neg = numerator_neg / denominator_neg if denominator_neg else 0

    return P_D_given_pos * 100, P_D_given_neg * 100


def main():
    print("🩺 Diagnostic Test Probability Calculator (Bayes' Theorem)\n")

    try:
        prevalence = float(input("Enter disease prevalence (0–100%): "))
        sensitivity = float(input("Enter test sensitivity (0–100%): "))
        specificity = float(input("Enter test specificity (0–100%): "))

        if not (0 <= prevalence <= 100 and 0 <= sensitivity <= 100 and 0 <= specificity <= 100):
            raise ValueError("All values must be between 0 and 100.")

        positive_result, negative_result = bayes_theorem(prevalence, sensitivity, specificity)

        print(f"\n📈 Probability of disease given a POSITIVE test result: {positive_result:.2f}%")
        print(f"📉 Probability of disease given a NEGATIVE test result: {negative_result:.2f}%")

    except ValueError as e:
        print(f"❌ Input error: {e}")


if __name__ == "__main__":
    main()
