
  create view "railway"."railway"."avg_speed_by_type__dbt_tmp" as (
    select "type" , AVG("avg_speed") as speed_avg
from "railway"."railway"."traffic_model"
Group by "type"
  );