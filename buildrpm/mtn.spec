Name:		mtn	
Version: 	3.3.1
Release:	1%{?dist}
Summary:	Movie thumbnailer

Group:		Amusements/Graphics
License:	GPLv2
URL:		http://gitlab.com/movie_thumbnailer/mtn/
Source0:	https://gitlab.com/movie_thumbnailer/mtn/-/archive/master/mtn.tar.gz
#Source0:	https://gitlab.com/movie_thumbnailer/mtn/repository/%{version}/archive.tar.gz
#Source0:	https://gitlab.com/movie_thumbnailer/mtn/repository/archive.tar.gz?ref=%{version}

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	gd-devel >= 2.1.1
BuildRequires:	ffmpeg-devel >= 3.3.1

Requires:	gd
Requires:	ffmpeg-libs

%description
Movie thumbnail generator

%prep
rm -rf ./*
tar -xf %SOURCE0
mv mtn*/* ./

%build
cd src
%make_build

%install
cd src
%make_install

%files
%{_bindir}/mtn
%{_defaultdocdir}/mtn/*
%{_mandir}/man1/mtn.1*

%clean
rm -rf %{buildroot}
rm -rf *

%changelog
* Fri Jan 18 2019 wahibre  <wahibre@gmx.com> - 3.3.1
- update to version 3.3.1

* Wed May 16 2018 wahibre  <wahibre@gmx.com> - 3.3
- update to version 3.3

* Tue Jan 02 2018 wahibre  <wahibre@gmx.com> - 3.2.1
- update to version 3.2.1

* Tue Dec 05 2017 wahibre  <wahibre@gmx.com> - 3.2
- update to version 3.2

* Thu Nov 23 2017 wahibre  <wahibre@gmx.com> - 3.1
- update to version 3.1

* Mon Aug 7 2017 wahibre  <wahibre@gmx.com> - 3.0
- initial
