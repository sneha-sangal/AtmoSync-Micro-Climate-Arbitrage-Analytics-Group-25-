# AtmoSync – Data Analysis Module

## Objective

To analyse environmental, shipment, route, container and market price data to identify useful patterns, evaluate transportation costs and explore potential agricultural price arbitrage opportunities.

## Parameters Analysed

- Temperature
- Humidity
- Vibration
- Shipment details
- Route distance and transportation costs
- Container capacity and refrigeration status
- Market prices across different cities

## Tools and Technologies

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Excel

## Completed Analysis Activities

The following analysis activities have been completed using Python:

1. **Dataset Exploration:** Examined the available datasets, their structure, data types, missing values and duplicate records.
2. **Sensor Analysis:** Performed descriptive statistical analysis of temperature, humidity and vibration readings.
3. **Shipment Analysis:** Analysed product-wise shipments, quantities, transportation modes and shipment costs.
4. **Route Analysis:** Examined route distances, estimated travel hours and transportation cost scenarios.
5. **Market Price Analysis:** Compared product prices across cities and analysed price variations and trends.
6. **Container Analysis:** Studied container types, capacities and refrigeration status.
7. **Sensor-Container Integration:** Combined sensor summaries with container information for integrated analysis.
8. **Arbitrage Analysis:** Compared same-day product prices across cities and estimated potential gross margins after considering available transportation cost data.

## Key Analytical Findings

- Analysed 10,000 sensor readings and 500 shipment records.
- Identified 522 comparable date-product price combinations across cities.
- Found matching route and shipment cost information for 212 comparisons.
- Out of these 212 comparisons, 193 showed a positive estimated gross margin and 19 showed a negative estimated gross margin.
- The average estimated gross margin was approximately ₹11.61 per kg.

**Note:** These margins are preliminary estimates, not confirmed profits. They do not include all operational expenses, such as storage, handling, spoilage, taxes and market fees.

## Deliverables

- Jupyter notebooks containing the analysis.
- Statistical summaries and visualisations.
- CSV files containing analysis outputs.
- Final Data Analysis Findings Report.

## Current Status

Data exploration, individual dataset analysis, sensor-container integration and preliminary arbitrage analysis have been completed. The analysis outputs and findings report have been prepared for further use in project visualisation and dashboard development.

## Current Status
Initial module setup. Dataset integration and actual analysis will begin once the cleaned dataset is available.
