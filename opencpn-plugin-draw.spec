%global commit 8d4f6f679a92eb9372fa90d943987d51b3e6a68d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global owner jongough
%global plugin ocpn_draw

Name: opencpn-plugin-draw
Summary: OpenCPN general drawing plugin
Version: 1.4.4
Release: 1.%{shortcommit}%{?dist}
License: GPLv2+

Source0: https://github.com/%{owner}/%{plugin}_pi/archive/%{commit}/%{plugin}_pi-%{shortcommit}.tar.gz

BuildRequires: bzip2-devel
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: gtk3-devel
BuildRequires: tinyxml-devel
BuildRequires: wxGTK3-devel
BuildRequires: zlib-devel

Requires: opencpn%{_isa}
Enhances: opencpn%{_isa}
Provides: opencpn-plugin-ocpn_draw%{_isa} = %{version}-%{release}

%description
The OpenCPN Draw plugin is designed to allow users to place
objects/items on the OpenCPN interface and have these georeferenced.
This allows the objects/items to move with the chart and have a
definined latitude and longitude.

%prep
%autosetup -n %{plugin}_pi-%{commit}

sed -i -e s'/SET(PREFIX_LIB lib)/SET(PREFIX_LIB %{_lib})/' cmake/PluginInstall.cmake

mkdir build

%build

cd build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF ..
%make_build

%install

cd build
mkdir -p %{buildroot}%{_bindir}
%make_install

%find_lang opencpn-%{plugin}_pi

%files -f build/opencpn-%{plugin}_pi.lang

%{_libdir}/opencpn/lib%{plugin}_pi.so

%{_datadir}/opencpn/plugins/%{plugin}_pi
