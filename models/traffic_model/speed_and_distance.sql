select d_avg.dist_avg, s_avg.speed_avg, t_val.type_val
from {{ ref('avg_distance_by_type') }} as d_avg, {{ ref('avg_speed_by_type') }} as s_avg,
 {{ ref('type') }} as t_val