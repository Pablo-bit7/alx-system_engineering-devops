# This Puppet manifest ensures Apache is installed, running, and enabled.

# Fix the typo in wp-settings.php
exec { 'fix-wordpress':
  command => 'sed -i s/\.phpp/\.php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
}

# Ensure Apache is restarted if the typo is fixed
service { 'apache2':
  subscribe => Exec['fix-wordpress'],
}

