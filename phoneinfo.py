from phonenumbers import timezone,geocoder,carrier
import phonenumbers

def number_info(n):
    phone = phonenumbers.parse(n)
    time = timezone.time_zones_for_number(phone)
    car = carrier.name_for_number(phone,"en")
    reg = geocoder.description_for_number(phone,"en")
    print(time[0])
    print(car)
    print(reg)
