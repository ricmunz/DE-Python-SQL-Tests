# Database Tables Overview

This database contains three tables: **Flights**, **Airlines**, and **Airports**. Each table serves a specific purpose in tracking and storing information related to flights, airlines, and airports.

---

## 1. **Flights Table**

The **Flights** table stores information about individual flights, including details like the flight date, origin and destination airports, flight delays, and more.

### Columns:
| Column Name              | Data Type     | Description                                                    |
|--------------------------|---------------|----------------------------------------------------------------|
| **YEAR**                 | smallint      | The year the flight is scheduled.                              |
| **MONTH**                | tinyint       | The month the flight is scheduled.                             |
| **DAY**                  | tinyint       | The day of the month the flight is scheduled.                  |
| **DAY_OF_WEEK**          | tinyint       | The day of the week the flight is scheduled.                   |
| **AIRLINE**              | nvarchar(2)   | The airline's IATA code.                                       |
| **FLIGHT_NUMBER**        | smallint      | The flight number.                                             |
| **TAIL_NUMBER**          | nvarchar(20)  | The aircraft's tail number (nullable).                         |
| **ORIGIN_AIRPORT**       | nvarchar(3)   | The IATA code of the origin airport.                           |
| **DESTINATION_AIRPORT**  | nvarchar(3)   | The IATA code of the destination airport.                      |
| **SCHEDULED_DEPARTURE**  | smallint      | The scheduled departure time (in minutes).                     |
| **DEPARTURE_TIME**       | smallint      | The actual departure time (nullable).                          |
| **DEPARTURE_DELAY**      | int           | The delay in departure (nullable).                             |
| **TAXI_OUT**             | smallint      | The taxi-out time (nullable).                                  |
| **WHEELS_OFF**           | smallint      | The time when the plane takes off (nullable).                  |
| **SCHEDULED_TIME**       | smallint      | The scheduled flight duration (in minutes).                    |
| **ELAPSED_TIME**         | smallint      | The actual flight duration (nullable).                         |
| **AIR_TIME**             | smallint      | The time spent in the air (nullable).                          |
| **DISTANCE**             | smallint      | The distance of the flight (in miles).                         |
| **WHEELS_ON**            | smallint      | The time when the plane lands (nullable).                      |
| **TAXI_IN**              | smallint      | The taxi-in time (nullable).                                   |
| **SCHEDULED_ARRIVAL**   | smallint      | The scheduled arrival time (in minutes).                       |
| **ARRIVAL_TIME**         | smallint      | The actual arrival time (nullable).                            |
| **ARRIVAL_DELAY**        | int           | The delay in arrival (nullable).                               |
| **DIVERTED**             | int           | Whether the flight was diverted (0 or 1).                      |
| **CANCELLED**            | bit           | Whether the flight was cancelled (0 or 1).                     |
| **CANCELLATION_REASON**  | nvarchar(255) | The reason for cancellation (nullable).                        |
| **AIR_SYSTEM_DELAY**     | int           | Delay caused by the air system (nullable).                     |
| **SECURITY_DELAY**       | int           | Delay caused by security (nullable).                           |
| **AIRLINE_DELAY**        | int           | Delay caused by the airline (nullable).                        |
| **LATE_AIRCRAFT_DELAY**  | int           | Delay caused by late aircraft arrival (nullable).              |
| **WEATHER_DELAY**        | int           | Delay caused by weather (nullable).                            |
| **FlightID**             | computed      | A unique identifier for each flight, based on columns YEAR, MONTH, DAY, AIRLINE, FLIGHT_NUMBER, ORIGIN_AIRPORT, and DESTINATION_AIRPORT   |

### Constraints:
- **PK_FlightID**: Primary key on **FlightID**.
- **FK_Flights_Airlines**: Foreign key referencing the **Airlines** table.
- **FK_Flights_OriginAirport**: Foreign key referencing the **Airports** table for the origin airport.
- **FK_Flights_DestinationAirport**: Foreign key referencing the **Airports** table for the destination airport.

### Description:
- **FlightID** is a computed column that combines various fields to create a unique identifier for the flight.

---

## 2. **Airlines Table**

The **Airlines** table stores information about airlines using IATA codes and their full names.

### Columns:
| Column Name   | Data Type     | Description                                          |
|----------------|---------------|------------------------------------------------------|
| **IATA_CODE**  | nvarchar(2)   | The airline's IATA code (primary key).               |
| **AIRLINE**    | nvarchar(50)  | The name of the airline.                             |

### Constraints:
- **PK_Airlines**: Primary key on **IATA_CODE**.

---

## 3. **Airports Table**

The **Airports** table stores details about airports, including their IATA code, location (city, state, country), and geographic coordinates.

### Columns:
| Column Name   | Data Type     | Description                                          |
|----------------|---------------|------------------------------------------------------|
| **IATA_CODE**  | nvarchar(3)   | The airport's IATA code (primary key).               |
| **AIRPORT**    | nvarchar(100) | The name of the airport.                             |
| **CITY**       | nvarchar(50)  | The city where the airport is located.               |
| **STATE**      | nvarchar(50)  | The state where the airport is located.              |
| **COUNTRY**    | nvarchar(50)  | The country where the airport is located.            |
| **LATITUDE**   | float         | The latitude of the airport (nullable).              |
| **LONGITUDE**  | float         | The longitude of the airport (nullable).             |

### Constraints:
- **PK_Airports**: Primary key on **IATA_CODE**.

---

## Relationships:
- The **Flights** table references the **Airlines** table through the **AIRLINE** column, ensuring that each flight is associated with an airline.
- The **Flights** table also references the **Airports** table twice:
  - **ORIGIN_AIRPORT** references the airport of origin.
  - **DESTINATION_AIRPORT** references the airport of destination.
