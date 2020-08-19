# translation-domain-report
Gives a percentage of translation between two languages of any page.

A small toll made in Python3 with BeautifulSoup.

The locale is set using URL parameters ex: https://golfgenius.com/leagues/4714361510128790175?locale=en

In this script we compare en(enghlish) and fr(french), but it can work with any languages if the domain has the correct configuration to support it.


Scan page with locale en. It finds all DOM elements from the list: ['p', 'a', 'span', 'li', 'h1', 'h2', 'h3', 'h4', 'h5'].

<p><img src="/images/en.png" width="520px"/></p>

Scan page with locale fr.

<p><img src="/images/fr.png" width="520px"/></p>


**Example**

We have a hardcoded text from the text from the main page

<p><img src="/images/example.png" width="520px"/></p>

If we run the script the result will be: 0.73% completed

<p><img src="/images/percentage1.png" width="520px"/></p>

If we migrate the code to suport translation

<p><img src="/images/example2.png" width="520px"/></p>

The new percentage will be: 1.09% completed

<p><img src="/images/percentage2.png" width="520px"/></p>


We can show word difference between two languages

<p><img src="/images/words.png" width="520px"/></p>
