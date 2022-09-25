select "type" , AVG("traveled_d") as dist_avg
from "railway"."railway"."traffic_model"
Group by "type"