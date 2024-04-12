from datetime import datetime, timedelta


def read_file(file_name: str) -> list:
    """
    Reads data from a file and parses it into a list of tuples.

    Parameters:
        file_path (str): The path to the file containing the data.

    Returns:
        list: A list of tuples containing the parsed data.
    """

    data = []
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.strip().split(', ')
            data.append((parts[0], datetime.strptime(parts[1], '%Y.%m.%d'), int(parts[2])))

    return data


def calculate_price_change(product_name, data):
    """
    Calculates the price change for a specific product within the last month.

    Parameters:
        product_name (str): The name of the product.
        data (list): A list of tuples containing product data.

    Returns:
        int: The price change of the product within the last month.
             Returns None if there is not enough data available.
    """
    today = datetime.now()
    one_month_ago = today - timedelta(days=30)

    # Filter data for the specific product and within the last month
    prices = [price for name, date, price in data if name == product_name and date >= one_month_ago]

    # If there are less than two prices within the last month, return None
    if len(prices) < 2:
        return None

    # Sort the prices
    prices = sorted(prices)

    # Calculate the price change
    price_change = prices[-1] - prices[0]
    return price_change


product_name = 'good 1'
data = read_file("input_data.txt")
price_change = calculate_price_change(product_name, data)

# Print the result
if price_change is not None:
    print(f'Ціна на товар {product_name} змінилась на {price_change} гривень за останній місяць.')
else:
    print(f'Для товару {product_name} немає даних за останній місяць.')
