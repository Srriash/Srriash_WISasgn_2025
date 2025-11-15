import math
import unittest

# Reference data for major bacteria
reference_db = {
    "Escherichia coli": {"doubling_time_min": [18, 20], "growth_rate_hr": [0.6, 0.8]},
    "Bacillus subtilis": {"doubling_time_min": [20, 24], "growth_rate_hr": [0.6, 0.72]},
    "Staphylococcus aureus": {"doubling_time_min": [24, 35], "growth_rate_hr": [0.5, 0.65]},
    "Pseudomonas aeruginosa": {"doubling_time_min": [50, 80], "growth_rate_hr": [0.3, 0.4]},
}

def calc_growth_rate_and_doubling_time(OD1, OD2, t1, t2):
    if OD2 == OD1 or OD2 <= 0 or OD1 <= 0 or t2 == t1:
        raise ValueError("Invalid OD or time values.")
    k = (math.log(OD2) - math.log(OD1)) / ((t2 - t1) / 60)  # per hour
    if k == 0:
        raise ValueError("Calculated growth rate is zero.")
    td = math.log(2) / k * 60
    return k, td

def within_typical_range(bact_name, k, td, rtol=1e-2):
    entry = reference_db.get(bact_name)
    if not entry:
        return None
    typical_td = entry["doubling_time_min"]
    typical_k = entry["growth_rate_hr"]
    td_typical = (
        math.isclose(td, typical_td[0], rel_tol=rtol) or
        math.isclose(td, typical_td[1], rel_tol=rtol) or
        typical_td[0] < td < typical_td[1]
    )
    k_typical = (
        math.isclose(k, typical_k[0], rel_tol=rtol) or
        math.isclose(k, typical_k[1], rel_tol=rtol) or
        typical_k[0] < k < typical_k[1]
    )
    return td_typical, k_typical, typical_td, typical_k

class TestBacteriaGrowthCalculator(unittest.TestCase):
    def test_ecoli_typical_growth_rate(self):
        # Input values for k=0.6/hr (typical), td=69.3 min (not typical, but growth rate is typical)
        OD1 = 0.1
        OD2 = 0.1822118800390509  # Calculated to match k=0.6/hr
        t1 = 0
        t2 = 60
        k, td = calc_growth_rate_and_doubling_time(OD1, OD2, t1, t2)
        td_typical, k_typical, typical_td, typical_k = within_typical_range("Escherichia coli", k, td)
        print(f"Inputs: OD1={OD1}, OD2={OD2}, t1={t1}, t2={t2}")
        print(f"Growth rate calculated: {k:.3f}  Doubling time: {td:.2f}")
        print(f"Doubling time typical? {td_typical}   Growth rate typical? {k_typical} ({typical_td}, {typical_k})")
        self.assertTrue(k_typical)               # Growth rate in range
        self.assertFalse(td_typical)             # Doubling time NOT in reference range

    def test_ecoli_typical_doubling_time(self):
        # Input values for td=20 min (typical), k=2.079/hr (NOT typical)
        OD1 = 0.1
        OD2 = 0.2
        t1 = 0
        t2 = 20
        k, td = calc_growth_rate_and_doubling_time(OD1, OD2, t1, t2)
        td_typical, k_typical, typical_td, typical_k = within_typical_range("Escherichia coli", k, td)
        print(f"Inputs: OD1={OD1}, OD2={OD2}, t1={t1}, t2={t2}")
        print(f"Growth rate calculated: {k:.3f}  Doubling time: {td:.2f}")
        print(f"Doubling time typical? {td_typical}   Growth rate typical? {k_typical} ({typical_td}, {typical_k})")
        self.assertTrue(td_typical)              # Doubling time in range
        self.assertFalse(k_typical)              # Growth rate NOT in reference range

    def test_invalid_values(self):
        with self.assertRaises(ValueError):
            calc_growth_rate_and_doubling_time(0.1, 0.1, 0, 10)
        with self.assertRaises(ValueError):
            calc_growth_rate_and_doubling_time(0, 0.2, 0, 10)
        with self.assertRaises(ValueError):
            calc_growth_rate_and_doubling_time(0.2, 0, 0, 10)
        with self.assertRaises(ValueError):
            calc_growth_rate_and_doubling_time(0.1, 0.2, 10, 10)

    def test_not_in_reference(self):
        k, td = calc_growth_rate_and_doubling_time(0.1, 0.2, 0, 30)
        result = within_typical_range("Unknown bacterium", k, td)
        self.assertIsNone(result)

    def test_edge_growth_rate_zero(self):
        with self.assertRaises(ValueError):
            calc_growth_rate_and_doubling_time(0.1, math.exp(math.log(0.1)), 0, 60)

if __name__ == "__main__":
    unittest.main()
