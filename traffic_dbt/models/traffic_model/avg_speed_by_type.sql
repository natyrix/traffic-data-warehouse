select "type" , AVG("avg_speed") 
from {{ ref('traffic_model') }}
Group by "type"