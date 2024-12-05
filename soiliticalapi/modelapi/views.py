import os
import pickle
import bz2
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PredictionInputSerializer

MODEL_PATH = "random_forest_model.pbz2"
ENCODER_PATH = "label_encoder.pbz2"

def load_pbz2(filename):
    with bz2.BZ2File(filename, 'rb') as file:
        return pickle.load(file)

class PredictionAPIView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = load_pbz2(
            os.path.join(settings.BASE_DIR, 'modelapi', 'ml_models', MODEL_PATH)
        )
        self.label_encoder = load_pbz2(
            os.path.join(settings.BASE_DIR, 'modelapi', 'ml_models', ENCODER_PATH)
        )

    def post(self, request, *args, **kwargs):
        serializer = PredictionInputSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            # Normalize soil type to match the valid choices in the serializer
            soil_type_normalized = data['soil_type'].strip().lower()

            # Check if the normalized soil type exists in the valid choices
            valid_soil_types = [choice[0] for choice in PredictionInputSerializer.SOIL_TYPE_CHOICES]
            if soil_type_normalized not in valid_soil_types:
                return Response(
                    {'error': f"Unknown soil type: {data['soil_type']}"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # You could map the normalized soil type to the encoded value here if necessary
            encoded_soil_type = valid_soil_types.index(soil_type_normalized)

            # Prepare values_list with the correct feature order
            values_list = [[
                encoded_soil_type,
                data['ec_value'],
                data['temperature'],
                data['n_value'],
                data['p_value'],
                data['k_value']
            ]]

            # Model prediction
            try:
                pred = self.model.predict(values_list)
            except Exception as e:
                return Response(
                    {'error': f"Model prediction failed: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            # Return the prediction result (this assumes the model predicts crop names)
            return Response({'prediction': self.label_encoder.inverse_transform(pred)[0]}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
