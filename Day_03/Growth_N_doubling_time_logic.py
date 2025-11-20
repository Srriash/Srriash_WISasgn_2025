# Growth_N_doubling_time_logic.py

import numpy as np

reference_db = {
    "Escherichia coli": {"doubling_time_min": [18, 20], "growth_rate_hr": [0.6, 0.8]},
    "Bacillus subtilis": {"doubling_time_min": [20, 24], "growth_rate_hr": [0.6, 0.72]},
    "Staphylococcus aureus": {"doubling_time_min": [24, 35], "growth_rate_hr": [0.5, 0.65]},
    "Pseudomonas aeruginosa": {"doubling_time_min": [50, 80], "growth_rate_hr": [0.3, 0.4]},
}

def calc_growth_rate_and_doubling_time(OD1, OD2, t1, t2):
    if OD2 == OD1 or OD2 <= 0 or OD1 <= 0 or t2 == t1:
        raise ValueError("Invalid OD or time values.")
    k = (np.log(OD2) - np.log(OD1)) / ((t2 - t1) / 60) # per hour
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
