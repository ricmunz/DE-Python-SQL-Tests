USE [DESQLTest]
GO
/****** Object:  Table [dbo].[Flights]    Script Date: 12/6/2024 6:48:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Flights](
	[YEAR] [smallint] NOT NULL,
	[MONTH] [tinyint] NOT NULL,
	[DAY] [tinyint] NOT NULL,
	[DAY_OF_WEEK] [tinyint] NOT NULL,
	[AIRLINE] [nvarchar](2) NOT NULL,
	[FLIGHT_NUMBER] [smallint] NOT NULL,
	[TAIL_NUMBER] [nvarchar](20) NULL,
	[ORIGIN_AIRPORT] [nvarchar](3) NOT NULL,
	[DESTINATION_AIRPORT] [nvarchar](3) NOT NULL,
	[SCHEDULED_DEPARTURE] [smallint] NOT NULL,
	[DEPARTURE_TIME] [smallint] NULL,
	[DEPARTURE_DELAY] [int] NULL,
	[TAXI_OUT] [smallint] NULL,
	[WHEELS_OFF] [smallint] NULL,
	[SCHEDULED_TIME] [smallint] NOT NULL,
	[ELAPSED_TIME] [smallint] NULL,
	[AIR_TIME] [smallint] NULL,
	[DISTANCE] [smallint] NOT NULL,
	[WHEELS_ON] [smallint] NULL,
	[TAXI_IN] [smallint] NULL,
	[SCHEDULED_ARRIVAL] [smallint] NOT NULL,
	[ARRIVAL_TIME] [smallint] NULL,
	[ARRIVAL_DELAY] [int] NULL,
	[DIVERTED] [int] NOT NULL,
	[CANCELLED] [bit] NOT NULL,
	[CANCELLATION_REASON] [nvarchar](255) NULL,
	[AIR_SYSTEM_DELAY] [int] NULL,
	[SECURITY_DELAY] [int] NULL,
	[AIRLINE_DELAY] [int] NULL,
	[LATE_AIRCRAFT_DELAY] [int] NULL,
	[WEATHER_DELAY] [int] NULL,
	[FlightID]  AS ((((((CONVERT([varchar](4),[YEAR])+right('00'+CONVERT([varchar](2),[MONTH]),(2)))+right('00'+CONVERT([varchar](2),[DAY]),(2)))+[AIRLINE])+right('0000'+CONVERT([varchar](4),[FLIGHT_NUMBER]),(4)))+[ORIGIN_AIRPORT])+[DESTINATION_AIRPORT]) PERSISTED NOT NULL,
 CONSTRAINT [PK_FlightID] PRIMARY KEY CLUSTERED 
(
	[FlightID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Flights]  WITH CHECK ADD  CONSTRAINT [FK_Flights_Airlines] FOREIGN KEY([AIRLINE])
REFERENCES [dbo].[Airlines] ([IATA_CODE])
GO
ALTER TABLE [dbo].[Flights] CHECK CONSTRAINT [FK_Flights_Airlines]
GO
ALTER TABLE [dbo].[Flights]  WITH CHECK ADD  CONSTRAINT [FK_Flights_DestinationAirport] FOREIGN KEY([DESTINATION_AIRPORT])
REFERENCES [dbo].[Airports] ([IATA_CODE])
GO
ALTER TABLE [dbo].[Flights] CHECK CONSTRAINT [FK_Flights_DestinationAirport]
GO
ALTER TABLE [dbo].[Flights]  WITH CHECK ADD  CONSTRAINT [FK_Flights_OriginAirport] FOREIGN KEY([ORIGIN_AIRPORT])
REFERENCES [dbo].[Airports] ([IATA_CODE])
GO
ALTER TABLE [dbo].[Flights] CHECK CONSTRAINT [FK_Flights_OriginAirport]
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'FlightID is a computed column that combines the following columns: YEAR, MONTH, DAY, AIRLINE, FLIGHT_NUMBER, ORIGIN_AIRPORT, and DESTINATION_AIRPORT to generate a unique identifier for the flight.' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Flights', @level2type=N'COLUMN',@level2name=N'FlightID'
GO
