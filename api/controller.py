from flask import request, jsonify, json
from api.incident_model import Incident, IncidentDb, Base_Incident
from api.utilities import IncidentValidator
incident_list = IncidentDb()
class IncidentController():
    def __init__(self):
        pass
  
    def create_incident(self):
        data = request.get_json()
        #incident_id = data.get("incident_id")
        createdBy = data.get("createdBy")
        createdOn = data.get("created_on")
        flag_type = data.get("flag_type")
        location = data.get("location")
        status = data.get("status")
        images = data.get("images")
        videos = data.get("videos")
        comment = data.get("comment")
      
        #validation of user input
    
       
        if not  IncidentValidator.validate_status(status):
            return jsonify ({'status': 400,
                            'error': 'The status provided is not defined'
        })
        if not IncidentValidator.validate_flag_type(flag_type):
            return jsonify ({'status': 400,
                            'error': 'The flag_type is not defined'
            })
       

        new_incindent = Incident(Base_Incident(createdOn, createdBy, 
         flag_type, location), status, images, videos, comment)
        
        incident_list.add_incident(new_incindent)
        #incident = new_incindent.to_json()
        return jsonify({
            "status": 201,
            'data':[{
                'incident_id':new_incindent.id,
             "message": f"created {flag_type} "}]
                
            }), 201

    def get_mall_incidents(self):
        '''geting all incidents '''
        response = incident_list.get_all_incidents()
        return jsonify ({'status':200, 
                        'data':response
        }),200

    def get_a_specific_incident(self, icident_id):
        response = incident_list.get_incident_by_id
        return jsonify({'data':response}) 

    
