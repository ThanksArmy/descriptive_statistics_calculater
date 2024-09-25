def descriptive_statistics():
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))
    step_size = int(input("Enter the step size: "))

    if step_size == 0 or (upper_bound - lower_bound) * step_size < 0:
        print("Invalid input. Please ensure the step size is non-zero and appropriate for the bounds.")
        return

    data = list(range(lower_bound, upper_bound + 1, step_size))
    if len(data) < 3:
        print("The group should include at least 3 values.")
        return

    mean = sum(data) / len(data)
    median = sorted(data)[len(data) // 2]
    range_value = max(data) - min(data)

    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Range: {range_value}")

# Example usage
descriptive_statistics()
