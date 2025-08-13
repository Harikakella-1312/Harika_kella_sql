-- 1. Find stocks with higher ROE than ANY tech sector stock,

select * from endeavour.subsector_lookup sl ;
select * from  endeavour.stock_fundamentals;
select * from endeavour.sector_lookup sl ;

select subl.subsector_name,sl.sector_id 
from endeavour.subsector_lookup subl
join endeavour.sector_lookup sl on sl.sector_id = subl.sector_id
where subl.sector_id!=37;


select sl.sector_name,sf.sector_id,sf.roe
from endeavour.stock_fundamentals sf 
join endeavour.sector_lookup sl 
on sl.sector_id=sf.sector_id
where sf.roe > any (select sf.roe 
from endeavour.stock_fundamentals sf 
where sl.sector_name!='Technology')
order by sl.sector_name ,sf.sector_id ;


-- 2. Find stocks with market cap higher than ALL small-cap stocks,
select market_cap from endeavour.stock_fundamentals sf ;

select sf.market_cap, sl.ticker_name
from endeavour.stock_fundamentals sf 
join endeavour.stocks_lookup sl 
on sl.ticker_symbol = sf.ticker_symbol
group by sf.market_cap, sl.ticker_name
having  max(sf.market_cap) > 20000000;

-- 3. Find stocks with market cap > $10 billion and has offices in CA (Use CTE)

select sf.market_cap , sl.ticker_name, cl.state
from endeavour.stock_fundamentals sf
join endeavour.stocks_lookup sl 
on sl.ticker_symbol = sf.ticker_symbol
join endeavour.company_locations cl
on cl.ticker_symbol = sf.ticker_symbol
group by sf.market_cap, sl.ticker_name, cl.state
having sf.market_cap > 10000000000 and cl.state='CA'
order by ticker_name;

-- 4.write a query to get sector performance by calculating the below,
-- 4.1 For each sector, count the number of unique stocks.

select sl.sector_name  ,sf.sector_id , count(distinct slp.ticker_name ) as unique_stock_count
from endeavour.stock_fundamentals sf 
join endeavour.stocks_lookup slp
on slp.ticker_symbol = sf.ticker_symbol 
join endeavour.sector_lookup sl 
on sl.sector_id =sf.sector_id 
group by sl.sector_name, sf.sector_id 
order by unique_stock_count;

--4.2 calculate the median market capitalization for the stocks within each sector --- windows






-- 4.3 the average Return on Equity (ROE) for the stocks within each sector.
select sl.sector_name, sf.roe, avg(sf.roe)
over (partition by sector_name) as avg_roe
from endeavour.sector_lookup sl 
join endeavour.stock_fundamentals sf 
on sf.sector_id =sl.sector_id;

-- 4.4 Based on the average ROE, classify each sector's performance as 'High ROE' 
-- (greater than 0.15), 'Medium ROE' (greater than 0.08), or 'Low ROE' (0.08 or less). ----windows

select distinct sl.sector_name, sf.roe, 
avg(roe) over (partition by sl.sector_name) as avg_roe,
case when avg(roe) > 0.15 then 'High roe'
     when avg(roe) > 0.08 then 'medium roe'
     else 'low roe'
end as performance
from endeavour.sector_lookup sl
join endeavour.stock_fundamentals sf
on sf.sector_id = sl.sector_id
group by sl.sector_name,sf.roe
order by sl.sector_name,performance ;

-- 4.5 If no stocks exist in a sector, the stock count should display 'No Stocks'.
	select * from endeavour.stock_fundamentals sf ;


select sl.sector_name, sf.ticker_symbol,
case when count()
from endeavour.sector_lookup sl 
join endeavour.stock_fundamentals sf 
on sf.sector_id =sl.sector_id 




-- 5.calculate the daily return and identify periods of high volatility for each stock.
-- Write a query satisfying below conditions 
-- 5.1 Select the ticker symbol, trading date, and closing price for each stock.

select sph.ticker_symbol, sph.trading_date , 
sph.close_price ,sl.ticker_name 
from endeavour.stocks_price_history sph 
join endeavour.stocks_lookup sl 
on sl.ticker_symbol = sph.ticker_symbol
order by sl.ticker_name 


-- 5.2 Calculate the daily return as a percentage for each stock, 
-- rounded to two decimal places.

SELECT 
    ticker_symbol,
    trading_date,
    close_price,
    ROUND(((close_price - LAG(close_price) OVER (
    PARTITION BY ticker_symbol ORDER BY trading_date
)) / LAG(close_price) OVER (
    PARTITION BY ticker_symbol ORDER BY trading_date
) * 100)::numeric, 2)
FROM endeavour.stocks_price_history;

-- 5.3 Identify days with high volatility, where the absolute 
--change in closing price from the previous day is greater than 5 units,
-- and label these days as 'High Volatility'. Otherwise, label them as 
--'Normal'.







-- 6. Find the 4th, 5th and 6th highest market cap stocks for
-- each sector of the economy

select sector_id, ticker_symbol, market_cap 
from (
select sector_id , market_cap, ticker_symbol,
rank() over(partition by sector_id
order by market_cap desc) as rnk
from endeavour.stock_fundamentals)
as ranked
where rnk in (4,5,6);


-- 7. For each year, get the stock with highest close price - Using Window Functions
-- What are the top 5 stock names with an average closing price above $150, 
-- considering only days when the closing price was greater than $100, sorted
-- by their average price in descending orde

select sph.ticker_symbol , 
date_part('year',sph.trading_date ) as year_only ,max(sph.close_price)
over (partition by sph.trading_date ) as max_closing_price
from endeavour.stocks_price_history sph
group by sph.ticker_symbol,sph.trading_date  ;


select ranked.ticker_name , ranked.avg_close_price, ranked.rnk
from
( select sl.ticker_name , avg(sph.close_price ) as avg_close_price,
rank() over(partition by sl.ticker_name 
order by sph.close_price desc) as rnk
from endeavour.stocks_price_history sph 
join endeavour.stocks_lookup sl 
on sl.ticker_symbol = sph.ticker_symbol 
where sph.close_price >100
group by sl.ticker_name, sph.close_price 
having avg(close_price)>150)
as ranked
where rnk in (1,2,3,4,5)
order by ranked.avg_close_price desc ;


select ranked.ticker_name , ranked.avg_close_price, ranked.rnk,
ranked.ticker_symbol ,ranked.year_only , ranked.max_closing_price 
from
( select sl.ticker_name , avg(sph.close_price ) as avg_close_price,
rank() over(partition by sl.ticker_name
order by sph.close_price desc) as rnk, 
sph.ticker_symbol , 
date_part('year',sph.trading_date ) as year_only ,max(sph.close_price)
over (partition by sph.trading_date ) as max_closing_price
from endeavour.stocks_price_history sph 
join endeavour.stocks_lookup sl 
on sl.ticker_symbol = sph.ticker_symbol 
where sph.close_price >100
group by sl.ticker_name, sph.close_price, sph.ticker_symbol ,sph.trading_date  
having avg(close_price)>150)
as ranked
where rnk in (1,2,3,4,5)
order by ranked.avg_close_price desc ;



 












