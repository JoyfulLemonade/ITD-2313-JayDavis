#cascading units for time as we know it
Year = 365
Hours = 24 * Year
Minutes = Hours * 60
Seconds = Minutes * 60
#speed based on time units
lightSpeed = 3 ** 10 * 8
lightYearD = lightSpeed * Seconds
print(" The speed of light travels " + str(lightYearD) + " meters in a year.")
