{{
  config(
    materialized='table'
  )
}}


select
  latitude,
  longitude,
  ts,
  concat(emoji, ' ', name) as item_label
from {{ ref('stg_item') }}
where ts > current_date - interval '1 day'
