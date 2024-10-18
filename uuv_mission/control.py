class Control:
    def __init__(self, Kd=0.15, Kp=0.6):
        self.Kd = Kd
        self.Kp = Kp
    def controller(self,previous_error, current_error):
        control_action = (self.Kp * current_error) + self.Kd * (current_error - previous_error)
        return control_action