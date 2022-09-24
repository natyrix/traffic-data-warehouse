select "type" , AVG("traveled_d") 
from {{ ref('traffic_model') }}
Group by "type"