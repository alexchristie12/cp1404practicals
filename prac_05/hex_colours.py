"""CP1404 Practical 05: hex_colours.py"""
NAME_TO_CODE = {"ABSOLUTE ZERO": "#0048ba", "BITTERSWEET": "#fe6f5e", "CAMEO PINK": "#efbbcc", "GO GREEN": "#00ab66",
                "LILAC": "#c8a2c8", "MAGENTA": "#ff00ff", "OXBLOOD": "#4a0000", "SANDYBROWN": "#f4a460",
                "SEAGREEN!": "#54ff9f", "UNITED NATIONS BLUE": "#5b92e5"}  # Insert Colours and codes
colour_name = input("Enter a colour name: ").upper()
while colour_name != "":
    try:
        print(f"{colour_name} corresponds to the colour code: {NAME_TO_CODE[colour_name]}")
    except KeyError:
        print(f"Invalid Input!")
    colour_name = input("Enter a colour name: ").upper()

