
  create view "railway"."railway"."avg_distance_by_type__dbt_tmp" as (
    select "type" , AVG("traveled_d") as dist_avg
from "railway"."railway"."traffic_model"
Group by "type"
  );