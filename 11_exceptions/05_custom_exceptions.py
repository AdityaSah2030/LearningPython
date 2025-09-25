def brew_chai(flavor):
    if flavor not in ["Masala", "Ginger", "Elaichi"]:
        raise ValueError("Unsupported Chai Flavor")
    print(f"Brewing {flavor} Chai...")

brew_chai("Mint")