def perform_operation(num1, num2, operation):
    op = operation.strip().lower() 
    if op in ("add", "+"):
        return num1 + num2
    elif op in ("subtract", "-"):
        return num1 - num2
    elif op in ("multiply", "*"):
        return num1 * num2
    elif op in ("divide", "/"):
        if num2 == 0:
            return "Error: Division by zero."
        return num1 / num2
    else:
        return "Error: Invalid operation."