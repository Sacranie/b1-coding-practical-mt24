def controller(previous_error, current_error):
    Kp = 0.15
    Kd = 0.6
    control_action = (Kp * current_error) + Kd * (current_error - previous_error)
    return control_action