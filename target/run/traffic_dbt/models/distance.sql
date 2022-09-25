
  create view "railway"."railway"."distance__dbt_tmp" as (
    select traveled_d,count(*) from transformed_data_final group by traveled_d order by count DESC
  );