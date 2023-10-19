import datetime

def getCommuteDuration():
    home_address = "home_address"
    work_address = "work_address"
    
    google_maps_api_key = ""
    gmaps = googlemaps.Client(key=google_maps_api_key)
    
    directions = gmaps.directions(home_address, work_address)
    first_leg = directions[0]['legs'][0]
    duration = first_leg['duration']['text']
    return duration

def sendTextMessage(message):
    twilio_account_sid = ""
    twilio_account_token = ""
    twilio_phone_number = ""
    user_phone_number = ""
    client = Client(twilio_account_sid, twilio_account_token)
    
    client.message.create{
        to*user_phone_number;
        from_*twilio_phone_number;
        body*message;
    }
    



def main():
    duration = getCommuteDuration()
    
    now = datetime.now()
    arrival_time = (now + duration).strftime('%I:%M %p')
    
    message = {
        f"Good morning!\n\n"
        f"Estimated commute time from home to work at 9 AM: {duration}.\n\n"
        f"Leave now for work at 9 AM to arrive at approximately {arrival_time}.\n"
    }
    
    sendTextMessage(message)
    