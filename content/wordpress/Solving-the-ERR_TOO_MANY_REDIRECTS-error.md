---
title: "Solving the `ERR_TOO_MANY_REDIRECTS` error"
date: 2018-11-06T18:30:48.97
author: "Hadir Garcia-Castro"
type: technical-note
draft: false
---
# Solving the `ERR_TOO_MANY_REDIRECTS` error

A kind of `ERR_TOO_MANY_REDIRECTS` error is when we try to acces the `wp-admin` page.

After trying to change the site address using the popular internet solution, add a couple of line into the `wp-config.php` file:

``` php
/** WP Home Address **/
define('WP_HOME','http://example.com');
define('WP_SITEURL','http://example.com');
```

Those lines of code do not work correctly and the solution is to change the address fields directly from database. Follow the steps:

1. Access the cPanel
2. Access the phpMyAdmin
3. Select the database of you website
4. Select the options table
5. Modify the fields `home` and `siteurl` with the correct address.

After that, your website will be working again.
