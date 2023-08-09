# Fix class-wp-locale.phpp to class-wp-locale.pp

exec { 'wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
