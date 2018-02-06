import datetime as dt
import numpy as np
import pandas as pd
from datetime import datetime
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, or_, and_

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurements = Base.classes.meas
Stations = Base.classes.sta

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
    	"Welcome!!!<br>"
        f"/api/v1.0/precipitation<br>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br>"
        f"/api/v1.0/<start> (enter date as mm/dd/yyyy) <br> "
        f"/api/v1.0/<start>/<end> (enter date as mm/dd/yyyy) <br>"
    )

@app.route("/api/v1.0/precipitation")
def precip():
	start_date = datetime.strptime('8/24/2016', '%m/%d/%Y')
	end_date = datetime.strptime('8/24/2017', '%m/%d/%Y')
	results = session.query(Measurements.date, Measurements.prcp).filter(and_(Measurements.date >= start_date, Measurements.date < end_date)).all()
	prcp_dict = {}
	for row in results:
		date = row[0].strftime("%Y/%m/%d")
		prcp_dict[date] = row[1]
	return jsonify(prcp_dict)


@app.route("/api/v1.0/stations")
def stations():
    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    results = session.query(Stations.station)
    station_list = []
    for row in results:
    	station_list.append(row[0])
    station_dict = {"station " : station_list}

    return jsonify(station_dict)

@app.route("/api/v1.0/tobs")
def prev_temps():
	start_date = datetime.strptime('12/20/2016', '%m/%d/%Y')
	results = session.query(Measurements.date, Measurements.tobs).filter(Measurements.date >= start_date)
	temp_dict = {}
	for row in results:
		date = row[0].strftime("%Y/%m/%d")
		temp_dict[date] = row[1]
	print(temp_dict)

	return jsonify(temp_dict)



@app.route("/api/v1.0/<start>")
def start(start):

    start_date = datetime.strptime("start", '%m-%d-%Y')

    calcs = session.query(Measurements.tobs).filter(datetime.strptime(Measurements.date, '%m/%d/%Y') >= datetime.date())

    records = []
    for record in calcs:
        records.append(record[0])
        
    tmin = min(records)
    tmax = max(records)
    tavg = np.mean(records)
    records_dict = {
                    "min_temp": tmin,
                    "max_temp": tmax,
                    "avg_temp": tavg
                    }
    return jsonify(records_dict)



@app.route("/api/v1.0/<start>/<end>")
def startend(start, end):
    start_date = datetime.strptime(start, '%m/%d/%Y')
    end_date = datetime.strptime(end, '%m/%d/%Y')
    calcs = session.query(Measurements.tobs).filter(Measurements.date >= start_date).filter(Measurements.date <= end_date)

    records = []
    for record in calcs:
        records.append(record[0])

    tmin = min(records)
    tmax = max(records)
    tavg = np.mean(records)
    records_dict = {
                    "min_temp": tmin,
                    "max_temp": tmax,
                    "avg_temp": tavg
                    }
    return jsonify(records_dict)

if __name__ == '__main__':
    app.run(debug=True)