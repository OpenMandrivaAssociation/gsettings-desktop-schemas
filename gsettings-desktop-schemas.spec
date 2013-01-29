%define name gsettings-desktop-schemas
%define version 3.7.4
%define release 1

Summary: Shared GSettings schemas for the desktop
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/gsettings-desktop-schemas/3.7/%{name}-%{version}.tar.xz
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://gnome.org/
BuildRequires: pkgconfig(glib-2.0) >= 2.25
BuildRequires: intltool
BuildRequires: libgirepository-devel
BuildRequires: gobject-introspection
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
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std pkgconfigdir=%_datadir/pkgconfig

%find_lang %name

%files -f %{name}.lang
%doc README NEWS AUTHORS
%_datadir/GConf/gsettings/gsettings-desktop-schemas.convert
%_datadir/GConf/gsettings/wm-schemas.convert
%_libdir/girepository-1.0/GDesktopEnums-3.0.typelib
%_datadir/glib-2.0/schemas/*.xml
%_datadir/gir-1.0/GDesktopEnums-3.0.gir

%files devel
%doc ChangeLog HACKING MAINTAINERS
%_includedir/%name
%_datadir/pkgconfig/%name.pc
