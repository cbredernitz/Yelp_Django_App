import django_filters
from yelp.models import User, Review, Business


class UserFilter(django_filters.FilterSet):
    user_name = django_filters.CharFilter(
        field_name='user_name',
        label='User Name',
        lookup_expr='icontains'
    )

    # description = django_filters.CharFilter(
    #     field_name='description',
    #     label='Description',
    #     lookup_expr='icontains'
    # )

    business = django_filters.ModelChoiceFilter(
        field_name='business',
        label='Reviewed Businesses',
        queryset=Business.objects.all().order_by('business_name'),
        lookup_expr='exact'
    )

    # region = django_filters.ModelChoiceFilter(
    #     field_name='country_area__location__region__region_name',
    #     label='Region',
    #     queryset=Region.objects.all().order_by('region_name'),
    #     lookup_expr='exact'
    # )

    # sub_region = django_filters.ModelChoiceFilter(
    #     field_name='country_area__location__sub_region__sub_region_name',
    #     label='Sub Region',
    #     queryset=SubRegion.objects.all().order_by('sub_region_name'),
    #     lookup_expr='exact'
    # )

    # intermediate_region = django_filters.ModelChoiceFilter(
    #     field_name='country_area__location__intermediate_region__intermediate_region_name',
    #     label='Intermediate Region',
    #     queryset=IntermediateRegion.objects.all().order_by('intermediate_region_name'),
    #     lookup_expr='exact'
    # )

    # country_area = django_filters.ModelChoiceFilter(
    #     field_name='country_area',
    #     label='Country/Area',
    #     queryset=CountryArea.objects.all().order_by('country_area_name'),
    #     lookup_expr='exact'
    # )

    useful = django_filters.NumberFilter(
        field_name='useful',
        label='Useful User',
        # queryset=User.objects.all().order_by(''),
        lookup_expr='gte'
    )

    class Meta:
        model = User
        # form = SearchForm
        # fields [] is required, even if empty.
        fields = []