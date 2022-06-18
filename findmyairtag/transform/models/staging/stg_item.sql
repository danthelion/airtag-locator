{{
  config(
    materialized='table'
  )
}}

-- extract raw fields
with raw as (
  select
    name as name,
    timestamp as ts,
    location ->> 'latitude' as latitude,
    location ->> 'longitude' as longitude,
    location ->> 'altitude' as altitude,
    role ->> 'emoji' as emoji
  from {{ source('tap_findmy', 'item') }}
)

-- Fix types
select
  latitude::float,
  longitude::float,
  altitude::float,
  ts,
  emoji,
  name
from raw
