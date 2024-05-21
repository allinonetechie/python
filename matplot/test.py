import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime
import random
import pandas as pd

# Initialize an empty DataFrame to store stock prices
df = pd.DataFrame(columns=['Time', 'Price'])

def get_real_time_stock_price():
    """
    Mock function to simulate getting real-time stock price.
    In a real-world scenario, replace this with an API call to fetch real-time data.
    """
    current_time = datetime.now().strftime('%H:%M:%S')
    price = random.uniform(100, 200)  # Mock price between $100 and $200
    return current_time, price

def update(frame):
    """
    Update the plot with new data.
    """
    global df
    current_time, price = get_real_time_stock_price()
    new_data = pd.DataFrame([[current_time, price]], columns=['Time', 'Price'])
    df = pd.concat([df, new_data], ignore_index=True)
    
    # Clear and update the plot
    ax.clear()
    ax.plot(df['Time'], df['Price'], color='blue')
    
    # Formatting
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Real-Time Stock Price')
    plt.xlabel('Time')
    plt.ylabel('Price ($)')
    plt.grid(True)

# Create a figure and axis
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, interval=1000)  # Update every 1000ms (1 second)

plt.show()
