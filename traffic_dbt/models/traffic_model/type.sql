select "type" , COUNT(id) 
from {{ ref('traffic_model') }}
Group by "type"