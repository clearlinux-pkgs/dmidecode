#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dmidecode
Version  : 3.0
Release  : 4
URL      : http://download-mirror.savannah.gnu.org/releases/dmidecode/dmidecode-3.0.tar.xz
Source0  : http://download-mirror.savannah.gnu.org/releases/dmidecode/dmidecode-3.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: dmidecode-bin
Requires: dmidecode-doc
Patch1: 0001-Use-modern-defaults.patch

%description
** INTRODUCTION **
Dmidecode reports information about your system's hardware as described in
your system BIOS according to the SMBIOS/DMI standard. This information
typically includes system manufacturer, model name, serial number, BIOS
version, asset tag as well as a lot of other details of varying level of
interest and reliability depending on the manufacturer. This will often
include usage status for the CPU sockets, expansion slots (e.g. AGP, PCI,
ISA) and memory module slots, and the list of I/O ports (e.g. serial,
parallel, USB).

%package bin
Summary: bin components for the dmidecode package.
Group: Binaries

%description bin
bin components for the dmidecode package.


%package doc
Summary: doc components for the dmidecode package.
Group: Documentation

%description doc
doc components for the dmidecode package.


%prep
%setup -q -n dmidecode-3.0
%patch1 -p1

%build
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/biosdecode
/usr/bin/dmidecode
/usr/bin/ownership
/usr/bin/vpddecode

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/dmidecode/*
%doc /usr/share/man/man8/*
