select "type" , AVG("traveled_d") as dist_avg
from {{ ref('traffic_model') }}
Group by "type"