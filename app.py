#imports
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from flask import Flask, jsonify

#i am unable to import sqlite files without importing my OS and the app's location 
import os 
os.chdir("C:\\Users\\frcon\\Desktop\\homework\\10-Advanced-Data-Storage-and-Retrieval\\Instructions")


#db setup
engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)
Station = Base.classes.station
Measurement = Base.classes.measurement


app = Flask(__name__)

#set and define routes

@app.route("/")
def welcome():
    """list all api routes."""
    return(

        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    #create session from python to DB    
    session = Session(engine)
    results=session.query(Measurement.date, Measurement.prcp).all()
    session.close()
    #create dictionary from the data and append to a list
    #i tried a few times to get it to show the specified dates but here are all the dates at least
    datetemp = []
    for date, prcp in results:
        datetempdict = {}
        datetempdict["date"] = date
        datetempdict["prcp"] = prcp
        datetemp.append(datetempdict) 
    #jsonify and display
    return jsonify(datetemp)

@app.route("/api/v1.0/stations")
def stations():
    #create session from python to DB
    session = Session(engine)
    stations = session.query(Station.station)
    session.close()
    #create dictionary and append to list
    sstation = []
    for stations in stations:
        stationss = {}
        stationss["stations"] = stations
        sstation.append(stationss)
    #display!  
    return jsonify(sstation)

@app.route("/api/v1.0/tobs")
def tobs():
    #create session from python to DB    
    session = Session(engine)
    results2=session.query(Measurement.date, Measurement.tobs).all()
    session.close()
    #create dictionary and append to list, again, i couldnt figure out how to isolate the most recent year
    datetobs = []
    for date, prcp in results2:
        datetobsdict = {}
        datetobsdict["date"] = date
        datetobsdict["prcp"] = prcp
        datetobs.append(datetobsdict) 
    #display
    return jsonify(datetobs)
#the last bits were beyond me :(
if __name__ == '__main__':
    app.run(debug=True)