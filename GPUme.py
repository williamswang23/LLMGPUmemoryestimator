def calculate_vram(param_count_billion, precision):
    """
    Calculate VRAM requirements based on LLM parameter size and precision.
    
    Args:
        param_count_billion (float): Number of parameters in the LLM (in billions).
        precision (str): Precision type (FP32, FP16, FP8, INT8, FP4, INT4).
        
    Returns:
        float: Estimated VRAM requirement in GB.
    """
    # Mapping precision to bytes per parameter
    precision_map = {
        "FP32": 4,
        "FP16": 2,
        "FP8": 1,
        "INT8": 1,
        "FP4": 0.5,
        "INT4": 0.5
    }

    # Validate precision input
    if precision not in precision_map:
        raise ValueError(f"Invalid precision '{precision}'. Supported precisions are: {', '.join(precision_map.keys())}")
    
    # Convert parameter count from billions to actual count
    param_count = param_count_billion * 1e9
    bytes_per_param = precision_map[precision]

    # Calculate VRAM in GB
    total_vram_gb = (param_count * bytes_per_param) / (1024 ** 3)
    return total_vram_gb


def main():
    """
    Main function to interact with the user for VRAM calculation.
    """
    print("Supported precisions and their memory requirements per parameter:")
    print("1. FP32 (32-bit Floating Point): 4 bytes per parameter")
    print("2. FP16 (16-bit Floating Point): 2 bytes per parameter")
    print("3. FP8 (8-bit Floating Point): 1 byte per parameter")
    print("4. INT8 (8-bit Integer): 1 byte per parameter")
    print("5. FP4 (4-bit Floating Point): 0.5 byte per parameter")
    print("6. INT4 (4-bit Integer): 0.5 byte per parameter")

    try:
        # Get user inputs
        param_count_billion = float(input("Enter the number of parameters in the LLM (in billions): "))
        precision = input("Enter the precision (FP32, FP16, FP8, INT8, FP4, INT4): ").upper()

        # Calculate VRAM
        vram_required = calculate_vram(param_count_billion, precision)
        print(f"\nThe estimated VRAM requirement for an LLM with {param_count_billion:.1f} billion parameters at {precision} precision is: {vram_required:.2f} GB")
    
    except ValueError as e:
        print(f"Error: {e}")


# If this script is run as a standalone program, execute main()
if __name__ == "__main__":
    main()
