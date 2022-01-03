from datetime import datetime
from django.contrib.auth.models import User
from testapp.models import Record, DataType


def create_records(data, user, data_type):
    template = {
        "user": user,
        "data_type": data_type,
        "recorded_date": None,
        "value": None,
    }

    for item in data:
        template["recorded_date"] = datetime.strptime(item["date"], "%Y-%m-%d")
        template["value"] = item["value"]
        Record.objects.create(**template)


def get_df(params):
    try:
        x_data_type = DataType.objects.get(name=params["x_data_type"])
        y_data_type = DataType.objects.get(name=params["y_data_type"])

        user = User.objects.get(id=params["user_id"])

        x_data = Record.objects.filter(user=user, data_type=x_data_type)
        y_data = Record.objects.filter(user=user, data_type=y_data_type)
    except Exception as e:
        return {"success": False, "error": str(e)}

    data = {
        "recorded_date": [],
        "value": [],
        "data_type": [],
    }

    for x, y in zip(x_data, y_data):
        data["recorded_date"].append(x.recorded_date.strftime("%Y-%m-%d"))
        data["value"].append(x.value)
        data["data_type"].append(x.data_type.name)

        data["recorded_date"].append(y.recorded_date.strftime("%Y-%m-%d"))
        data["value"].append(y.value)
        data["data_type"].append(y.data_type.name)

    return {"success": True, "data": data}
