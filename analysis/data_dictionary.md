# AtmoSync – Data Dictionary

This document describes the variables used in the five datasets of the AtmoSync project, including their data types, measurement units and roles in the data analysis process.

## 1. IoT Sensor Data

| Column Name | Data Type | Unit | Analytical Purpose |
|---|---|---|---|
| Sensor_ID | Identifier | — | Identifies individual sensors |
| Container_ID | Identifier | — | Links sensor readings with container information |
| Timestamp | DateTime | — | Supports time-based analysis of sensor readings |
| Temperature_C | Numerical | °C | Examines temperature distribution and variations |
| Humidity_Percent | Numerical | % | Examines humidity levels and variations |
| Vibration_Level | Numerical | Dataset-defined | Studies vibration patterns in sensor readings |
| Location | Categorical | — | Identifies the location associated with sensor readings |

## 2. Shipment Details

| Column Name | Data Type | Unit | Analytical Purpose |
|---|---|---|---|
| Shipment_ID | Identifier | — | Identifies individual shipments |
| Container_ID | Identifier | — | Connects shipments with container records |
| Product | Categorical | — | Enables product-wise shipment analysis |
| Quantity_KG | Numerical | kg | Measures the quantity transported |
| Origin_City | Categorical | — | Identifies shipment starting locations |
| Destination_City | Categorical | — | Identifies shipment destinations |
| Dispatch_Date | Date | — | Supports dispatch-date analysis |
| Expected_Arrival_Date | Date | — | Helps examine expected shipment duration |
| Transport_Mode | Categorical | — | Enables comparison of transportation modes |
| Transport_Cost | Numerical | Dataset currency | Supports transportation cost analysis |

## 3. Market Prices

| Column Name | Data Type | Unit | Analytical Purpose |
|---|---|---|---|
| Price_ID | Identifier | — | Identifies individual market price records |
| Date | Date | — | Supports date-wise price comparison |
| City | Categorical | — | Enables comparison of prices across cities |
| State | Categorical | — | Identifies the state associated with market records |
| Product | Categorical | — | Enables product-wise price analysis |
| Minimum_Price_Per_KG | Numerical | Dataset currency/kg | Represents the minimum recorded market price |
| Maximum_Price_Per_KG | Numerical | Dataset currency/kg | Represents the maximum recorded market price |
| Modal_Price_Per_KG | Numerical | Dataset currency/kg | Used for comparing market prices and identifying price gaps |

## 4. Route Details

| Column Name | Data Type | Unit | Analytical Purpose |
|---|---|---|---|
| Route_ID | Identifier | — | Identifies individual route records |
| Origin_City | Categorical | — | Identifies the starting city |
| Destination_City | Categorical | — | Identifies the destination city |
| Distance_KM | Numerical | km | Used to compare route distances |
| Estimated_Travel_Hours | Numerical | hours | Supports estimated travel-time analysis |
| Transport_Cost_Per_KM | Numerical | Dataset currency/km | Helps estimate transportation costs for routes |

## 5. Container Details

| Column Name | Data Type | Unit | Analytical Purpose |
|---|---|---|---|
| Container_ID | Identifier | — | Identifies individual containers |
| Container_Type | Categorical | — | Enables comparison of different container types |
| Capacity_KG | Numerical | kg | Supports container capacity analysis |
| Sensor_ID | Identifier | — | Links containers with their associated sensors |
| Refrigeration_Status | Categorical | — | Enables comparison of sensor readings across refrigeration statuses |

## Purpose of the Data Dictionary

This data dictionary provides a structured reference for understanding the variables used in the project. It supports consistent interpretation of the datasets and explains how individual variables contribute to the overall analysis.
