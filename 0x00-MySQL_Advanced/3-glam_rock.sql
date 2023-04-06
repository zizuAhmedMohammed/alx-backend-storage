-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
-- Column names must be: band_name and lifespan (in years)
-- Use attributes formed and split for computing the lifespan
-- The script can be executed on any database

SELECT band_name, EXTRACT(YEAR FROM DATE_TRUNC('year', NOW())) - MAX(split) AS lifespan 
FROM metal_bands 
WHERE style LIKE '%Glam rock%' GROUP BY band_name 
ORDER BY lifespan DESC;
