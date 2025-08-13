-- 1.Find the List of companies that share the same
-- city but are located in different states.

-- Only include subsector/city combinations where more than
-- one distinct state exists.

select ssl.subsector_name, cl.city
from endeavour.subsector_lookup ssl 
join endeavour.stock_fundamentals sf 
on sf.subsector_id = ssl.subsector_id
join endeavour.company_locations cl 
on cl.ticker_symbol = sf.ticker_symbol
group by ssl.subsector_name,cl.city
having count(distinct cl.state) > 1
order by ssl.subsector_name, cl.city


-- 2. List companies whose EPS is greater than the overall average EPS
with eps_with_avg
as (select sl.subsector_name , sf.eps_ttm,
avg(sf.eps_ttm ) over (partition by sl.subsector_name) as avg_eps_ttm
from endeavour.subsector_lookup sl 
join endeavour.stock_fundamentals sf 
on sf.sector_id =sl.sector_id )
select subsector_name , eps_ttm, avg_eps_ttm
from eps_with_avg 
where eps_ttm > avg_eps_ttm;


-- 3.Finding Top 5 Companies by Market Cap in Each Sector

select sector_name, market_cap
from ( select slp.sector_name, sf.market_cap,
rank() over (partition by slp.sector_name 
order by sf.market_cap) as rnk 
from endeavour.sector_lookup slp
join endeavour.stock_fundamentals sf 
on sf.sector_id = slp.sector_id )
as ranked
where rnk in (1,2,3,4,5)

-- 4.Calculate the Average Trading Volume for Each Sector Over the Past Month

select sf.sector_id , round(avg(sph.volume ),2) as avg_trad_vol
from endeavour.stocks_price_history sph 
join endeavour.stock_fundamentals sf 
on sf.ticker_symbol =sph.ticker_symbol 
where sph.trading_date >= current_date - interval '1 month'
group by sf.sector_id
order by avg_trad_vol
;




-- 5.Identifying Companies with Consistent Growth in EPS Over the Past Year


WITH eps_with_prev AS (
    SELECT 
        sf.sector_id,
        sph.trading_date,
        sf.eps_ttm,
        LAG(sf.eps_ttm) OVER (PARTITION BY sf.ticker_symbol
        ORDER BY sph.trading_date) AS prev_eps
    FROM endeavour.stock_fundamentals sf
    JOIN endeavour.stocks_price_history sph
      ON sph.ticker_symbol = sf.ticker_symbol
    WHERE sph.trading_date >= CURRENT_DATE - INTERVAL '1 year'
)
SELECT 
    sector_id ,
    COUNT(*) AS total_periods,
    SUM(CASE WHEN eps_ttm > prev_eps 
    THEN 1 ELSE 0 END) AS growth_periods
FROM eps_with_prev
WHERE prev_eps IS NOT NULL
GROUP BY sector_id 
ORDER BY growth_periods DESC
LIMIT 20;












