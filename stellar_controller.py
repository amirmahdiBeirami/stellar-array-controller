# stellar_controller.py

class StellarArray:
    def __init__(self, name="Alpha-Quadrant Array"):
        self.name = name
        self.alignment_degrees = 0
        # self.power_output_gw = 100 # Initial power output in Gigawatts
        self.power_output_gw = 100 #bug fix


    def align(self, degrees: float) -> str:
        """Aligns the stellar array to the specified degrees."""
        self.alignment_degrees = degrees
        message = f"{self.name} aligned to {self.alignment_degrees} degrees. Current Power: {self.power_output_gw} GW."
        print(f"LOG: {message}")
        return message

    def adjust_power(self, adjustment_gw: float) -> str:
        """Adjusts the power output of the array."""
        self.power_output_gw += adjustment_gw
        message = f"Power output adjusted by {adjustment_gw} GW. Current output: {self.power_output_gw} GW."
        print(f"LOG: {message}")
        return message

    def get_status(self) -> str:
        """Returns the current status of the stellar array."""
        status = f"Status for {self.name}: Alignment at {self.alignment_degrees} degrees. Power: {self.power_output_gw} GW."
        print(f"LOG: {status}")
        return status

if __name__ == "__main__":
    controller = StellarArray()
    print("--- Stellar Array Controller Initializing ---")
    controller.align(15.5)
    controller.adjust_power(10)
    controller.get_status()
    print("--- Stellar Array Controller Operations Complete ---")
