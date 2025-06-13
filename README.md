
# RTL Power Analyzer

This tool estimates the dynamic power consumption of a Verilog design using VCD switching activity data.

## Features
- Parse VCD files and calculate dynamic power for each signal.
- Total dynamic power computation using user-specified parameters.

## Requirements

Install dependencies using:

```
pip install -r requirements.txt
```

## Usage

```
python power_analyzer.py <your_file.vcd> <voltage(V)> <frequency(Hz)> <capacitance(F)>
```

### Example

```
python power_analyzer.py sample.vcd 1.0 100000000 1e-14
```

## Sample VCD

A sample VCD file `sample.vcd` is included for testing.

## Author

Generated using ChatGPT 😉
