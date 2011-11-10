Summary: Shared GSettings schemas for the desktop
Name: gsettings-desktop-schemas
Version: 3.2.0
Release: 1
Source0: http://ftp.gnome.org/pub/GNOME/sources/gsettings-desktop-schemas/%{name}-%{version}.tar.xz
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://gnome.org/

BuildRequires: glib2-devel >= 2.25
BuildRequires: intltool
BuildArch: noarch

%description
This contains a collection of GSettings schemas for settings shared by
various components of a desktop.

%package devel
Group: Development/C
Summary: Development files for %name

%description devel
This contains a collection of GSettings schemas for settings shared by
various components of a desktop.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std pkgconfigdir=%_datadir/pkgconfig

%find_lang %name

%files -f %{name}.lang
%doc README NEWS AUTHORS
%_datadir/GConf/gsettings/gsettings-desktop-schemas.convert
%_datadir/glib-2.0/schemas/*.xml

%files devel
%doc ChangeLog HACKING MAINTAINERS
%_includedir/%name
%_datadir/pkgconfig/%name.pc
