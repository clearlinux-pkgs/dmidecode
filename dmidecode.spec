#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xA5526B9BB3CD4E6A (jdelvare@suse.de)
#
Name     : dmidecode
Version  : 3.5
Release  : 16
URL      : https://download-mirror.savannah.gnu.org/releases/dmidecode/dmidecode-3.5.tar.xz
Source0  : https://download-mirror.savannah.gnu.org/releases/dmidecode/dmidecode-3.5.tar.xz
Source1  : https://download-mirror.savannah.gnu.org/releases/dmidecode/dmidecode-3.5.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: dmidecode-bin = %{version}-%{release}
Requires: dmidecode-license = %{version}-%{release}
Requires: dmidecode-man = %{version}-%{release}
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
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
Requires: dmidecode-license = %{version}-%{release}

%description bin
bin components for the dmidecode package.


%package doc
Summary: doc components for the dmidecode package.
Group: Documentation
Requires: dmidecode-man = %{version}-%{release}

%description doc
doc components for the dmidecode package.


%package license
Summary: license components for the dmidecode package.
Group: Default

%description license
license components for the dmidecode package.


%package man
Summary: man components for the dmidecode package.
Group: Default

%description man
man components for the dmidecode package.


%prep
%setup -q -n dmidecode-3.5
cd %{_builddir}/dmidecode-3.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678834518
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1678834518
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dmidecode
cp %{_builddir}/dmidecode-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/dmidecode/4cc77b90af91e615a64ae04893fdffa7939db84c || :
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
%defattr(0644,root,root,0755)
%doc /usr/share/doc/dmidecode/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dmidecode/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/biosdecode.8
/usr/share/man/man8/dmidecode.8
/usr/share/man/man8/ownership.8
/usr/share/man/man8/vpddecode.8
