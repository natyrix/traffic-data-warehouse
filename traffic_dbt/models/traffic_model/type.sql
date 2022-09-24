select "type" , COUNT(id) as type_val
from {{ ref('traffic_model') }}
Group by "type"