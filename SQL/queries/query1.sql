-- This script modifies the 'Flights' table by performing the following steps:
-- 1. Drops the existing 'FlightID' column (if it exists).
-- 2. Adds a new 'FlightID' computed column, which combines the 'YEAR', 'MONTH', 'DAY', 'AIRLINE', 'FLIGHT_NUMBER', 'ORIGIN_AIRPORT', and 'DESTINATION_AIRPORT' columns to create a unique identifier for each flight.
-- 3. Adds a description for the 'FlightID' column using extended properties.
-- 4. Sets the newly created 'FlightID' column as the Primary Key for the 'Flights' table.


-- Step 1: Drop the existing FlightID column (if it exists)
IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.COLUMNS 
           WHERE TABLE_NAME = 'Flights' AND COLUMN_NAME = 'FlightID')
BEGIN
    ALTER TABLE Flights
    DROP COLUMN FlightID;
END

-- Step 2: Add the new FlightID computed column (combining YEAR, MONTH, DAY, AIRLINE, FLIGHT_NUMBER, ORIGIN_AIRPORT, and DESTINATION_AIRPORT)
ALTER TABLE Flights
ADD FlightID AS (
    CAST(YEAR AS VARCHAR(4)) + 
    RIGHT('00' + CAST(MONTH AS VARCHAR(2)), 2) + 
    RIGHT('00' + CAST(DAY AS VARCHAR(2)), 2) + 
    AIRLINE + 
    RIGHT('0000' + CAST(FLIGHT_NUMBER AS VARCHAR(4)), 4) + 
    ORIGIN_AIRPORT + 
    DESTINATION_AIRPORT
) PERSISTED NOT NULL;

-- Step 3: Add a description for the FlightID column using extended properties
EXEC sp_addextendedproperty 
    @name = N'MS_Description', 
    @value = N'FlightID is a computed column that combines the following columns: YEAR, MONTH, DAY, AIRLINE, FLIGHT_NUMBER, ORIGIN_AIRPORT, and DESTINATION_AIRPORT to generate a unique identifier for the flight.', 
    @level0type = N'SCHEMA', @level0name = dbo, 
    @level1type = N'TABLE', @level1name = Flights, 
    @level2type = N'COLUMN', @level2name = FlightID;

-- Step 4: Make the new FlightID the Primary Key
ALTER TABLE Flights
ADD CONSTRAINT PK_FlightID PRIMARY KEY (FlightID);