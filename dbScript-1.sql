--1. Get the full address of all companies along with their stock ticker name.,

select * from endeavour.company_locations cl ;
select * from endeavour.stocks_lookup sl ;


select address, city, state, ticker_name 
from endeavour.company_locations cl 
join endeavour.stocks_lookup sl 
on sl.ticker_symbol = cl.ticker_symbol ;

-- 2. Find the total market capitalization for each sector along with sector names.,

select * from endeavour.sector_lookup slp;
select * from endeavour.stock_fundamentals sf  ;

select slp.sector_name,sf.sector_id, sum(sf.market_cap)
from endeavour.sector_lookup slp 
join endeavour.stock_fundamentals sf
on sf.sector_id =slp.sector_id 
group by slp.sector_name,sf.sector_id ;

-- 3.List the stock symbols and the highest closing price for each stock in each state.,

select * from endeavour.stocks_price_history sph ;
select * from endeavour.state_lookup sl ;
select * from endeavour.stock_fundamentals sf ;

select sph.ticker_symbol, max(close_price), cl.state
from endeavour.company_locations cl  
join endeavour.stocks_price_history sph 
on sph.ticker_symbol =cl.ticker_symbol 
group by sph.ticker_symbol , cl.state
order by cl.state , sph.ticker_symbol ;



-- 4. Find all stocks with a price-to-earnings ratio (PE) less than 15 and sort them by ticker symbol.,

select ticker_symbol, price_to_book_ratio
from endeavour.stock_fundamentals sf 
where sf.price_to_book_ratio < 15
order by sf.ticker_symbol ;






-- 5.Retrieve all stock price histories for 'AAPL' within the last 30 days and order by trading date.,

select * from endeavour.stocks_price_history sph 
where sph.ticker_symbol ='AAPL'
and sph.trading_date >= CURRENT_DATE - INTERVAL '30' day
order by trading_date;

--  6.List the names of all companies located in the state of 'California'.,
select  sl.ticker_name,cl.state 
from endeavour.company_locations cl 
join endeavour.stocks_lookup sl on sl.ticker_symbol = cl.ticker_symbol
where cl.state='CA';

-- 7.find all stocks where the current raio is greater than the average current ration of all stocks.



select sf.ticker_symbol ,sf.current_ratio 
from endeavour.stock_fundamentals sf 
where sf.current_ratio > (select avg(sf.current_ratio) as avg_ratio
from endeavour.stock_fundamentals sf);


-- 8. Generate a monthly summary of average open and close prices for each stock.,
select ticker_symbol, avg(open_price),avg(close_price),
date_trunc('month',trading_date) as month
from endeavour.stocks_price_history sph 
group by sph.ticker_symbol , date_trunc('month',trading_date)
order by month;

-- 9. Find all stocks with ticker symbols that contain the substring 'TECH'.,
select sf.ticker_symbol, sf.subsector_id, sl.subsector_name
from endeavour.stock_fundamentals sf 
join endeavour.subsector_lookup sl 
on sl.subsector_id = sf.subsector_id ;

-- 10. Calculate the average debt-equity ratio for each sector.

select sf.sector_id ,avg(sf.debt_equity_ratio ),sl.sector_name 
from endeavour.stock_fundamentals sf 
join endeavour.sector_lookup sl 
on sl.sector_id =sf.sector_id 
group by sl.sector_name , sf.sector_id ;







