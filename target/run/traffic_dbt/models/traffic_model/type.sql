
  create view "railway"."railway"."type__dbt_tmp" as (
    select "type" , COUNT(id) as type_val
from "railway"."railway"."traffic_model"
Group by "type"
  );