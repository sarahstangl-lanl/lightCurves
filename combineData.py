import matplotlib.pyplot as plt
import numpy as np
import re
import os.path
import math
import datetime



def mjd_to_calendar(mjd):
		jd = mjd + 2400000.5 + 0.5

		"""
		this is the algorithm converting JD to calendar date in Chapter 7 of Jean Meeus' Astronomical Algorithms Second Edition
		"""

		Z = int(jd)
		F = jd % 1

		A = 0
		alpha = 0
		if Z < 2299161:
			A = Z
		else:
			alpha = int((Z - 1867216.25)/36524.25)
			A = Z + 1 + alpha - int(alpha/4)

		B = A + 1524
		C = int((B - 122.1)/365.25)
		D = int(365.25 * C)
		E = int((B-D)/30.6001)

		day = B - D - int(30.6001 * E) + F
		month = 0
		if E < 14:
			month = E - 1
		if E == 14 or E == 15:
			month = E - 13

		year = 0
		if month > 2:
			year = C - 4716
		if month == 1 or month ==2:
			year = C - 4715


		fracDay = day % 1
		hours = int(fracDay * 24)
		minutes = int(((fracDay * 24) % 1) * 60)
		seconds = int(((((fracDay * 24) % 1) * 60) % 1) * 60)
		day = int(day)
		calendarDate = str(month) + '-' + str(day) + '-' + str(year) + ' ' + str(hours) + ':' + str(minutes) + ':' + str(seconds)

		## year, month, day, hour, minute, second, microsecond

		calendarDate = datetime.datetime(year, month, day, hours, minutes, seconds)

		return calendarDate




skip = []

for f in '604 1001 1005 2022 608 593 2016 790 601 803 991 1882'.split():
	fname = "txt/lc_" + f

	b = True

	for x in ["B", "V", "U", "R"]:
		if not os.path.isfile(fname + "_" + x + ".txt"):
			skip.append("lc_" + f + "_" + x + ".txt")
			b = False

	if not b:
		continue

	print("Processing " + f)

	B_mag = []
	B_mjd = []
	B_calendarDate = []
	B_errors = []

	R_mag = []
	R_mjd = []
	R_calendarDate = []
	R_errors = []

	U_mag = []
	U_mjd = []
	U_calendarDate = []
	U_errors = []

	V_mag = []
	V_mjd = []
	V_calendarDate = []
	V_errors = []

	i = 0
	file = open(fname + "_B.txt", "r") 
	for line in file:
		if i == 0:
			line = 0
		else:
			line = str.split(line)
			B_calendarDate.append(mjd_to_calendar(float(line[0])))
			B_mjd.append(float(line[0]))
			B_mag.append(float(line[1]))
			B_errors.append(float(line[2]))
		i += 1

	i = 0
	file = open(fname + "_R.txt", "r") 
	for line in file:
		if i == 0:
			line = 0
		else:
			line = str.split(line)
			R_calendarDate.append(mjd_to_calendar(float(line[0])))
			R_mjd.append(float(line[0]))
			R_mag.append(float(line[1]))
			R_errors.append(float(line[2]))
		i += 1

	i = 0
	file = open(fname + "_U.txt", "r") 
	for line in file:
		if i == 0:
			line = 0
		else:
			line = str.split(line)
			U_calendarDate.append(mjd_to_calendar(float(line[0])))
			U_mjd.append(float(line[0]))
			U_mag.append(float(line[1]))
			U_errors.append(float(line[2]))
		i += 1

	i = 0
	file = open(fname + "_V.txt", "r") 
	for line in file:
		if i == 0:
			line = 0
		else:
			line = str.split(line)
			V_calendarDate.append(mjd_to_calendar(float(line[0])))
			V_mjd.append(float(line[0]))
			V_mag.append(float(line[1]))
			V_errors.append(float(line[2]))
		i += 1


	"""
	fig = plt.figure()
	ax1 = fig.add_subplot(111)
	ax2 = ax1.twiny()

	ax1.plot(B_mjd, B_mag, 'b.', label = 'B')
	ax2.plot(B_calendarDate, B_mag,'b.', alpha = 0.0)
	ax1.plot(R_mjd, R_mag, 'r.', label = 'R')
	ax2.plot(R_calendarDate, R_mag, 'r.', alpha = 0.0)
	ax1.plot(U_mjd, U_mag, 'k.', label = 'U')
	ax2.plot(U_calendarDate, U_mag, 'k.', alpha = 0.0)
	ax1.plot(V_mjd, V_mag, 'm.', label = 'V')
	ax2.plot(V_calendarDate, V_mag, 'm.', alpha = 0.0) 

	ax1.set_xlabel('MJD')
	ax2.set_xlabel('Calendar Date')
	ax1.set_ylabel('Magnitude')

	XmjdMin = min([min(B_mjd),min(R_mjd),min(U_mjd),min(V_mjd)])
	XcalMin = min([min(B_calendarDate),min(R_calendarDate),min(U_calendarDate),min(V_calendarDate)])

	XmjdMax = max([max(B_mjd),max(R_mjd),max(U_mjd),max(V_mjd)])
	XcalMax = max([max(B_calendarDate),max(R_calendarDate),max(U_calendarDate),max(V_calendarDate)])

	ax1.set_xlim(XmjdMin,XmjdMax) #mjd
	ax2.set_xlim(XcalMin,XcalMax) #calendar

	Ymin = [min(B_mag),min(R_mag),min(U_mag),min(V_mag)]
	Ymax = [max(B_mag),max(R_mag),max(U_mag),max(V_mag)]
	ax1.set_yticks(np.arange(min(Ymin), max(Ymax), 0.1))
	ax2.set_yticks(np.arange(min(Ymin), max(Ymax), 0.1))

	ax1.legend(loc = 'center left', bbox_to_anchor = (1, 0.5))
	plt.subplots_adjust(right = .87)

	fig.savefig(f + '.png')
	"""

	wb = Workbook()
	ws = wb.active

	maxlength = max([len(B_mag),len(R_mag),len(U_mag),len(V_mag)])

	titleRow = ['B MJD','B Calendar Date', 'B Magnitutde', 'B Mag Error','R MJD','R Calendar Date', 'R Magnitutde', 'R Mag Error','U MJD','U Calendar Date', 'U Magnitutde', 'U Mag Error','V MJD','V Calendar Date', 'V Magnitutde', 'V Mag Error']
	ws.append(titleRow)
	for i in xrange(0, maxlength):
		row = []
		if i < len(B_mag):
			row.append(B_mjd[i])
			row.append(B_calendarDate[i])
			row.append(B_mag[i])
			row.append(B_errors[i])
		else:
			row.append("")
			row.append("")
			row.append("")
			row.append("")

		if i < len(R_mag):
			row.append(R_mjd[i])
			row.append(R_calendarDate[i])
			row.append(R_mag[i])
			row.append(R_errors[i])
		else:
			row.append("")
			row.append("")
			row.append("")
			row.append("")

		if i < len(U_mag):
			row.append(U_mjd[i])
			row.append(U_calendarDate[i])
			row.append(U_mag[i])
			row.append(U_errors[i])
		else:
			row.append("")
			row.append("")
			row.append("")
			row.append("")

		if i < len(V_mag):
			row.append(V_mjd[i])
			row.append(V_calendarDate[i])
			row.append(V_mag[i])
			row.append(V_errors[i])
		else:
			row.append("")
			row.append("")
			row.append("")
			row.append("")
		ws.append(row)

	date_style = Style(number_format="M/D/YYYY")
	for col in [2,6,10,14]:
		for row in range(2,maxlength+2,1):
			ws.cell(row=row,column=col).style = date_style

	Ymin = np.nanmin([np.nanmin(B_mag),np.nanmin(R_mag),np.nanmin(U_mag),np.nanmin(V_mag)])
	Ymax = np.nanmax([np.nanmax(B_mag),np.nanmax(R_mag),np.nanmax(U_mag),np.nanmax(V_mag)])

	chart = ScatterChart()
	chart.title = f
	chart.style = 13
	chart.x_axis.title = 'Modified Julian Date'
	chart.y_axis.title = 'Magnitude'
	chart.y_axis.scaling.min = Ymin
	chart.y_axis.scaling.max = Ymax
	chart.y_axis.unit = 0.5

	for i in [3,7,11,15]:
		xvalues = Reference(ws, min_col=i - 2, min_row=2, max_row=maxlength+1)
		yvalues = Reference(ws, min_col=i,     min_row=1, max_row=maxlength+1)
		series = Series(yvalues, xvalues, title_from_data=True)

		series.marker = marker.Marker('circle')
		series.graphicalProperties.line.noFill=True
		chart.y_axis.scaling.orientation="maxMin"
		chart.series.append(series)

	chart2 = ScatterChart()
	chart2.title = f
	chart2.style = 13
	chart2.x_axis.title = 'Calendar Date'
	chart2.y_axis.title = 'Magnitude'
	chart2.y_axis.scaling.min = Ymin
	chart2.y_axis.scaling.max = Ymax
	chart2.y_axis.unit = 0.5

	for i in [3,7,11,15]:
		xvalues2 = Reference(ws, min_col=i - 1, min_row=2, max_row=maxlength+1)
		yvalues2 = Reference(ws, min_col=i,     min_row=1, max_row=maxlength+1)
		series2 = Series(yvalues2, xvalues2, title_from_data=True)

		series2.marker = marker.Marker('circle')
		series2.graphicalProperties.line.noFill=True
		chart2.y_axis.scaling.orientation="maxMin"
		chart2.series.append(series2)

	ws.add_chart(chart, "N5")
	
	wb.save("xlsxChip1/lc_" + f + ".xlsx")

