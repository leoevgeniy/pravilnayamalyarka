from rest_framework import serializers
from .models import PromoSlider


class PromoSlidesSerializer(serializers.ModelSerializer):
	class Meta:
		model = PromoSlider
		fields= all
