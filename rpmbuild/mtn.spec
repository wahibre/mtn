Name:		mtn	
Version: 	3.0
Release:	1%{?dist}
Summary:	Movie thumbnailer

Group:		Amusements/Graphics
License:	GPLv2
URL:		http://gitlab.com/movie_thumbnailer/mtn/
Source0:	%{name}.%{version}.tar.gz
                #wget -O %{name}.%{version}.tar.gz https://gitlab.com/movie_thumbnailer/mtn/repository/archive.tar.gz?ref=%{version}

BuildRequires:	gd-devel >= 2.2.2
BuildRequires:	ffmpeg-compat-devel >= 0.6.7

Requires:	gd
Requires:	ffmpeg-compat

%description
Movie thumbnail generator

%prep
tar -xzf %SOURCE0

%build
cd mtn*/src
%make_build

%install
cd mtn*/src
%make_install

%files
%{_bindir}/mtn
%{_defaultdocdir}/mtn/*

%clean
rm -rf %{buildroot}
rm -rf *

%changelog
* Mon Aug 7 2017 wahibre  <wahibre@gmx.com> - 3.0
- removed old and deprecated piece of code and replaced with new FFmpeg's (3.1.8) API
- add -X option to include video extension in output filename
- add -S option to select video stream
- add -d option to set recursion depth
- return code -1 on failure
