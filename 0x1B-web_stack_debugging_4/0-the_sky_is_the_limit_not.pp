# 0-the_sky_is_the_limit_not.pp
# This Puppet manifest optimizes Nginx for high concurrency capabilities.

exec { 'increase-trafic-nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  notify  => Exec['restart-nginx'],
}

exec { 'restart-nginx':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Exec['tune-nginx'],
}

service { 'apache2':
  ensure => stopped,
}
