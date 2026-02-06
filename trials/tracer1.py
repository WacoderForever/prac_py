import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def start_phone_tracer(target):
    print(f"[+] Phonetracer v2.1 - OSINT")
    print(f"[+] Target: {target}")
    print(f"[*] Initiating trace...")
    
    try:
        p = phonenumbers.parse(target, None)
        
        # Get location information
        location = geocoder.description_for_number(p, "en")
        print(f"[+] Location: {location}")
        
        # Get carrier information
        carrier_name = carrier.name_for_number(p, "en")
        print(f"[+] Carrier: {carrier_name}")
        
        # Get timezone information
        time_zones = timezone.time_zones_for_number(p)
        print(f"[+] Timezone(s): {', '.join(time_zones)}")
        
        print(f"[+] Trace Complete")
        
    except phonenumbers.NumberParseException as e:
        print(f"[!] Error: Invalid phone number - {e}")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

# Example usage
start_phone_tracer("+2547xxxxxxxx")