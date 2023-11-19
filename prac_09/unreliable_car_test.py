"""
CP1404 Practical 09 - Unreliable Car test
Estimated Time: 10 minutes
Actual Time: 8 minutes
"""

from prac_09.unreliable_car import UnreliableCar


# For this test the system a bunch of times and get an estimate, also test basic functionality
def main():
    """Test for Unreliable Car class"""
    test_car = UnreliableCar("Rust Bucket", 100000, 50)
    # From here we would expect a success 50% of the time
    # Check Initial Attributes
    assert test_car.name == "Rust Bucket"
    assert test_car.fuel == 100000
    assert test_car.reliability == 50
    # Repeated Test
    successes = 0
    n = 200000
    for i in range(n):
        if test_car.drive(1) != 0:
            successes += 1
    final_prob = successes / n
    print(f"{final_prob:.4f}")
    # Overall it generally passes, with results like 0.5000 or 0.4998


if __name__ == "__main__":
    main()
