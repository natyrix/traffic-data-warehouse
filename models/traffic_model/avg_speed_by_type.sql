select "type" , AVG("avg_speed") as speed_avg
from {{ ref('traffic_model') }}
Group by "type"