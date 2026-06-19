import re


def analyze_password(password):
    # Initialize scoring and feedback
    score = 0
    feedback = []

    # 1. Length Check
    length = len(password)
    if length < 8:
        feedback.append("❌ Too short: Passwords must be at least 8 characters.")
    elif length >= 12:
        score += 2
        feedback.append("✅ Great length: 12+ characters significantly increases brute-force resistance.")
    else:
        score += 1
        feedback.append("⚠️ Acceptable length, but 12+ characters would be much stronger.")

    # 2. Character Variety Checks
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("💡 Add lowercase letters to increase variety.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("💡 Add uppercase letters to increase variety.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("💡 Add numbers to increase complexity.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>_+\-\[\]~`=;\']", password):
        score += 1
    else:
        feedback.append("💡 Add special characters (e.g., !, @, #) to increase complexity.")

    # 3. Known Weak Patterns / Sequential Checks
    # Checking for common sequential runs (e.g., "12345", "abcdef", "qwerty")
    lowered_pw = password.lower()
    sequences = ["12345", "abcdef", "qwerty", "password", "p@ssword"]

    pattern_detected = False
    for seq in sequences:
        if seq in lowered_pw:
            pattern_detected = True
            feedback.append(f"❌ Weak pattern found: Avoid using common sequences like '{seq}'.")

    if pattern_detected:
        score = max(0, score - 2)  # Penalize the score for weak patterns

    # 4. Final Rating Evaluation
    if score >= 5:
        rating = "STRONG 💪"
    elif score >= 3:
        rating = "MEDIUM ⚠️"
    else:
        rating = "WEAK ❌"

    return {
        "score": f"{score}/6",
        "rating": rating,
        "suggestions": feedback
    }


# --- Demonstration ---
if __name__ == "__main__":
    print("--- Security Automation: Password Analyzer ---")
    test_password = input("Enter a password to test: ")

    results = analyze_password(test_password)

    print("\n--- Analysis Results ---")
    print(f"Strength Rating: {results['rating']}")
    print(f"Metrics Score:   {results['score']}")
    print("\nFeedback & Suggestions:")
    for suggestion in results["suggestions"]:
        print(f" - {suggestion}")