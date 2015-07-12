websheets: Online version of coding handouts with blanks
========================================================
Created originally by David Pritchard (daveagp@gmail.com) in 2013.
Released under the GNU Affero General Public License (but see
other licenses for subdirectories/subrepositories).

GETTING STARTED

See the list of the main components of the websheets system here:

http://cscircles.cemc.uwaterloo.ca/websheets.html

There are also other mirrors at USC and Princeton but they require that
you have an account at one of those schools.

INSTALLATION

Install these on your server first:
 https://github.com/cemc/safeexec
 https://github.com/daveagp/java_jail 
This requires root access. See the instructions therein for details. It is best to
install these in locations that are not served to users by your web server.

If you wish to run C++ problems through websheets, you need to do a 
couple of small changes to java_jail:
 - add a subdirectory "scratch" with apache write permission
 - add libraries libstdc++.so.6 & libgcc_s.so.1 to the jail

Next, in some folder accessible to your web server, run

git clone --recursive https://github.com/daveagp/websheets

Next, copy ws-config.example.json to ws-config.json. 
Set up the options in ws-config.json.

Run the commands in "install.sql", e.g. with:
  mysql database_name -u user_name -p < install.sql

Try visiting
 http://your.website/url/to/websheets/index.php
and everything should now work except authentication.

LOGIN MECHANISMS

Websheets doesn't currently let users create accounts or store
passwords, and instead it relies on third-party authentication.

It primarily uses an open-source module called "HybridAuth".
"HybridAuth" supports tons of providers but Websheets is most easily
prepared to utilize three: Facebook, Google and GitHub.
   
(a) To use one of these three open authenticators, you just have 
    to register your "application" (your local Websheets mirror) with 
    the corresponding provider and copy the id and secret into ws-config.json.

    Use your google "Client ID for web applications" and "Client secret"
    or facebook "App ID" and "App Secret".
    The receiving URI should be like
      http://your.website/url/to/websheets/hybridauth/hybridauth/index.php

    Delete the options you don't want to use in ws-config.json.

(b) If your school has Google Apps accounts for all students 
    (e.g., USC does this), you can enforce that _only_ students
    with accounts corresponding to your school may log in
    (e.g. to avoid strangers from consuming CPU cycles).
    Enter "google-apps-domain" and "required_username_suffix"
    in ws-config.json if you want to do this (in addition to
    your google app credentials).

(c) If using GitHub, you have to copy a file in hybridauth:
     cd hybridauth
     cp additional-providers/hybridauth-github/Providers/GitHub.php hybridauth/Hybrid/Providers/

Additional hybridauth providers can be added if you poke around
auth.php a bit.

Many schools (Waterloo, Princeton) also have PHP libraries 
that perform authentication for students specifically from their 
school. You can hook it up to Websheets by modifying auth.php
accordingly. For an example, see the Princeton-related code in auth.php.

ADDITIONAL SETUP

To download updates, you need two commands to get the subrepos:
   git pull; git submodule update

WARNING: You'll be putting a DB password in ws-config.json.
Please check that
     http://your.website/url/to/websheets/ws-config.json
is inaccessible; .htaccess tries to do this, but you should confirm it works.

THANKS

Thanks to the COS 126 staff at Princeton for offering feedback when using
this tool from Fall 2013 to Spring 2014: 
Donna Gabai, Maia Ginsburg, Bob Sedgewick and Doug Clark.

Thanks to Mark Redekopp at U. Southern California for great feedback when
the C++ backend was developed.


