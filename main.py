import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import statsmodels.formula.api as smf

st.title("Forecasting of TMT Steel Rods")
uploaded_file = st.file_uploader("ar.csv", type="csv")

if uploaded_file is not None:
    # Read the CSV data into a DataFrame
    data = pd.read_csv(uploaded_file)

    train = data.iloc[:-6]
    test = data.iloc[-6:]

    model_hw = ExponentialSmoothing(train, trend="add", seasonal="add", seasonal_periods=12). \
        fit(smoothing_level=0.2, smoothing_trend=0.4, smoothing_seasonal=0.08)

    # future_data = pd.DataFrame(index=test.index)
    future_forecast_hw = model_hw.forecast(12)

    st.subheader("Select the number of months to forecast:")
    num_months = st.selectbox("Select month:", range(1, 13))

    # Plot the line chart with historical and forecasted data upon button click
    if st.button("Plot"):
        plt.figure(figsize=(10, 6))
        plt.plot(data.index, data['Quantity'], label='Historical data')
        plt.plot(future_forecast_hw.index, future_forecast_hw, label='Forecasted data')

        # Highlight the last 6 months of the forecasted data
        if num_months == 6:
            last_six_months = future_forecast_hw[-6:]
            plt.plot(last_six_months.index, last_six_months, 'r-', linewidth=2, label='Last 6 Months')

            # Display the values of the selected forecasted months
            forecasted_values = last_six_months.values
            for i, value in enumerate(forecasted_values):
                st.write(f"Month {i + 1}: {value}")

        plt.xlabel('Date')
        plt.ylabel('Quantity')
        plt.title('Historical and Forecasted Data')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Display the chart
        st.pyplot(plt)


















    # # # Display the forecasted values for the next 6 months
    # st.subheader("Select a month from the forecasted data:")
    # month_options = [(test.index[-1] + pd.DateOffset(months=i + 1)).strftime('%b %Y') for i in range(6)]
    #
    #
    #
    # selected_month = st.selectbox("Select month:", month_options)
    #
    # # Plot the line chart with historical and forecasted data upon button click
    # if st.button("Plot"):
    #     plt.figure(figsize=(10, 6))
    #     plt.plot(data.index, data['Quantity'], label='Historical data')
    #     plt.plot(future_data.index, future_forecast_hw, label='Forecasted data')
    #
    #     # # Highlight the selected month
    #     # if selected_month in month_options:
    #     #     selected_index = month_options.index(selected_month)
    #     #     plt.axvline(x=selected_month, color='r', linestyle='--',
    #     #                 label=f"Selected Month: {selected_month.strftime('%b %Y')}")
    #
    #     plt.xlabel('Date')
    #     plt.ylabel('Quantity')
    #     plt.title('Historical and Forecasted Data')
    #     plt.legend()
    #     plt.xticks(rotation=45)
    #     plt.tight_layout()
    #
    #     # Display the chart
    #     st.pyplot(plt)
















