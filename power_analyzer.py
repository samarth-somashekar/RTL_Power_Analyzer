
from vcdvcd import VCDVCD

def compute_power(transitions, capacitance, voltage, frequency):
    return transitions * capacitance * (voltage ** 2) * frequency

def main(vcd_file, voltage, frequency, capacitance):
    vcd = VCDVCD(vcd_file, signals=None, store_tvs=True)
    print("Signal\tTransitions\tPower (uW)")
    print("-" * 40)
    total_power = 0

    for signal in vcd.signals:
        transitions = len(vcd[signal]['tv'])
        power = compute_power(transitions, capacitance, voltage, frequency)
        total_power += power
        print(f"{signal}\t{transitions}\t{power * 1e6:.2f}")

    print("-" * 40)
    print(f"Total Dynamic Power: {total_power * 1e6:.2f} µW")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 5:
        print("Usage: python power_analyzer.py <your_file.vcd> <voltage(V)> <frequency(Hz)> <capacitance(F)>")
    else:
        vcd_file = sys.argv[1]
        voltage = float(sys.argv[2])
        frequency = float(sys.argv[3])
        capacitance = float(sys.argv[4])
        main(vcd_file, voltage, frequency, capacitance)
