 curl -L --insecure -x 172.30.71.80:3128 -X GET 'http://www.google.com' -vv
Note: Unnecessary use of -X or --request, GET is already inferred.
*   Trying 172.30.71.80:3128...
* Connected to 172.30.71.80 (172.30.71.80) port 3128 (#0)
> GET http://www.google.com/ HTTP/1.1
> Host: www.google.com
> User-Agent: curl/7.71.1
> Accept: */*
> Proxy-Connection: Keep-Alive
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 403 Forbidden
< Server: squid/3.5.20
< Mime-Version: 1.0
< Date: Fri, 11 Oct 2024 08:33:25 GMT
< Content-Type: text/html;charset=utf-8
< Content-Length: 3553
< X-Squid-Error: ERR_ACCESS_DENIED 0
< Vary: Accept-Language
< Content-Language: en
< X-Cache: MISS from squid-dkb.sigma-belpsb.by
< X-Cache-Lookup: NONE from squid-dkb.sigma-belpsb.by:3128
< Via: 1.1 squid-dkb.sigma-belpsb.by (squid/3.5.20)
< Connection: keep-alive
<
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>
<meta type="copyright" content="Copyright (C) 1996-2016 The Squid Software Foundation and contributors">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>ERROR: The requested URL could not be retrieved</title>
<style type="text/css"><!--
 /*
 * Copyright (C) 1996-2016 The Squid Software Foundation and contributors
 *
 * Squid software is distributed under GPLv2+ license and includes
 * contributions from numerous individuals and organizations.
 * Please see the COPYING and CONTRIBUTORS files for details.
 */

/*
 Stylesheet for Squid Error pages
 Adapted from design by Free CSS Templates
 http://www.freecsstemplates.org
 Released for free under a Creative Commons Attribution 2.5 License
*/

/* Page basics */
* {
        font-family: verdana, sans-serif;
}

html body {
        margin: 0;
        padding: 0;
        background: #efefef;
        font-size: 12px;
        color: #1e1e1e;
}

/* Page displayed title area */
#titles {
        margin-left: 15px;
        padding: 10px;
        padding-left: 100px;
        background: url('/squid-internal-static/icons/SN.png') no-repeat left;
}

/* initial title */
#titles h1 {
        color: #000000;
}
#titles h2 {
        color: #000000;
}

/* special event: FTP success page titles */
#titles ftpsuccess {
        background-color:#00ff00;
        width:100%;
}

/* Page displayed body content area */
#content {
        padding: 10px;
        background: #ffffff;
}

/* General text */
p {
}

/* error brief description */
#error p {
}

/* some data which may have caused the problem */
#data {
}

/* the error message received from the system or other software */
#sysmsg {
}

pre {
    font-family:sans-serif;
}

/* special event: FTP / Gopher directory listing */
#dirmsg {
    font-family: courier;
    color: black;
    font-size: 10pt;
}
#dirlisting {
    margin-left: 2%;
    margin-right: 2%;
}
#dirlisting tr.entry td.icon,td.filename,td.size,td.date {
    border-bottom: groove;
}
#dirlisting td.size {
    width: 50px;
    text-align: right;
    padding-right: 5px;
}

/* horizontal lines */
hr {
        margin: 0;
}

/* page displayed footer area */
#footer {
        font-size: 9px;
        padding-left: 10px;
}


body
:lang(fa) { direction: rtl; font-size: 100%; font-family: Tahoma, Roya, sans-serif; float: right; }
:lang(he) { direction: rtl; }
 --></style>
</head><body id=ERR_ACCESS_DENIED>
<div id="titles">
<h1>ERROR</h1>
<h2>The requested URL could not be retrieved</h2>
</div>
<hr>

<div id="content">
<p>The following error was encountered while trying to retrieve the URL: <a href="http://www.google.com/">http://www.google.com/</a></p>

<blockquote id="error">
<p><b>Access Denied.</b></p>
</blockquote>

<p>Access control configuration prevents your request from being allowed at this time. Please contact your service provider if you feel this is incorrect.</p>

<p>Your cache administrator is <a href="mailto:root?subject=CacheErrorInfo%20-%20ERR_ACCESS_DENIED&amp;body=CacheHost%3A%20squid-dkb.sigma-belpsb.by%0D%0AErrPage%3A%20ERR_ACCESS_DENIED%0D%0AErr%3A%20%5Bnone%5D%0D%0ATimeStamp%3A%20Fri,%2011%20Oct%202024%2008%3A33%3A25%20GMT%0D%0A%0D%0AClientIP%3A%20172.30.56.91%0D%0A%0D%0AHTTP%20Request%3A%0D%0AGET%20%2F%20HTTP%2F1.1%0AUser-Agent%3A%20curl%2F7.71.1%0D%0AAccept%3A%20*%2F*%0D%0AProxy-Connection%3A%20Keep-Alive%0D%0AHost%3A%20www.google.com%0D%0A%0D%0A%0D%0A">root</a>.</p>
<br>
</div>

<hr>
<div id="footer">
<p>Generated Fri, 11 Oct 2024 08:33:25 GMT by squid-dkb.sigma-belpsb.by (squid/3.5.20)</p>
<!-- ERR_ACCESS_DENIED -->
</div>
</body></html>
* Connection #0 to host 172.30.71.80 left intact
