# main.py

from Growth_N_doubling_time_logic import reference_db, calc_growth_rate_and_doubling_time, within_typical_range

if __name__ == "__main__":
    print("Enter scientific name of bacterium (e.g., Escherichia coli):")
    bact_name = input().strip()
    while True:
        OD1 = float(input("Enter initial optical density (OD1): "))
        if OD1 <= 0:
            print("Error: OD1 must be positive and non-zero. Please re-enter.")
        else:
            break
    while True:
        OD2 = float(input("Enter optical density (OD2) at later time: "))
        if OD2 == OD1:
            print("Error: OD2 cannot be the same as OD1. Please enter a different value.")
        elif OD2 <= 0:
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
    try:
        k, td = calc_growth_rate_and_doubling_time(OD1, OD2, t1, t2)
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
