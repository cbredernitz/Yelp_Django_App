from yelp.models import Business, Attire, Review, NoiseLevel, City, State
from api.serializers import BusinessSerializer
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response


class BusinessViewSet(viewsets.ModelViewSet):
	"""
	This ViewSet provides both 'list' and 'detail' views.
	"""
	queryset = Business.objects.select_related('attire', 'noise_level', 'city', 'state').order_by('business_name')
	serializer_class = BusinessSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def delete(self, request, pk, format=None):
		business = self.get_object(pk)
		self.perform_destroy(self, business)

		return Response(status=status.HTTP_204_NO_CONTENT)

	def perform_destroy(self, instance):
		instance.delete()


'''
class SiteListAPIView(generics.ListCreateAPIView):
	queryset = HeritageSite.objects.select_related('heritage_site_category').order_by('site_name')
	serializer_class = HeritageSiteSerializer
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
'''

'''
class SiteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = HeritageSite.objects.select_related('heritage_site_category').order_by('site_name')
	serializer_class = HeritageSiteSerializer
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
'''