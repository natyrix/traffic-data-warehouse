
  create view "railway"."railway"."traffic_model__dbt_tmp" as (
    

with traffic_model as (

    select * from transformed_data_final

)

select *
from traffic_model
  );