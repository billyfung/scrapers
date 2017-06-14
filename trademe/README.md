This is to scrape information from trade me, since getting access to the API is a pain

A search result looks something like
```
http://www.trademe.co.nz/browse/categoryattributesearchresults.aspx?134=1&136=&153=&132=FLAT&59=0&59=0&122=0&122=0&29=&123=0&123=0&search=1&sidebar=1&cid=5748&rptpath=350-5748-
```

And a good place to start crawling would be
```
http://www.trademe.co.nz/property/residential-property-to-rent/auckland/auckland-city
```

Goal is the scrape all the residential listing for all the available information and plot heatmap of prices.