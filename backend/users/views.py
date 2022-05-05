import json
import logging
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from users.models import Profile, User
from .serializers import ProfileSerializer
from rest_framework.response import Response
# Create your views here.


logger = logging.getLogger(__name__)


@csrf_exempt
def create_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = data['user']
        email = user['email']
        password = user['password']
        print(email, password)
        user_id = User.objects.create_user(email, password)
        logger.info("User created")
        if 'profile' in data:
            profile_data = data['profile']
            profile = Profile.objects.get(user=user_id)
            if 'first_name' in profile_data:
                profile.first_name = profile_data['first_name']
            if 'last_name' in profile_data:
                profile.last_name = profile_data['last_name']
            if 'bio' in profile_data:
                profile.bio = profile_data['bio']
            if 'phone' in profile_data:
                profile.phone = profile_data['phone']
            profile.save()
            logger.info("Profile saved")
        return HttpResponse(user_id)


class ProfileViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.UpdateModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        profile = self.queryset.get(user=self.request.user)
        serializer = self.serializer_class(instance=profile)
        logger.info("Get profile " + str(serializer.data))
        return Response(serializer.data)
