import numpy as np

# Reference data for major bacteria (doubling_time range in minutes, growth_rate range per hour)
reference_db = {
    "Escherichia coli": {"doubling_time_min": [18, 20], "growth_rate_hr": [0.6, 0.8]},
    "Bacillus subtilis": {"doubling_time_min": [20, 24], "growth_rate_hr": [0.6, 0.72]},
    "Staphylococcus aureus": {"doubling_time_min": [24, 35], "growth_rate_hr": [0.5, 0.65]},
    "Pseudomonas aeruginosa": {"doubling_time_min": [50, 80], "growth_rate_hr": [0.3, 0.4]},
}

def calc_growth_rate_and_doubling_time(OD1, OD2, t1, t2):
    if OD2 == OD1 or OD2 <= 0 or OD1 <= 0 or t2 == t1:
        raise ValueError("Invalid OD or time values.")
    k = (np.log(OD2) - np.log(OD1)) / ((t2 - t1) / 60)  # per hour
    if k == 0:
        raise ValueError("Calculated growth rate is zero.")
    td = np.log(2) / k * 60
    return k, td

def within_typical_range(bact_name, k, td, rtol=1e-2):
    entry = reference_db.get(bact_name)
    if not entry:
        return None
    typical_td = entry["doubling_time_min"]
    typical_k = entry["growth_rate_hr"]
    td_typical = (
        np.isclose(td, typical_td[0], rtol=rtol) or
        np.isclose(td, typical_td[1], rtol=rtol) or
        typical_td[0] < td < typical_td[1]
    )
    k_typical = (
        np.isclose(k, typical_k[0], rtol=rtol) or
        np.isclose(k, typical_k[1], rtol=rtol) or
        typical_k[0] < k < typical_k[1]
    )
    return td_typical, k_typical, typical_td, typical_k

print("Enter scientific name of bacterium (e.g., Escherichia coli):")
bact_name = input().strip()

OD1 = float(input("Enter initial optical density (OD1): "))
while True:
    OD2 = float(input("Enter optical density (OD2) at later time: "))
    if OD2 == OD1:
        print("Error: OD2 cannot be the same as OD1. Please enter a different value.")
    elif OD2 <= 0 or OD1 <= 0:
        print("Error: Optical densities must be positive and non-zero. Please re-enter.")
    else:
        break

t1 = float(input("Enter time at OD1 (minutes): "))
while True:
    t2 = float(input("Enter time at OD2 (minutes): "))
    if t2 == t1:
        print("Error: t2 cannot be the same as t1. Please enter a different value.")
    else:
        break

# Calculation and output
try:
    k, td = calc_growth_rate_and_doubling_time(OD1, OD2, t1, t2)
    if k == 0:
        print("Error: Calculated growth rate is zero. Check your OD and time values.")
    else:
        print(f"\nCalculated growth rate: {k:.2f} per hour")
        print(f"Calculated doubling time: {td:.1f} minutes")
        if bact_name in reference_db:
            typical_td = reference_db[bact_name]["doubling_time_min"]
            typical_k = reference_db[bact_name]["growth_rate_hr"]
            td_typical, k_typical, _, _ = within_typical_range(bact_name, k, td)
            if td_typical:
                print(f"This is within the usual doubling time for {bact_name} ({typical_td[0]}-{typical_td[1]} min).")
            else:
                print(f"This doubling time is NOT typical for {bact_name} (normal: {typical_td[0]}-{typical_td[1]} min).")
            if k_typical:
                print(f"Growth rate is also typical for {bact_name} ({typical_k[0]}-{typical_k[1]} per hour).")
            else:
                print(f"Growth rate is NOT typical for {bact_name} ({typical_k[0]}-{typical_k[1]} per hour).")
        else:
            print("Sorry, your bacterium is not on my list.")
            print("You can look up its average doubling time and growth rate via Perplexity AI:")
            print(f"https://www.perplexity.ai/search?q=average+doubling+time+and+growth+rate+{bact_name.replace(' ', '+')}")
except Exception as e:
    print("An error occurred during the calculation:", str(e))

print("\nPurpose: This program calculates the growth rate and doubling time of a bacterial culture from optical density readings, compares these values to known literature data for the selected species, and provides a lookup link for other bacteria.")
