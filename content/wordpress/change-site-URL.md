---
title: "Change site URL"
date: 2018-11-06T18:25:48.97
author: "Hadir Garcia-Castro"
type: technical-note
draft: false
---
# Change site URL

## If the fields are disabled

To change the WordPress home address or Site URL, however the fields are disable to be edited. Then find the wp-config.php file via FTP and open up it. Look for the `WP_HOME` or `WP_SITEURL` fields and erase them to enable the files in the WP panel again.
If they (the fileds) do not exist and you want to disable them, then write the following lines at the end of the file:

``` php
/** WP Home Address **/
define('WP_HOME','http://example.com');
define('WP_SITEURL','http://example.com');
```
