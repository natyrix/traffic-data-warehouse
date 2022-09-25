select "type" , AVG("avg_speed") as speed_avg
from "railway"."railway"."traffic_model"
Group by "type"