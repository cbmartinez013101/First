import yfinance as yf
import pandas as pd
import tkinter as tk

def moving_averages(ticker, short_window, long_window):
    df=yf.download(ticker, period="id", interval="id", group_by="ticker")
    df['Short_MA'] = df['Close'].rolling(window=short_window).mean()
    df['Long_MA'] = df['Close'].rolling(window=long_window).mean()
    return df

def crossovers(df):
    if df['Short_MA'].iloc[-2] < df['Long_MA'].iloc[-2]\
    and df['Short_MA'].iloc[-1] >= df['Long_MA'].iloc[-1]:
        return "Cross Above"
    elif df['Short_MA'].iloc[-2] > df['Long_MA'].iloc[-2]\
    and df['Short_MA'].iloc[-1] <= df['Long_MA'].iloc[-1]:
        return "Crossover Below"
    else:
        return "No Crossover"

def query_stock():
    ticker = entry.get()
    short_window = 5
    long_window = 20
    try:
        data = moving_averages(ticker, short_window, long_window)
        result = check_crossovers(data)
        results_label.config(text=f"{ticker}: {result}")
    except Exception as e:
        results_label.config(text=f"Error: {e}")
#Main application

pp=tk.TK()
pp.title("Moving average crossover alert")

#Creat widgets
label=tk.Label(app, text="Enter Ticker Symbol:")
label.pack(pady=10)
entry = tk.Entry(app)
entry.pack()
query_button - tk.Button(app, text='Query', command=query_stock)
query_button.pack()
result_label = tk.Label(app, text="")
result_label.pack(pady=10)

#Start the GUI application
app.mainloop()
