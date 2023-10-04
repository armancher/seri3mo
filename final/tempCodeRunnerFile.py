def read_customer_file(filename):
    # Read customer data from the customer file
    customers = {}
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split('|')
            customers[data[3]] = {
                'name': data[0],
                'family_name': data[1],
                'phone': data[2]
            }
    return customers

def read_storage_file(filename):
    # Read storage data from the storage file
    storage = []
    with open(filename, 'r') as file:
        # Skip the first line (column headers)
        next(file)
        for line in file:
            data = line.strip().split('|')
            storage.append({
                'goods_id': data[0],
                'input': int(data[1]),
                'output': int(data[2]),
                'price': float(data[3])
            })
    return storage

def read_goods_item_file(filename):
    # Read goods item data from the goods item file
    goods_items = {}
    with open(filename, 'r') as file:
        # Skip the first line (column headers)
        next(file)
        for line in file:
            data = line.strip().split('|')
            goods_items[data[0]] = {
                'name': data[1],
                'price': float(data[2])
            }
    return goods_items



def generate_bill(customer_id, discount_percentage):
    customers = read_customer_file('G:\\python mojtamafani\\final\\customer.txt')
    storage = read_storage_file('G:\\python mojtamafani\\final\\storage.txt')
    goods_items = read_goods_item_file('G:\\python mojtamafani\\final\\list_item.txt')

    # Find the customer by ID
    customer = customers.get(customer_id)

    if customer:
        # Convert percentage discount to decimal
        discount = float(discount_percentage) / 100.0

        # Print customer information
        print("                                           Factor")
        print(f"name: {customer['name']:40}family name: {customer['family_name']:40}phone: {customer['phone']}")

        # Print table headers
        print(f"{'Name':<10}{'Price':<20}{'Amount':<20}{'Discount':<20}{'Final Price':<20}")

        # Initialize total price
        total_price = 0

        # Generate bills for each item in the storage
        for s in storage:
            goods_id = s['goods_id']
            goods_item = goods_items.get(goods_id)
            if goods_item:
                input_amount = s['input']
                output_amount = s['output']
                amount = input_amount - output_amount
                price = goods_item['price']
                total_price_item = (price * amount) - (price * amount * discount)

                # Print the bill for each item
                print(f"{goods_item['name']:<10}${price:<20}{amount:<20}{discount * 100:.1f}%{'${:.2f}'.format(total_price_item):<20}")

                # Update total price
                total_price += total_price_item

        # Print total
        print(f"{'TOTAL:':<50}{'${:.2f}'.format(total_price):<20}")
    else:
        print(f"Customer with ID '{customer_id}' not found.")

# Example usage:
customer_id = input("Enter customer ID: ")
discount_percentage = input("Enter discount percentage (e.g., 15 for 15%): ")
generate_bill(customer_id, discount_percentage)
