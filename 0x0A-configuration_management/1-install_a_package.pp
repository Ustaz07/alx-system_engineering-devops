# Puppet manifest to install Flask package

# Declare package resource to install Flask
package { 'flask':
  ensure => '2.1.0',
  provider => 'pip3',
}
