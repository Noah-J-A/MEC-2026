import json


def blood_pressure(name , current_blood_pressure):
    '''
    This function takes the name of the astronuat and their current blood pressure
    as parameters, then compares it to the normal levels for that astronaut. The function
    then returns the priority score for tasks that would improve their blood pressure and or
    schedule an appointment
    '''
    file = open("health.json", "r", encoding="utf-8")
    health = json.load(file)

    blood_pressure_max = health[name]["blood pressure safe range"][1][0]
    blood_pressure_min = health[name]["blood pressure safe range"][0][0]

    if current_blood_pressure < blood_pressure_min:
        return(round(abs(float(current_blood_pressure)-float(blood_pressure_min)))/2, 2)
    elif current_blood_pressure > blood_pressure_max:
        return(round(abs(float(current_blood_pressure)-float(blood_pressure_max)))/2, 2)
    file.close
    return(0)

def bone_density(name, T-value_decrease_month):
    '''
    This function takes the name of the astronaut and their T- value decrease for this month as parameters, then compares
    them to the astronauts expected bone decay. This function then retruns a priority score based on the severity
    of the current bone decay.
    '''
    file = open("health.json", "r", encoding="utf-8")
    health = json.load(file)

    max_bone_decay = health[name]["blood pressure safe range"][1][0]
    

    if current_blood_pressure < blood_pressure_min:
        return(round(abs(float(current_blood_pressure)-float(blood_pressure_min)))/2, 2)
    elif current_blood_pressure > blood_pressure_max:
        return(round(abs(float(current_blood_pressure)-float(blood_pressure_max)))/2, 2)
    file.close
    return(0)




