from rest_framework import serializers

class PredictionInputSerializer(serializers.Serializer):
    SOIL_TYPE_CHOICES = [
        ('loamy soil', 'loamy soil'),
        ('clayey soil - loamy soil', 'clayey soil - loamy soil'),
        ('well-drained - loamy soil', 'well-drained - loamy soil'),
        ('sandy clay', 'sandy clay'),
        ('sandy loam - silt loam', 'sandy loam - silt loam')
    ]

    soil_type = serializers.ChoiceField(choices=SOIL_TYPE_CHOICES, default='loamy soil')
    n_value = serializers.FloatField(required=True, min_value=0.0, help_text="Nitrogen value in soil")
    p_value = serializers.FloatField(required=True, min_value=0.0, help_text="Phosphorous value in soil")
    k_value = serializers.FloatField(required=True, min_value=0.0, help_text="Potassium value in soil")
    ec_value = serializers.FloatField(required=True, min_value=0.0, help_text="Electrical conductivity of the soil")
    temperature = serializers.FloatField(required=True, min_value=-50.0, max_value=100.0, help_text="Temperature in degrees Celsius")
