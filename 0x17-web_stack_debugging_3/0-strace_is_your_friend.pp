# This Puppet manifest ensures Apache is installed, running, and enabled.

# Ensure Apache is installed
package { 'apache2':
  ensure => installed,
}

# Ensure Apache service is running and enabled
service { 'apache2':
  ensure  => running,
  enable  => true,
  require => Package['apache2'],
}

# Fix the typo in wp-settings.php
exec { 'fix-wordpress':
  command => 'sed -i s/\.phpp/\.php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
  onlyif  => 'grep \.phpp /var/www/html/wp-settings.php',
  require => Service['apache2'],
}

# Ensure Apache is restarted if the typo is fixed
service { 'apache2':
  subscribe => Exec['fix-wordpress'],
}
