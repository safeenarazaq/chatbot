import streamlit as st

# Function to perform calculation
def calculate(num1, num2, operation):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid Operation"

# Title of the app
st.title('Simple Calculator')

# Input fields for the numbers
num1 = st.number_input('Enter first number', value=0)
num2 = st.number_input('Enter second number', value=0)

# Dropdown menu for selecting operation
operation = st.selectbox('Choose operation', ['Add', 'Subtract', 'Multiply', 'Divide'])

# Button to perform calculation
if st.button('Calculate'):
    result = calculate(num1, num2, operation)
    st.write(f'The result is: {result}')


