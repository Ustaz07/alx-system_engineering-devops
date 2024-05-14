# Puppet manifest to install Flask package

# Ensure Flask package is installed using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
