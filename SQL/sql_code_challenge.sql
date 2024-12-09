--* =======================================================
--* === SQL Code Challenge: Code and Question Responses ===
--* =======================================================

--*
--* Task 1
--* We need to prioritize read performance. There are no more data being added to this historical dataset. The data will be queried extensively by an analysis team for the next 9 months. You choose your approach for all queries below. 

--* [Return all the fields from 20 records ]
SELECT
    TOP 20 Flights.*,
    Airlines.AIRLINE,
    OriginAirports.AIRPORT AS OriginAirport,
    DestinationAirports.AIRPORT AS DestinationAirport
FROM
    Flights
    JOIN Airlines ON Flights.AIRLINE = Airlines.IATA_CODE
    JOIN Airports AS OriginAirports ON Flights.ORIGIN_AIRPORT = OriginAirports.IATA_CODE
    JOIN Airports AS DestinationAirports ON Flights.DESTINATION_AIRPORT = DestinationAirports.IATA_CODE;

--* [How would you rate the efficiency of the code in terms of the number of records queried?]
--> This 20 records retrieval is efficient since we are not doing any complex filtering
--> and SQL Server will stop scanning the table once it finds the 20th record.

--* [Return all of the destination airports and the corresponding arrival time where the take off time was before 11AM (ignore timezones)]
--> Filtering before join should reduce the number of records scanned/joined.
SELECT
    Flights.DESTINATION_AIRPORT,
    DestinationAirports.AIRPORT AS AIRPORT_NAME,
    Flights.ARRIVAL_TIME
FROM
    (
        SELECT
            DESTINATION_AIRPORT,
            ARRIVAL_TIME
        FROM
            Flights
        WHERE
            DEPARTURE_TIME < 1100
    ) AS Flights
    JOIN Airports AS DestinationAirports ON Flights.DESTINATION_AIRPORT = DestinationAirports.IATA_CODE;

--* [What is the longest flight time?]
SELECT
    MAX(ELAPSED_TIME) AS LONGEST_FLIGHT_TIME
FROM
    Flights;

--* How many different airlines are in the dataset?
SELECT
    COUNT(DISTINCT AIRLINE) AS DISTINCT_AIRLINES
FROM
    Flights;

--*
--* Task #2
--* 

--* [The correlation between distance of the flight and the actual arrival time]
--* [The correlation between the arrival delay and the theoretical time a flight should be in the air (AIR_TIME) ]
-->  These two were omitted from lack of correlation function in SQL Server.

--* [The specific number of flights that go to a given airport.]
--* [The average amount of time for each of those flights is in the air]
--* [Order the output by the most frequent destination airports]
--* [We are targeting the top 5 most frequent destination airports for this analysis, so we just need those results.]
SELECT
    TOP 5 DESTINATION_AIRPORT,
    COUNT(*) AS NUMBER_OF_FLIGHTS,
    AVG(AIR_TIME) AS AVERAGE_AIRTIME
FROM
    Flights
GROUP BY
    DESTINATION_AIRPORT
ORDER BY
    NUMBER_OF_FLIGHTS DESC;

--
--* === Questions ===
--* 1. Remember this is historical data taken from daily operations, and assume that the data are being written nearly real-time.
--* 2. You are allowed to create any data model that you desired for these analyses. Why or why not would your model be efficient enough for use when the dataset was being written? 
--    For these two, I shall part from the premise of how I loaded the data onto my model. Because I strictly used SSMS GUI for
--    loading my dataset, this was extremely inefficient and I recognize this is an area that would benefit from more practice in
--    establishing pipelines for programatically loading CSVs with SQL scripts like I am more familiar with in Python.
--    Because the dataset is well structured already, it works well for my model. However, without this structure and
--    requiring non-relational db's, this is an area I am eager to expand upon with SQL.
-- 
--* 3. Your team has been implementing No-SQL databases for OTHER datasets. This has proven useful and your supervisor is curious to know if you’d recommend that approach here. What would you do? 
--    This is an area where I am missing hands-on experience. Though I understand that NoSQL databases can effective for handling 
--    large volumes of data on scalable system architectures in real-time intake scenarios. Given that the team has successfully
--    implemented it for other datasets, I am intrigued in further evaluating the specifics of the datasets and other considerations 
--    prior to making a proper recommendation.

--
--* === Consider the following columns ===
--* [ YEAR | MONTH | DAY | DAY_OF_WEEK | AIRLINE | FLIGHT_NUMBER | TAIL_NUMBER ]
--* Inspect the data types. Do you think each is appropriate for the content of the data? If not, how would you change those? Why? Note: Do not assume this question implies the data types are incorrect. For each field, explain what and why you would change/maintain the data types.
-- 
--   There were no data types included with the datasets or presented separately. As I imported the CSVs to SSMS, 
--   it did pre-fill some data types which I then modified. It defaulted to nvarchar(50) for AIRLINE and TAIL_NUMBER. 
--   For AIRILINE, by looking at the AIRLINES table I noticed the values followed the IATA specification which dictated 
--   these should be two characters long. 
--
--   For MONTH (1-12), DAY (1-31) and DAY_OF_WEEK(1-7), I chose tinyint. With YEAR(1903-2999), I chose smallint because
--   it’s the next step up from tiny. All these seem more efficient than simple integer types. 
--   FLIGHT_NUMBER possible range seems to be 1-9999 so I chose smallint as well.
--
--   I did choose a 20 char length for TAIL_NUMBER as an initial guesstimate but it might likely not exceed 6-8. 
--   However, I went with 20 to give myself some wiggle room in case I had underestimated this length.
--   I chose this route as a better alternative to be able to fit the data accurately with a storage overhead instead 
--   of ending up with erroneous data because of implicit conversions or records getting dropped during import. 
--   Not ideal but usable given my time constraints.