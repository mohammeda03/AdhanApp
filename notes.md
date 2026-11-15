# Notes on Adhan Calculation
## Fajr
--------------------------------------------------
Fajr is calculated using the sun's depression angle below the Eastern horizon. Using the Islamic Society of North America (ISNA) method, we'd use the 15 degree solar depression angle. 

## Dhuhr
Dhuhr is calculated at solar noon, which is the exact moment the sun crosses the local median. In Chicago this is 87.6 degrees W longitude. Add between 1 to 5 minutes buffer to avoid true solar nooon since that's prohibited (A window called *Zawal* at its exact zenith). 

## Asr
It's calculated from the sun's elevation angle when an object's shadow reaches a specific length relative to its midday shadow. My family uses thes Shafi'i standard, which is when an object's shadow equals its own height plus it's midday shadow. 

## Maghrib

Calculated at the exact moment the upper edge of the sun disappears below the Chicago's western horizon, accounting for the standard atmospheric refraction. 

## Isha
Isha is calculated using the same 15 degree depression as Fajr

## How I'll actually get the prayer times
Instead of hand calculating them by location (Nearly impossible I'd say for all locations), I'll use an API. After researching some, I'm using the AlAdhan API (https://gist.github.com/Zxce3/e1cc0363de3694e04bb440a5c8d57726)

## V1
I'll start with V1, which is just the daily adhan times for Chicago. This seems to be esaily done by the "GET /timingsByCity/{date}" API call. This is the documented example: 
GET /timingsByCity/2023-12-01?city=Dubai&country=AE&method=8
