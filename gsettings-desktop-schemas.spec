%define name gsettings-desktop-schemas
%define version 2.91.92
%define release %mkrel 1

Summary: Shared GSettings schemas for the desktop
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://gnome.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README NEWS AUTHORS
%_datadir/GConf/gsettings/gsettings-desktop-schemas.convert
%_datadir/glib-2.0/schemas/*.xml

%files devel
%defattr(-,root,root)
%doc ChangeLog HACKING MAINTAINERS
%_includedir/%name
%_datadir/pkgconfig/%name.pc
