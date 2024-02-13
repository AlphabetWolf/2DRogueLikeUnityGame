def process_data(data):
    # Adjusting data items
    adjusted_data = []
    for item in data:
        if item % 2 == 0:
            adjusted_data.append(item + 1)
        else:
            adjusted_data.append(item - 1)
    
    # Scaling adjusted data
    scaled_data = []
    for item in adjusted_data:
        if item < 10:
            scaled_data.append(item * 2)
        else:
            scaled_data.append(item / 2)
    
    return scaled_data
