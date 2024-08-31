from rest_framework.throttling import UserRateThrottle

class Jackcreatethrottle(UserRateThrottle):
    scope='jack'