class IncidentDb():
    def __init__(self):
        self.incident_list = []

   
    def add_incident(self, incident):
        '''This method creates anew incident '''
        new_incident = incident.__dict__
        new_incident['incident_id'] = id
        self.incident_list.append(new_incident)
     
    def get_incident_by_id(self, incident_id):
        '''This fetches a prticular incident  '''
        for incident in self.incident_list:
            if incident.incident_id == incident_id:
                try:
                    return incident[0]
                except IndexError:    
                    return None 
    
    def get_all_incidents(self):
        '''This method fetchs all created incidents '''
        return self.incident_list


class IncidentDb():
    def __init__(self):
        self.incident_list = []

    def add_incident(self, incident):
        self.incident_list.append(incident)
        # print(self.incident_list)
     

    def get_incident_by_id(self, incident_id):
        for incident in self.incident_list:
            if incident.incident_id == incident_id:
                return incident
        return None 
    
    def get_incidents(self):
        # print(self.incident_list)
        return self.incident_list

    def get_incident_json(self):
        return [incident.to_json for incident in self.incident_list] 
    