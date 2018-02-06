import datetime as dt
import numpy as np
import pandas as pd
from datetime import datetime, date
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



#################################################
# Flask Routes
#################################################


calcs = session.query(Measurements.date, Measurements.tobs)

records = []
for record in calcs:
    records.append(record[0])
# print(records)

dater = date.strptime("12-20-2016", '%m-%d-%Y')
print(type(dater))
# tmin = min(records)
# tmax = max(records)
# tavg = np.mean(records)
# records_dict = {
#                 "min_temp": tmin,
#                 "max_temp": tmax,
#                 "avg_temp": tavg
#                 }
# return jsonify(records_dict)