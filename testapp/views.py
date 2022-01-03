import pandas as pd
import scipy.stats as stats
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

import testapp.services as services
from testapp.models import DataType


class Calculate(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = User.objects.get(id=request.data["user_id"])
        data = request.data["data"]

        x_data_type = DataType.objects.get_or_create(name=data["x_data_type"])[0]
        y_data_type = DataType.objects.get_or_create(name=data["y_data_type"])[0]
        x_data = data["x"]
        y_data = data["y"]

        services.create_records(x_data, user, x_data_type)
        services.create_records(y_data, user, y_data_type)

        return Response(status=status.HTTP_200_OK)

    def get(self, request):
        res = services.get_df(request.query_params)

        if res["success"]:
            df = pd.DataFrame(res["data"])
            x_data_type = request.query_params["x_data_type"]
            y_data_type = request.query_params["y_data_type"]

            x_data = df[df["data_type"] == x_data_type]["value"].tolist()
            y_data = df[df["data_type"] == y_data_type]["value"].tolist()

            # conver django decimal.Decimal to python's native float
            x_data = [float(x) for x in x_data]
            y_data = [float(y) for y in y_data]

            # calculate correlation using scipy.stats.pearsonr
            correlation = stats.pearsonr(x_data, y_data)

            res = {
                "user_id": request.query_params["user_id"],
                "x_data_type": x_data_type,
                "y_data_type": y_data_type,
                "correlation": {
                    "value": correlation[0],
                    "p_value": correlation[1],
                }
            }

            return Response(res, status=status.HTTP_200_OK)

        return Response(res["error"], status=status.HTTP_404_NOT_FOUND)
