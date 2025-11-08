def oral_health_assessment():
    print("Welcome to the Oral Microbiome and Health Assessment Tool!")
    print("Please answer the following questions about your oral hygiene and habits.")

    # Oral hygiene practices
    brush_freq = int(input("How many times do you brush your teeth per day? (0-3): "))
    floss = input("Do you floss daily? (yes/no): ").strip().lower()
    mouthwash = input("Do you use mouthwash regularly? (yes/no): ").strip().lower()

    # Food practices
    sugar_intake = input("How often do you eat sugary foods/drinks? (never/rarely/sometimes/often): ").strip().lower()
    fiber_intake = input("How often do you eat high-fiber foods (vegetables/fruits/whole grains)? (never/rarely/sometimes/often): ").strip().lower()
    water_intake = input("How much water do you drink per day? (in liters, e.g., 1.5): ")

    # Medical and oral conditions
    dry_mouth = input("Do you experience dry mouth regularly? (yes/no): ").strip().lower()
    gum_bleed = input("Do your gums bleed when you brush/floss? (yes/no): ").strip().lower()
    cavities = int(input("How many cavities were you diagnosed with in the past year? (0 or more): "))
    bad_breath = input("Do you experience frequent bad breath? (yes/no): ").strip().lower()

    # Simple rule-based assessment
    score = 0
    if brush_freq >= 2:
        score += 1
    if floss == 'yes':
        score += 1
    if mouthwash == 'yes':
        score += 0.5
    if sugar_intake in ('never', 'rarely'):
        score += 1
    if fiber_intake in ('often', 'sometimes'):
        score += 1
    try:
        if float(water_intake) >= 1.5:
            score += 0.5
    except:
        pass
    if dry_mouth == 'yes':
        score -= 0.5
    if gum_bleed == 'yes':
        score -= 1
    if cavities > 0:
        score -= 1
    if bad_breath == 'yes':
        score -= 0.5

    # Output
    print("\nAssessment Result:")
    if score >= 3:
        print("Your oral hygiene practices and habits suggest a HEALTHY oral microbiome and good oral health.")
    elif score >= 1:
        print("Your oral health is AVERAGE, but there are areas that could benefit from improvement.")
    else:
        print("Your responses indicate a HIGHER RISK for oral microbiome imbalance and oral health problems.")
        print("Consider revisiting your oral hygiene and dietary practices, or speak with a dental professional.")
    print("(This self-assessment is for informational purposes only.)")

if __name__ == "__main__":
    oral_health_assessment()
