# Plaintext Output of **code_challenge.py**

Disabled default use of ANSI escape code styling in function print_bold(). Each section/task header should have bold.

```bash
==== application_in 	(Original) ====
DataFrame Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 12 columns):
 #   Column               Non-Null Count  Dtype         
---  ------               --------------  -----         
 0   countyname           1000 non-null   object        
 1   party                1000 non-null   object        
 2   dateofbirth          1000 non-null   datetime64[ns]
 3   mailapplicationtype  1000 non-null   object        
 4   appissuedate         1000 non-null   datetime64[ns]
 5   appreturndate        1000 non-null   datetime64[ns]
 6   ballotsentdate       998 non-null    datetime64[ns]
 7   ballotreturneddate   822 non-null    datetime64[ns]
 8   legislative          1000 non-null   object        
 9   senate               1000 non-null   object        
 10  congressional        1000 non-null   object        
 11  is_confidential      1000 non-null   bool          
dtypes: bool(1), datetime64[ns](5), object(6)
memory usage: 87.0+ KB
None 

First 5 rows:
   countyname party dateofbirth mailapplicationtype appissuedate  \
0  SCHUYLKILL   NOP  1946-11-11              MAILIN   2020-08-27   
1    DELAWARE     D  2002-07-25             OLMAILV   2020-09-01   
2       BERKS     D  1998-10-04             OLMAILV   2020-04-15   
3      BEAVER     D  1963-11-18             OLMAILV   2020-08-05   
4     DAUPHIN     D  1963-01-11             OLMAILV   2020-04-10   

  appreturndate ballotsentdate ballotreturneddate  \
0    2020-08-27     2020-08-27         2020-10-23   
1    2020-09-01     2020-10-03         2020-10-21   
2    2020-04-15     2020-10-07         2020-10-21   
3    2020-08-05     2020-09-24         2020-10-19   
4    2020-04-10     2020-10-05         2020-10-19   

                   legislative                    senate  \
0   123RD LEGISLATIVE DISTRICT  29TH SENATORIAL DISTRICT   
1   161ST LEGISLATIVE DISTRICT  26TH SENATORIAL DISTRICT   
2   129TH LEGISLATIVE DISTRICT  29TH SENATORIAL DISTRICT   
3    15TH LEGISLATIVE DISTRICT  47TH SENATORIAL DISTRICT   
4  106TH  LEGISLATIVE DISTRICT  48TH SENATORIAL DISTRICT   

                 congressional  is_confidential  
0   9TH CONGRESSIONAL DISTRICT            False  
1   5TH CONGRESSIONAL DISTRICT            False  
2   9TH CONGRESSIONAL DISTRICT            False  
3  17TH CONGRESSIONAL DISTRICT            False  
4  10TH CONGRESSIONAL DISTRICT            False  


==== invalid_data ====
DataFrame Info:
<class 'pandas.core.frame.DataFrame'>
Index: 180 entries, 11 to 996
Data columns (total 12 columns):
 #   Column               Non-Null Count  Dtype         
---  ------               --------------  -----         
 0   countyname           180 non-null    object        
 1   party                180 non-null    object        
 2   dateofbirth          180 non-null    datetime64[ns]
 3   mailapplicationtype  180 non-null    object        
 4   appissuedate         180 non-null    datetime64[ns]
 5   appreturndate        180 non-null    datetime64[ns]
 6   ballotsentdate       178 non-null    datetime64[ns]
 7   ballotreturneddate   2 non-null      datetime64[ns]
 8   legislative          180 non-null    object        
 9   senate               180 non-null    object        
 10  congressional        180 non-null    object        
 11  is_confidential      180 non-null    bool          
dtypes: bool(1), datetime64[ns](5), object(6)
memory usage: 17.1+ KB
None 

First 5 rows:
   countyname party dateofbirth mailapplicationtype appissuedate  \
11   DELAWARE     R  1960-02-05              MAILIN   2020-05-28   
22   DELAWARE     D  1978-04-25             OLMAILV   2020-05-25   
23    DAUPHIN     R  1981-12-31             OLMAILV   2020-05-06   
29   DELAWARE     D  1998-05-11             OLMAILV   2020-09-07   
31  LANCASTER     R  1960-01-25             OLMAILV   2020-04-30   

   appreturndate ballotsentdate ballotreturneddate  \
11    2020-05-28     2020-10-03                NaT   
22    2020-05-25     2020-10-03                NaT   
23    2020-05-06     2020-10-05                NaT   
29    2020-09-07     2020-10-03                NaT   
31    2020-04-30     2020-10-06                NaT   

                   legislative                    senate  \
11  159TH LEGISLATIVE DISTRICT   9TH SENATORIAL DISTRICT   
22  162ND LEGISLATIVE DISTRICT  26TH SENATORIAL DISTRICT   
23  104TH LEGISLATIVE DISTRICT  15TH SENATORIAL DISTRICT   
29  185TH LEGISLATIVE DISTRICT   8TH SENATORIAL DISTRICT   
31   99TH LEGISLATIVE DISTRICT  36TH SENATORIAL DISTRICT   

                  congressional  is_confidential  
11   5TH CONGRESSIONAL DISTRICT            False  
22   5TH CONGRESSIONAL DISTRICT            False  
23  10TH CONGRESSIONAL DISTRICT            False  
29   5TH CONGRESSIONAL DISTRICT            False  
31  11TH CONGRESSIONAL DISTRICT            False  


==== application_in 	(After dropping null values) ====
DataFrame Info:
<class 'pandas.core.frame.DataFrame'>
Index: 820 entries, 0 to 999
Data columns (total 12 columns):
 #   Column               Non-Null Count  Dtype         
---  ------               --------------  -----         
 0   countyname           820 non-null    object        
 1   party                820 non-null    object        
 2   dateofbirth          820 non-null    datetime64[ns]
 3   mailapplicationtype  820 non-null    object        
 4   appissuedate         820 non-null    datetime64[ns]
 5   appreturndate        820 non-null    datetime64[ns]
 6   ballotsentdate       820 non-null    datetime64[ns]
 7   ballotreturneddate   820 non-null    datetime64[ns]
 8   legislative          820 non-null    object        
 9   senate               820 non-null    object        
 10  congressional        820 non-null    object        
 11  is_confidential      820 non-null    bool          
dtypes: bool(1), datetime64[ns](5), object(6)
memory usage: 77.7+ KB
None 

First 5 rows:
   countyname party dateofbirth mailapplicationtype appissuedate  \
0  SCHUYLKILL   NOP  1946-11-11              MAILIN   2020-08-27   
1    DELAWARE     D  2002-07-25             OLMAILV   2020-09-01   
2       BERKS     D  1998-10-04             OLMAILV   2020-04-15   
3      BEAVER     D  1963-11-18             OLMAILV   2020-08-05   
4     DAUPHIN     D  1963-01-11             OLMAILV   2020-04-10   

  appreturndate ballotsentdate ballotreturneddate  \
0    2020-08-27     2020-08-27         2020-10-23   
1    2020-09-01     2020-10-03         2020-10-21   
2    2020-04-15     2020-10-07         2020-10-21   
3    2020-08-05     2020-09-24         2020-10-19   
4    2020-04-10     2020-10-05         2020-10-19   

                   legislative                    senate  \
0   123RD LEGISLATIVE DISTRICT  29TH SENATORIAL DISTRICT   
1   161ST LEGISLATIVE DISTRICT  26TH SENATORIAL DISTRICT   
2   129TH LEGISLATIVE DISTRICT  29TH SENATORIAL DISTRICT   
3    15TH LEGISLATIVE DISTRICT  47TH SENATORIAL DISTRICT   
4  106TH  LEGISLATIVE DISTRICT  48TH SENATORIAL DISTRICT   

                 congressional  is_confidential  
0   9TH CONGRESSIONAL DISTRICT            False  
1   5TH CONGRESSIONAL DISTRICT            False  
2   9TH CONGRESSIONAL DISTRICT            False  
3  17TH CONGRESSIONAL DISTRICT            False  
4  10TH CONGRESSIONAL DISTRICT            False  


==== application_in['senate'] 	(snake case) ====
0    29th_senatorial_district
1    26th_senatorial_district
2    29th_senatorial_district
3    47th_senatorial_district
4    48th_senatorial_district
Name: senate, dtype: object


==== application_in 	(Added 'yr_born' column) ====
First 5 rows:
   countyname party dateofbirth  yr_born mailapplicationtype appissuedate  \
0  SCHUYLKILL   NOP  1946-11-11     1946              MAILIN   2020-08-27   
1    DELAWARE     D  2002-07-25     2002             OLMAILV   2020-09-01   
2       BERKS     D  1998-10-04     1998             OLMAILV   2020-04-15   
3      BEAVER     D  1963-11-18     1963             OLMAILV   2020-08-05   
4     DAUPHIN     D  1963-01-11     1963             OLMAILV   2020-04-10   

  appreturndate ballotsentdate ballotreturneddate  \
0    2020-08-27     2020-08-27         2020-10-23   
1    2020-09-01     2020-10-03         2020-10-21   
2    2020-04-15     2020-10-07         2020-10-21   
3    2020-08-05     2020-09-24         2020-10-19   
4    2020-04-10     2020-10-05         2020-10-19   

                   legislative                    senate  \
0   123RD LEGISLATIVE DISTRICT  29th_senatorial_district   
1   161ST LEGISLATIVE DISTRICT  26th_senatorial_district   
2   129TH LEGISLATIVE DISTRICT  29th_senatorial_district   
3    15TH LEGISLATIVE DISTRICT  47th_senatorial_district   
4  106TH  LEGISLATIVE DISTRICT  48th_senatorial_district   

                 congressional  is_confidential  
0   9TH CONGRESSIONAL DISTRICT            False  
1   5TH CONGRESSIONAL DISTRICT            False  
2   9TH CONGRESSIONAL DISTRICT            False  
3  17TH CONGRESSIONAL DISTRICT            False  
4  10TH CONGRESSIONAL DISTRICT            False  


==== Correlation matrix: Age and Party (All parties) ====
                   age  party_encoded
age            1.00000       -0.06044
party_encoded -0.06044        1.00000


==== Correlation matrix: Age and Party (Dem,Rep,Other) ====
                   age  party_encoded
age            1.00000       -0.13937
party_encoded -0.13937        1.00000


==== Median day latency per district between app issue and ballot return (legislative) ====
First 5 rows:
                  legislative  median_latency_days
0  100TH LEGISLATIVE DISTRICT                 28.0
1  101ST LEGISLATIVE DISTRICT                 85.0
2  102ND LEGISLATIVE DISTRICT                124.0
3  103RD LEGISLATIVE DISTRICT                 55.0
4  104TH LEGISLATIVE DISTRICT                 11.5


==== Congressional district with most ballot requests ====
                 congressional  count
11  3RD CONGRESSIONAL DISTRICT     84


==== Drawing plot for visualizing Democrat and Republican application counts by county ====

```

![plot image](/Python/plot_image.png)