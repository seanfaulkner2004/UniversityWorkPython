"""A program voltage calculating program. 
The user enters site names, then the current and resistance measured at each site,
then it prints the voltage of each site followed by the average.
"""

DIVIDER = "-" * 30


def main():
    """This function is too long, and will be shortened shortly!"""
    site_names = []
    prompt = "Enter measurement site name (or q to quit): "
    site = input(prompt)
    while site != "q":
        site_names.append(site)
        site = input(prompt)
    sites = []
    for site_name in site_names:
        prompt = f"Enter current followed by resistance for {site_name}: "
        current_str, resistance_str = input(prompt).split()
        voltage = float(current_str) * float(resistance_str)
        site = (site_name, voltage)
        sites.append(site)
    total = 0
    for site_name, voltage in sites:
        total += voltage
    average = total / len(sites)
    print(DIVIDER)
    print("Voltages")
    print(DIVIDER)
    for site_name, voltage in sites:
        print(f"{site_name}: {voltage:.2f} V")
    print(DIVIDER)
    print(f"Average: {average:.2f} V")


main()