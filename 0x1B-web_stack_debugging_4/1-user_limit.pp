# 1-user_limit.pp
# This Puppet manifest configures the OS to increase the file descriptor limit for the holberton user.

exec { 'add-hard-file-limit':
  command => 'sed -i "/holberton hard/s/5/8192/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
  notify  => Exec['add-soft-file-limit'],
}

exec { 'add-soft-file-limit':
  command => 'sed -i "/holberton soft/s/4/8192/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

# Ensure that these changes take effect by reloading the PAM limits module
exec { 'reload-pam-limits':
  command => '/sbin/sysctl -p',
  path    => '/usr/sbin/:/sbin/:/usr/local/bin/:/bin/',
  require => Exec['add-soft-file-limit'],
}
