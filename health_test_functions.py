import json


def blood_pressure(name,current_blood_pressure):
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
        file.close()
        priority = round(abs(float(current_blood_pressure)-float(blood_pressure_min))/2, 2)
        if priority > 10.0:
            priority = 10.0
        return(priority)
    elif current_blood_pressure > blood_pressure_max:
        file.close()
        priority=round(abs(float(current_blood_pressure)-float(blood_pressure_max))/2, 2)
        if priority > 10.0:
            priority = 10.0
        return(priority)
    file.close()
    return(0.0)

def bone_density(name,T_value_decrease_month):
    '''
    This function takes the name of the astronaut and their T- value decrease for this month as parameters, then compares
    them to the astronauts expected bone decay. This function then retruns a priority score based on the severity
    of the current bone decay.
    '''
    file = open("health.json", "r", encoding="utf-8")
    health = json.load(file)

    max_bone_decay = health[name]["bone density decay rate max"]

    if T_value_decrease_month < max_bone_decay:
        file.close()
        priority = round(abs(float(T_value_decrease_month)-float(max_bone_decay))*10, 2)
        if priority > 10.0:
            priority = 10.0
        return(priority)
    file.close
    return(0.0)

def heart_rate_rest(name, current_bpm):
    '''
    This function takes the name of the astronaut and their current heart rate as parameters and compares 
    it to their average resting heart rate. This function then returns a priority score based on the severity
    of the current heart rate
    '''
    file = open("health.json", "r", encoding="utf-8")
    health = json.load(file)

    bpm_min,bpm_max = health[name]["heart rate rest avg"]
    priority = 0.0
    if current_bpm < bpm_min:
        if priority > 10.0:
            priority = 10.0
        priority = round(abs(float(current_bpm)-float(min_bpm))/2, 2)
    if current_bpm > bpm_max:
        if priority > 10.0:
            priority = 10.0
        priority = round(abs(float(current_bpm)-float(max_bpm))/2, 2)
    file.close()
    return(priority)

def body_temp(name, current_body_temp):
    '''
    This function takes the name of the astronaut and their current body temperature as parameters and compares
    it to their average body temp. This function then returns a priority score based on the severity of their
    current body_temp
    '''
    file = open("health.json", "r", encoding="utf-8")
    health = json.load(file)

    body_temp_min,body_temp_max = health[name]["body temp avg"]
    priority = 0.0
    if current_body_temp < body_temp_min:
        priority = round(abs(float(current_body_temp)-float(body_temp_min)))
    if current_body_temp > body_temp_max:
        priority = round(abs(float(current_body_temp)-float(body_temp_min)))
    file.close()
    return(priority)


