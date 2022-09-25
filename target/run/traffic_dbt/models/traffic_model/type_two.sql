
  create view "railway"."railway"."type_two__dbt_tmp" as (
    select d_avg.dist_avg, s_avg.speed_avg, t_val.type_val
from "railway"."railway"."avg_distance_by_type" as d_avg, "railway"."railway"."avg_speed_by_type" as s_avg,
 "railway"."railway"."type" as t_val
  );