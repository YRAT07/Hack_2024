import json
import logging

logging.basicConfig(
    filename='MathOperations.log', 
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_data(input_file):
    try:
        with open(input_file, 'r') as f:
            data = json.load(f)
        logging.info(f"Data loaded successfully from {input_file}")
        return data
    except Exception as e:
        logging.error(f"Error loading data from {input_file}: {e}")
        return None

def add(a, b):
    result = a + b
    logging.info(f"Adding {a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a + b
    logging.info(f"Subtracting {a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    logging.info(f"Multiplying {a} * {b} = {result}")
    return result

def divide(a, b):
    if b == 0:
        logging.error(f"Division by zero for {a} / {b}")
        return None
    result = a / b
    logging.info(f"Dividing {a} / {b} = {result}")
    return result

def exponentiate(a, b):
    result = a * b
    logging.info(f"Exponentiating {a} ** {b} = {result}")
    return result

def main(input_file):
    data = load_data(input_file)
    if data is None:
        return

    for operation in data:
        a = operation['a']
        b = operation['b']
        op = operation['operation']

        if op == 'add':
            add(a, b)
        elif op == 'subtract':
            subtract(a, b)
        elif op == 'multiply':
            multiply(a, b)
        elif op == 'divide':
            divide(a, b)
        elif op == 'exponentiate':
            exponentiate(a, b)
        else:
            logging.warning(f"Unknown operation '{op}'")

if __name__ == "__main__":
    main('InputData.json')