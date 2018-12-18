from yelp.models import Business, Attire, User, Review, \
	NoiseLevel, City, State
from rest_framework import response, serializers, status


class AttireSerializer(serializers.ModelSerializer):

	class Meta:
		model = Attire
		fields = ('attire_id', 'attire')


class CitySerializer(serializers.ModelSerializer):

	class Meta:
		model = City
		fields = ('city_id', 'city_name')


class NoiseLevelSerializer(serializers.ModelSerializer):

	class Meta:
		model = NoiseLevel
		fields = ('noise_level_id', 'noise')


class StateSerializer(serializers.ModelSerializer):

	class Meta:
		model = State
		fields = ('state_id', 'state_abbrev')


class ReviewSerializer(serializers.ModelSerializer):
	user_id = serializers.ReadOnlyField(source='user.user_id')
	business_id = serializers.ReadOnlyField(source='business.business_id')

	class Meta:
		model = Review
		fields = ('business_id', 'user_id')


class BusinessSerializer(serializers.ModelSerializer):
	business_name = serializers.CharField(
		allow_blank=False,
		max_length=100
	)

	noise_level = NoiseLevelSerializer(
		many=False,
		read_only=True
	)
	noise_level_id = serializers.PrimaryKeyRelatedField(
		allow_null=True,
		many=False,
		write_only=True,
		queryset=NoiseLevel.objects.all(),
		source='noise_level'
	)
	attire = AttireSerializer(
		many=False,
		read_only=True
	)
	attire_id = serializers.PrimaryKeyRelatedField(
		allow_null=True,
		many=False,
		write_only=True,
		queryset=Attire.objects.all(),
		source='attire'
	)
	city = CitySerializer(
		many=False,
		read_only=True
	)
	city_id = serializers.PrimaryKeyRelatedField(
		allow_null=False,
		many=False,
		write_only=True,
		queryset=City.objects.all(),
		source='city'
	)
	state = StateSerializer(
		many=False,
		read_only=True
	)
	state_id = serializers.PrimaryKeyRelatedField(
		allow_null=False,
		many=False,
		write_only=True,
		queryset=State.objects.all(),
		source='state'
	)
	address = serializers.CharField(
		allow_blank=False,
		max_length=100
	)
	neighborhood = serializers.CharField(
		allow_blank=True,
		max_length=100
	)
	postal_code = serializers.CharField(
		allow_blank=True,
		max_length=100
	)
	longitude = serializers.DecimalField(
		allow_null=True,
		max_digits=10,
		decimal_places=2
	)
	latitude = serializers.DecimalField(
		allow_null=True,
		max_digits=10,
		decimal_places=2
	)
	business_stars = serializers.DecimalField(
		allow_null=False,
		max_digits=10,
		decimal_places=2
	)
	business_review_count = serializers.IntegerField(
		allow_null=False
	)
	is_open = serializers.IntegerField(
		allow_null=False
	)

	class Meta:
		model = Business
		fields = (
			'business_id',
			'business_name',
			'noise_level',
			'noise_level_id',
			'attire',
			'attire_id',
			'city',
			'city_id',
			'state',
			'state_id',
			'address',
			'neighborhood',
			'postal_code',
			'longitude',
			'latitude',
			'business_stars',
			'business_review_count',
			'is_open'
		)

	def create(self, validated_data):
		"""
		"""

		business = Business.objects.create(**validated_data)

		return business

	def update(self, instance, validated_data):
		# site_id = validated_data.pop('heritage_site_id')
		business_id = instance.business_id

		instance.business_name = validated_data.get(
			'business_name',
			instance.business_name
		)
		instance.noise_level_id = validated_data.get(
			'noise_level_id',
			instance.noise_level_id
		)
		instance.attire_id = validated_data.get(
			'attire_id',
			instance.attire_id
		)
		instance.city_id = validated_data.get(
			'city_id',
			instance.city_id
		)
		instance.state_id = validated_data.get(
			'state_id',
			instance.state_id
		)
		instance.address = validated_data.get(
			'address',
			instance.address
		)
		instance.neighborhood = validated_data.get(
			'neighborhood',
			instance.neighborhood
		)
		instance.postal_code = validated_data.get(
			'postal_code',
			instance.postal_code
		)
		instance.longitude = validated_data.get(
			'longitude',
			instance.longitude
		)
		instance.latitude = validated_data.get(
			'latitude',
			instance.latitude
		)
		instance.business_stars = validated_data.get(
			'business_stars',
			instance.business_stars
		)
		instance.business_review_count = validated_data.get(
			'business_review_count',
			instance.business_review_count
		)
		instance.is_open = validated_data.get(
			'is_open',
			instance.is_open
		)
		instance.save()

		return instance