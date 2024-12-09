# SQL Code Challenge

### Responses from Word instructions file are in **sql_code_challende.sql** alongside code.

<br>
<br>


# Database Tables Overview

This database contains three tables: **Flights**, **Airlines**, and **Airports**. Each table serves a specific purpose in tracking and storing information related to flights, airlines, and airports.

---

## 1. **Flights Table**

The **Flights** table stores information about individual flights, including details like the flight date, origin and destination airports, flight delays, and more.

### Columns:
| Column Name              | Data Type     | Description                                                    |
|--------------------------|---------------|----------------------------------------------------------------|
| **YEAR**                 | smallint      | The year the flight is scheduled.  (1903-32767)                |
| **MONTH**                | tinyint       | The month the flight is scheduled. (1-12)                      |
| **DAY**                  | tinyint       | The day of the month the flight is scheduled. (1-31)           |
| **DAY_OF_WEEK**          | tinyint       | The day of the week the flight is scheduled. (1-7)             |
| **AIRLINE**              | nvarchar(2)   | The airline's IATA code.                                       |
| **FLIGHT_NUMBER**        | smallint      | The flight number.                                             |
| **TAIL_NUMBER**          | nvarchar(20)  | The aircraft's tail number (nullable).                         |
| **ORIGIN_AIRPORT**       | nvarchar(3)   | The IATA code of the origin airport.                           |
| **DESTINATION_AIRPORT**  | nvarchar(3)   | The IATA code of the destination airport.                      |
| **SCHEDULED_DEPARTURE**  | smallint      | The scheduled departure time (in minutes).                     |
| **DEPARTURE_TIME**       | smallint      | The actual departure time (nullable). [0000-2359]              |
| **DEPARTURE_DELAY**      | int           | The delay in departure (nullable). [+/-]                       |
| **TAXI_OUT**             | smallint      | The taxi-out time (nullable).                                  |
| **WHEELS_OFF**           | smallint      | The time when the plane takes off (nullable).                  |
| **SCHEDULED_TIME**       | smallint      | The scheduled flight duration (in minutes).                    |
| **ELAPSED_TIME**         | smallint      | The actual flight duration (nullable).                         |
| **AIR_TIME**             | smallint      | The time spent in the air (nullable).                          |
| **DISTANCE**             | smallint      | The distance of the flight (in miles).                         |
| **WHEELS_ON**            | smallint      | The time when the plane lands (nullable).                      |
| **TAXI_IN**              | smallint      | The taxi-in time (nullable).                                   |
| **SCHEDULED_ARRIVAL**   | smallint      | The scheduled arrival time (in minutes).                        |
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

### Sample Data:
<div style="overflow-x:auto;">
  <table>
    <thead>
      <tr>
        <th>YEAR</th>
        <th>MONTH</th>
        <th>DAY</th>
        <th>DAY_OF_WEEK</th>
        <th>AIRLINE</th>
        <th>FLIGHT_NUMBER</th>
        <th>TAIL_NUMBER</th>
        <th>ORIGIN_AIRPORT</th>
        <th>DESTINATION_AIRPORT</th>
        <th>SCHEDULED_DEPARTURE</th>
        <th>DEPARTURE_TIME</th>
        <th>DEPARTURE_DELAY</th>
        <th>TAXI_OUT</th>
        <th>WHEELS_OFF</th>
        <th>SCHEDULED_TIME</th>
        <th>ELAPSED_TIME</th>
        <th>AIR_TIME</th>
        <th>DISTANCE</th>
        <th>WHEELS_ON</th>
        <th>TAXI_IN</th>
        <th>SCHEDULED_ARRIVAL</th>
        <th>ARRIVAL_TIME</th>
        <th>ARRIVAL_DELAY</th>
        <th>DIVERTED</th>
        <th>CANCELLED</th>
        <th>CANCELLATION_REASON</th>
        <th>AIR_SYSTEM_DELAY</th>
        <th>SECURITY_DELAY</th>
        <th>AIRLINE_DELAY</th>
        <th>LATE_AIRCRAFT_DELAY</th>
        <th>WEATHER_DELAY</th>
        <th>FlightID</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>2015</td>
        <td>2</td>
        <td>18</td>
        <td>3</td>
        <td>AA</td>
        <td>6</td>
        <td>N365AA</td>
        <td>OGG</td>
        <td>DFW</td>
        <td>1815</td>
        <td>1809</td>
        <td>-6</td>
        <td>8</td>
        <td>1817</td>
        <td>424</td>
        <td>410</td>
        <td>399</td>
        <td>3711</td>
        <td>456</td>
        <td>3</td>
        <td>519</td>
        <td>459</td>
        <td>-20</td>
        <td>0</td>
        <td>0</td>
        <td>NULL</td>
        <td>NULL</td>
        <td>NULL</td>
        <td>NULL</td>
        <td>NULL</td>
        <td>NULL</td>
        <td>20150218AA0006OGGDFW</td>
      </tr>
      <tr>
        <td>2015</td>
        <td>2</td>
        <td>18</td>
        <td>3</td>
        <td>AA</td>
        <td>8</td>
        <td>N357AA</td>
        <td>HNL</td>
        <td>DFW</td>
        <td>1745</td>
        <td>1738</td>
        <td>-7</td>
        <td>11</td>
        <td>1749</td>
        <td>441</td>
        <td>428</td>
        <td>410</td>
        <td>3784</td>
        <td>439</td>
        <td>7</td>
        <td>506</td>
        <td>446</td>
        <td>-20</td>
        <td>0</td>
        <td>0</td>
        <td>NULL</td>
        <td>NULL</td>
        <td>NULL</td>
        <td>NULL</td>
        <td>NULL</td>
        <td>NULL</td>
        <td>20150218AA0008HNLDFW</td>
      </tr>
      <tr>
        <td>2015</td>
        <td>2</td>
        <td>18</td>
        <td>3</td>
        <td>AA</td>
        <td>10</td>
        <td>N795AA</td>
        <td>LAX</td>
        <td>JFK</td>
        <td>2200</td>
        <td>2155</td>
        <td>-5</td>
        <td>17</td>
        <td>2212</td>
        <td>317</td>
        <td>309</td>
        <td>287</td>
        <td>2475</td>
        <td>559</td>
        <td>5</td>
        <td>617</td>
        <td>604</td>
        <td>-13</td>
        <td>0</td>
        <td>0</td>
        <td>NULL</td>
        <td>NULL</td>
        <td>NULL</td>
        <td>NULL</td>
        <td>NULL</td>
        <td>NULL</td>
        <td>20150218AA0010LAXJFK</td>
      </tr>
    </tbody>
  </table>
</div>


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

### Sample Data:
<div style="overflow-x:auto;">
  <table>
    <thead>
      <tr>
        <th>IATA_CODE</th>
        <th>AIRLINE</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>AA</td>
        <td>American Airlines Inc.</td>
      </tr>
      <tr>
        <td>AS</td>
        <td>Alaska Airlines Inc.</td>
      </tr>
      <tr>
        <td>B6</td>
        <td>JetBlue Airways</td>
      </tr>
    </tbody>
  </table>
</div>

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


### Sample Data:
<div style="overflow-x:auto;">
  <table>
    <thead>
      <tr>
        <th>IATA_CODE</th>
        <th>AIRPORT</th>
        <th>CITY</th>
        <th>STATE</th>
        <th>COUNTRY</th>
        <th>LATITUDE</th>
        <th>LONGITUDE</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>ABE</td>
        <td>Lehigh Valley International Airport</td>
        <td>Allentown</td>
        <td>PA</td>
        <td>USA</td>
        <td>40.652359</td>
        <td>-75.440399</td>
      </tr>
      <tr>
        <td>ABI</td>
        <td>Abilene Regional Airport</td>
        <td>Abilene</td>
        <td>TX</td>
        <td>USA</td>
        <td>32.411320</td>
        <td>-99.681900</td>
      </tr>
      <tr>
        <td>ABQ</td>
        <td>Albuquerque International Sunport</td>
        <td>Albuquerque</td>
        <td>NM</td>
        <td>USA</td>
        <td>35.040218</td>
        <td>-106.609192</td>
      </tr>
    </tbody>
  </table>
</div>

---

## Relationships:
- The **Flights** table references the **Airlines** table through the **AIRLINE** column, ensuring that each flight is associated with an airline.
- The **Flights** table also references the **Airports** table twice:
  - **ORIGIN_AIRPORT** references the airport of origin.
  - **DESTINATION_AIRPORT** references the airport of destination.

![ER Diagram](https://raw.githubusercontent.com/ricmunz/DE-Python-SQL-Tests/refs/heads/main/SQL/data/tables_gen_no_data/ER%20Diagram.png)