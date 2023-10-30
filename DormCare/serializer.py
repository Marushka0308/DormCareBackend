from rest_framework import serializers
from .models import User
from .models import Complaints
from .models import Announcements

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['registration_number','username','password','email','phone_number','room_number','hostel_block']

class ComplaintsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaints
        fields = ['id','date','time','complaints','likes','status']

class AnnouncementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcements
        fields = ['announcement','date']