---
title: "Create a child theme"
date: 2018-11-15T13:34:00.518
author: "Hadir Garcia-Castro"
type: technical-note
draft: false
---
# Create a child theme

To create a child them on Wordpress do the following steps:

## Step 1
Open you server directory via FTP, find you domine and into the `wp-content` folder find the `themes`folder.

## Step 2
Into the `themes` folder, create a new folder and name it as `child-theme`.

## Step 3
Create two files, a `style.css` file and a `functions.php` file, and write the following lines into them.

`# style.css`

``` css
/*
Theme Name: theme-child
Theme URI: https://dev.hadir.ga/
Description: This is a custom child theme I have created.
Author: Author's Name
URI: https://www.hadir.ga/
Template: parent-theme
Version: 0.1
*/
```

`functions.php`
``` php
<?php
if ( !defined( 'ABSPATH' ) ) exit;

if ( !function_exists( 'hadirga_child_parent_css' ) ):
    function theme_child_parent_css() {
        wp_enqueue_style( 'hadirga_child_parent', trailingslashit( get_template_directory_uri() ) . 'style.css', array( 'bootstrap' ) );
	if( is_rtl() ) {
		wp_enqueue_style( 'hadirga_child_parent_rtl', trailingslashit( get_template_directory_uri() ) . 'style-rtl.css', array( 'bootstrap' ) );
	}

    }
endif;
add_action( 'wp_enqueue_scripts', 'hadirga_child_parent_css', 10 );

/**
 * Import options from hadirga
 *
 * @since 1.0.0
 */
function hadirga_child_get_lite_options() {
	$hadirga_mods = get_option( 'theme_mods_hadirga' );
	if ( ! empty( $hadirga_mods ) ) {
		foreach ( $hadirga_mods as $hadirga_mod_k => $hadirga_mod_v ) {
			set_theme_mod( $hadirga_mod_k, $hadirga_mod_v );
		}
	}
}
add_action( 'after_switch_theme', 'hadirga_child_get_lite_options' );

```

Finaly, if you want to have a custom screenshot image for your child theme, then add it to the folder with the name `screenshot.png`.
