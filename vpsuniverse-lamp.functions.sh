#!/usr/bin/env bash

#
# vpsuniverse lamp functions
#
# (c) 2024, VPS Universe
#

vpsuniverse_lamp_install() { lamp_install && [[ "${IAM,,}" == 'debian' ]]; }

setup_vpsuniverse_lamp() {
  debug '# setup vpsuniverse lamp'
  setup_lamp || return 1
  if debian_buster_image; then
    setup_adminer || return 1
  else
    setup_phpmyadmin || return 1
  fi
  setup_webmin
}

# vim: ai:ts=2:sw=2:et
