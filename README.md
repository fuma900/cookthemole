CookTheMole - v0.0.1
===========

**Website**: https://cookthemole.appspot.com/

**API endpoint**: https://cookthemole.appspot.com/_ah/api/

**Backend**:

>Parse recipes websites (with no direct requests from the server)*** using python + BS4
on a Google App Engine server.
The client can connect through an API created using Google Endpoints.

>It's made out of 3 components:
- **Logic** *(parse-url.py)*: look for the provider-specific file in the "provider" folder and does all the hard work on the data scraped
- **Parser** *(provider/website_com.py)*: scrape instruction for the specific website
- **API** *(cookthemole_api.py)*: expose data from parse-url.py using Google Endpoints.

**Chrome Extension**:
>Enable handfree cooking using voice recognition and TTS.

**Supported websites:**
>- allreciepes.com (Alpha)

**To do:**
>- change filename and varaibles to use CamelCase
- protect API with API keys (remove google login)
- change the connection schema to be like:
  - client asks the server for directions
  - server instructs client about what the request must be
  - client make the request and send data to the server
  - server return the results

*** Not yet implemented - This way server doesn't make any request to other servers (avoiding IP blocks and other problems)
and the client use the most of the bandwidth (server doesn't have to open the whole html page but just read plain text).
