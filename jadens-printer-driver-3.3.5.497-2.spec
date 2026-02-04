Name: jadens-printer-driver
Version: 3.3.5.497
Release: 2
Summary: jadens-printer-driver
License: see /usr/share/doc/jadens-printer-driver/copyright
Distribution: Debian

%define _rpmdir ../
%define _rpmfilename %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm
%define _unpackaged_files_terminate_build 0

%description
CUPS support for JADENS thermal printing devices.

%files
%dir "/usr/lib/cups/"
%dir "/usr/lib/cups/filter/"
"/usr/lib/cups/filter/jadens_printer_filter"
%dir "/usr/share/cups/"
%dir "/usr/share/cups/model/"
%dir "/usr/share/cups/model/Jadens/"
"/usr/share/cups/model/Jadens/JD-268.ppd"
"/usr/share/cups/model/Jadens/BY-245.ppd"
"/usr/share/cups/model/Jadens/JD-568P.ppd"
"/usr/share/cups/model/Jadens/JD-166.ppd"
"/usr/share/cups/model/Jadens/JD-468BT.ppd"
"/usr/share/cups/model/Jadens/JD-338.ppd"
"/usr/share/cups/model/Jadens/JD-168.ppd"
"/usr/share/cups/model/Jadens/BY-C10.ppd"
"/usr/share/cups/model/Jadens/PD-A4(NEW).ppd"
"/usr/share/cups/model/Jadens/JD-328.ppd"
"/usr/share/cups/model/Jadens/PD-A4Pro(NEW).ppd"
"/usr/share/cups/model/Jadens/JD-468.ppd"
"/usr/share/cups/model/Jadens/JD-328BT.ppd"
"/usr/share/cups/model/Jadens/Label Printer(4inch).ppd"
"/usr/share/cups/model/Jadens/PD-A4.ppd"
"/usr/share/cups/model/Jadens/JD-268BT-AD.ppd"
"/usr/share/cups/model/Jadens/JD-24.ppd"
"/usr/share/cups/model/Jadens/BY-426BT.ppd"
"/usr/share/cups/model/Jadens/JD-136.ppd"
"/usr/share/cups/model/Jadens/JD-116.ppd"
"/usr/share/cups/model/Jadens/BY-426.ppd"
"/usr/share/cups/model/Jadens/JD-868WF.ppd"
"/usr/share/cups/model/Jadens/JD-468BT_Pro.ppd"
"/usr/share/cups/model/Jadens/JD-156T.ppd"
"/usr/share/cups/model/Jadens/JD-668BT.ppd"
"/usr/share/cups/model/Jadens/BY-245BT.ppd"
"/usr/share/cups/model/Jadens/JD-126.ppd"
"/usr/share/cups/model/Jadens/PD-A4Pro.ppd"
"/usr/share/cups/model/Jadens/PeriPage A40.ppd"
"/usr/share/cups/model/Jadens/C10.ppd"
"/usr/share/cups/model/Jadens/JD-668Pro.ppd"
"/usr/share/cups/model/Jadens/Label Printer(3inch).ppd"
"/usr/share/cups/model/Jadens/JD-668Pro-BT_Dongle.ppd"
"/usr/share/cups/model/Jadens/JD-668Pro-DG.ppd"
"/usr/share/cups/model/Jadens/JD-168BT.ppd"
"/usr/share/cups/model/Jadens/JD-156.ppd"
"/usr/share/cups/model/Jadens/JD-268BT.ppd"
"/usr/share/cups/model/Jadens/JD-338BT.ppd"
"/usr/share/cups/model/Jadens/JD-768WF.ppd"
