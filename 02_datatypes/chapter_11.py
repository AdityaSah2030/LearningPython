import arrow
from collections import namedtuple

# ---------- Date & Time using Arrow ----------
# Get current UTC time
brewing_time = arrow.utcnow()
print(f"Current UTC brewing time: {brewing_time}")

# Convert brewing time to Europe/Rome timezone
brewing_time_rome = brewing_time.to("Europe/Rome")
print(f"Brewing time in Rome timezone: {brewing_time_rome}")

# ---------- Named Tuple for Chai Profile ----------
# Define a custom tuple type with fields 'flavor' and 'aroma'
chaiProfile = namedtuple("chaiProfile", ["flavor", "aroma"])

# Create an instance of chaiProfile
my_chai = chaiProfile(flavor="Masala", aroma="Spicy")

# Display chai profile details
print(f"Chai Flavor: {my_chai.flavor}")
print(f"Chai Aroma: {my_chai.aroma}")

# ---------- Combined Output ----------
print("\n--- Final Chai Brewing Profile ---")
print(f"Flavor : {my_chai.flavor}")
print(f"Aroma  : {my_chai.aroma}")
print(f"Brewed at (Rome time): {brewing_time_rome}")