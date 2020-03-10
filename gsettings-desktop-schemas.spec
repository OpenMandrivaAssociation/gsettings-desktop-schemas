%define	debug_package	%nil
%define url_ver	%(echo %{version}|cut -d. -f1,2)

%define api	3.0
%define girname	%mklibname %{name}-gir %{api}

Summary:	Shared GSettings schemas for the desktop
Name:		gsettings-desktop-schemas
Version:	3.36.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://gnome.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gsettings-desktop-schemas/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	meson
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
Requires:	dconf
# MD needed for glib-compile-schemas
Requires:	glib2.0-common

%description
This contains a collection of GSettings schemas for settings shared by
various components of a desktop.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package devel
Group:		Development/C
Summary:	Development files for %{name}

%description devel
This contains a collection of GSettings schemas for settings shared by
various components of a desktop.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%doc README NEWS AUTHORS
%{_datadir}/GConf/gsettings/gsettings-desktop-schemas.convert
%{_datadir}/GConf/gsettings/wm-schemas.convert
%{_datadir}/glib-2.0/schemas/*.xml

%files -n %{girname}
%{_libdir}/girepository-1.0/GDesktopEnums-%{api}.typelib

%files devel
%doc ChangeLog HACKING MAINTAINERS
%{_includedir}/%{name}
%{_datadir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/GDesktopEnums-%{api}.gir

