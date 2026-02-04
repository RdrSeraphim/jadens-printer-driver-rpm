# jadens-printer-driver-rpm
[![Copr build status](https://copr.fedorainfracloud.org/coprs/srp/jadens-printer-driver/package/jadens-printer-driver/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/srp/jadens-printer-driver/package/jadens-printer-driver/)

A rebuild of JADENS' Debian package to properly work on RPM-based Linux distro.

This repo also modifies the behavior that would come with the original Debian package to avoid redundant files, since the original package would otherwise install a filter binary for every architecture it's been built for regardless of the system's architecture.

Builds are managed in COPR (see build status badge above), while source extraction and re-organization is done via GitHub Actions.

JADENS provides their Debian package through a non-static link, meaning updates to the ensemble have to be done manually.
