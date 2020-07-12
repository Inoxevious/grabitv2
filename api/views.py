# *coding: utf-8*
from backoffice.models import User
from api.serializers import *
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework_gis.filters import DistanceToPointFilter
@api_view(['POST'])
def createpaymentintent(request):
    if request.method == "POST":
        amount =  request.data["amount"]
        stripe.api_key = "pk_test_51GslFEGN6hwQCl2kYrHGNohCYqg8P4mmTWl8a7CS8tz9jaREYCLKSxvkuZjFg7bgWa0CYsiLfuonhpBj5BtrdRsB00hNez14LZ"
        intent = stripe.PaymentIntent.create(
            amount=int(amount),
            currency='eur',
        )
        return JsonResponse(intent, safe=False)
    else:
        return HttpResponse(status=501)
class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

        def get_distance(self, obj):
            return obj.distance_to_user.km

class PackageListView(generics.ListAPIView):
    """
            get:
                Get list of Packages
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    """
    distance_filter_field = 'location'
    filter_backends = (DistanceToPointFilter,)
    distance_filter_convert_meters = True
    """
    def get_queryset(self):
        latitude = self.request.query_params.get('latitude', None)
        longitude = self.request.query_params.get('longitude', None)
        max_distance = self.request.query_params.get('max_distance', None)
        if latitude and longitude:
            point_of_user = Point(float(longitude), float(latitude), srid=4326)
            # Here we're actually doing the query, notice we're using the Distance class fom gis.measure
            queryset = Package.objects.filter(
                location__distance_lte=(
                    point_of_user,
                    Distance(km=float(max_distance))
                )
            ).annotate(distance_to_user = DistanceModel("location",point_of_user)).order_by('distance_to_user')
        else:
            queryset = Package.objects.all()
        return queryset




class UserListView(generics.ListAPIView):
    """
            get:
                Search or get users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('email', 'username')

class UserListCreateView(generics.ListCreateAPIView):
    """
            create:
                add users
            get:
                Search or get users
                You can search using:
                    :param email
                    :param username
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('email', 'username','password')

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
            get:
                get a specific user
            delete:
                Remove an existing user.
            patch:
                Update one or more fields on an existing user.
            put:
                Update a user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer