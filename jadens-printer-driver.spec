Name:           jadens-printer-driver
Version:        3.3.5.497
Release:        %autorelease
Summary:        CUPS support for JADENS thermal printing devices
License:        Proprietary
Source0:        %{name}-%{version}.tar.gz

ExclusiveArch:  x86_64
BuildRequires:  cups-devel

%description
CUPS support for JADENS thermal printing devices. Converted from Debian package.

%prep
%setup -q -c

%build

%install
mkdir -p %{buildroot}%{_libdir}/cups/filter
mkdir -p %{buildroot}%{_datadir}/cups/model/Jadens

cp -p usr/lib/cups/filter/jadens_printer_filter %{buildroot}%{_libdir}/cups/filter/
cp -p usr/share/cups/model/Jadens/*.ppd %{buildroot}%{_datadir}/cups/model/Jadens/

chmod 755 %{buildroot}%{_libdir}/cups/filter/jadens_printer_filter

%files
%dir %{_libdir}/cups
%dir %{_libdir}/cups/filter
attr(755,root,root) %{_libdir}/cups/filter/jadens_printer_filter
%dir %{_datadir}/cups
%dir %{_datadir}/cups/model
%dir %{_datadir}/cups/model/Jadens
%{_datadir}/cups/model/Jadens/*.ppd

%changelog
%autochangelog
