# Read Pysense sensor data
def PysenseReadSensor(py, si, mp, li, lt, rtc):
    # Pysense battery voltage data sensor
    py_batt = py.read_battery_voltage()         # PysenseReading[12], volts

    # Pysense SI data sensor
    si_temp = si.temperature()                  # PysenseReading[0], degC
    si_hmdt = si.humidity()                     # PysenseReading[1], %RH
    si_dewp = si.dew_point()                    # PysenseReading[2], degC

    # Pysense MP mode ALTITUDE data sensor
    mp_temp = mp.temperature()                  # PysenseReading[3], degC
    mp_alt  = mp.altitude()                     # PysenseReading[4], meters

    # Pysense LI data sensor
    li_roll = li.roll()                         # PysenseReading[5], Angle in degrees. Range -180 to +180.
    li_ptch = li.pitch()                        # PysenseReading[6], Angle in degrees. Range -90 to +90.
    li_acc  = li.acceleration()
    li_accX = li_acc[0]                         # PysenseReading[7], G
    li_accY = li_acc[1]                         # PysenseReading[8], G
    li_accZ = li_acc[2]                         # PysenseReading[9], G

    # Pysense LTL data sensor
    ltl = lt.light()
    ltlB = ltl[0]                               # PysenseReading[10], lux
    ltlR = ltl[1]                               # PysenseReading[11], lux

    # Pysense MP mode PRESSSURE data sensor
    #mpp_press = mpp.presssure()/100             Unit hPa

    # Real Time Clock of the measurement
    rtc_now = rtc.now()                         # Year, Month, Day, Hour, Min, Sec, usec, tzinfo
    rtc_yr  = rtc_now[0]
    rtc_mth = rtc_now[1]
    rtc_day = rtc_now[2]
    rtc_hr  = rtc_now[3]
    rtc_min = rtc_now[4]
    rtc_sec = rtc_now[5]
    rtc_time= str(rtc_yr)+"-"+str(rtc_mth)+"-"+str(rtc_day)+" "+str(rtc_hr)+":"+str(rtc_min)+":"+str(rtc_sec)     #PysenseReading[13]

    PysenseReading = [si_temp, si_hmdt, si_dewp, mp_temp, mp_alt, li_roll, li_ptch, li_accX, li_accY, li_accZ, ltlB, ltlR, py_batt, rtc_time]

    return PysenseReading


# Pysense sensor message pack JSON formatting (IBM Cloud)
def JSONPysensePack_IBM(PysenseReading):

    PysensePack = {'si_temp' : PysenseReading[0],  # in degC.
                   'si_hmdt' : PysenseReading[1],  # in %RH.
                   'si_dewp' : PysenseReading[2],  # in degC.
                   'mp_temp' : PysenseReading[3],  # in degC.
                   'mp_alt'  : PysenseReading[4],  # in m.
                   'li_roll' : PysenseReading[5],  # Angle in deg. Range -180 to +180.
                   'li_ptch' : PysenseReading[6],  # Angle in deg. Range -90 to +90.
                   'li_accX' : PysenseReading[7],  # X channel in G.
                   'li_accY' : PysenseReading[8],  # Y channel in G.
                   'li_accZ' : PysenseReading[9],  # Z channel in G.
                   'ltlB'    : PysenseReading[10], # Blue channel in lux.
                   'ltlR'    : PysenseReading[11], # Red channel in lux.
                   'py_batt' : PysenseReading[12], # in volts.
                   'rtc_time': PysenseReading[13]  # yyyy-mm-dd hh:mm:ss
    }

    return PysensePack


# Pysense sensor message pack JSON formatting (AWS)
def JSONPysensePack_AWS(PysenseReading):

    # Shadow JSON schema:
    #
    # Name: Bot
    # {
    #	"state": {
    #		"reported":{
    #			"property1": value1
    #           "property2": value2
    #           etc...
    #		}
    #	}
    # }

    PysensePack = {
        "state": {
            "reported": {
                'si_temp' : PysenseReading[0],  # in degC.
                'si_hmdt' : PysenseReading[1],  # in %RH.
                'si_dewp' : PysenseReading[2],  # in degC.
                'mp_temp' : PysenseReading[3],  # in degC.
                'mp_alt'  : PysenseReading[4],  # in m.
                'li_roll' : PysenseReading[5],  # Angle in deg. Range -180 to +180.
                'li_ptch' : PysenseReading[6],  # Angle in deg. Range -90 to +90.
                'li_accX' : PysenseReading[7],  # X channel in G.
                'li_accY' : PysenseReading[8],  # Y channel in G.
                'li_accZ' : PysenseReading[9],  # Z channel in G.
                'ltlB'    : PysenseReading[10], # Blue channel in lux.
                'ltlR'    : PysenseReading[11], # Red channel in lux.
                'py_batt' : PysenseReading[12], # in volts.
                'rtc_time': PysenseReading[13]  # yyyy-mm-dd hh:mm:ss
                        }
                }
    }

    return PysensePack


# Data sensor message single JSON formatting (Tago)
def JSONPysenseMsg_Tago(msg_variable, msg_unit, msg_value, msg_time):

    # Template JSON message
    #PysenseMsg = {
                #"variable"  : "xxx",
                #"unit"      : "xxx",
                #"value"     : xxx,
                #"time"      : xxx,
                #"serie"     : xxx,
                #"location"  : {
                #    "lat"   : xxx,
                #    "lng"   : xxx,
                #    },
                #"metadata"  : {
                #    "color" : "green"
                #    }
                #}

    PysenseMsg = {
                "variable"  : msg_variable,
                "unit"      : msg_unit,
                "value"     : msg_value,
                "time"      : msg_time
    }

    return PysenseMsg
